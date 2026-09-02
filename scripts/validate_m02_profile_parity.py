#!/usr/bin/env python3
"""Compare the M02 Operator rule-card profile with the Go golden oracle."""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OPERATOR = ROOT / "starter-kits/M02-operator-profile"
GO_PROFILE = ROOT / "starter-kits/M02-go-builder"
sys.path.insert(0, str(OPERATOR))
from run_operator import evaluate

CASES = ("valid", "missing", "observed-zero", "malformed", "duplicate", "identity-conflict", "mixed-currency", "deterministic-tie")


def normalize(value: Any) -> Any:
    if isinstance(value, float) and value.is_integer():
        return int(value)
    if isinstance(value, list):
        return [normalize(item) for item in value]
    if isinstance(value, dict):
        return {key: normalize(item) for key, item in value.items()}
    return value


def canonical(value: Any) -> str:
    return json.dumps(normalize(value), ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def operator_result(path: Path) -> tuple[int, str]:
    try:
        rows = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(rows, list):
            return 2, "observations JSON phải là list"
        return 0, canonical(evaluate(rows))
    except (OSError, json.JSONDecodeError) as exc:
        return 2, str(exc)


def go_result(path: Path) -> tuple[int, str]:
    env = dict(os.environ)
    env.setdefault("GOCACHE", "/tmp/affiliate-m02-go-cache")
    run = subprocess.run(
        ["go", "run", "main.go", str(path)],
        cwd=GO_PROFILE,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )
    return run.returncode, run.stdout.strip() if run.returncode == 0 else run.stderr.strip()


def validate(include_go: bool = True) -> list[str]:
    errors: list[str] = []
    expected = json.loads((ROOT / "evals/expected/m02-profile-states.json").read_text(encoding="utf-8"))
    for name in CASES:
        path = ROOT / "evals/cases/m02" / f"{name}.json"
        operator_code, operator_output = operator_result(path)
        expected_state = expected[name]
        if name == "malformed":
            if operator_code == 0:
                errors.append("operator profile accepted malformed JSON")
        else:
            if operator_code != 0:
                errors.append(f"operator profile failed valid JSON case {name}: {operator_output}")
            else:
                result = json.loads(operator_output)
                if result.get("recommended_state") != expected_state:
                    errors.append(f"operator case {name} expected {expected_state}, got {result.get('recommended_state')}")
                if result.get("action") is not None or result.get("ai_or_tool_called") is not False:
                    errors.append(f"operator case {name} violated no-action/no-AI boundary")
        if not include_go:
            continue
        go_code, go_output = go_result(path)
        if name == "malformed":
            if go_code == 0:
                errors.append("Go profile accepted malformed JSON")
            continue
        if go_code != 0:
            errors.append(f"Go profile failed case {name}: {go_output}")
            continue
        if canonical(json.loads(go_output)) != operator_output:
            errors.append(f"profile parity mismatch for {name}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Check M02 Operator/Go parity")
    parser.add_argument("--operator-only", action="store_true", help="skip Go; useful before Go is installed")
    args = parser.parse_args()
    errors = validate(include_go=not args.operator_only)
    if errors:
        print("M02 PROFILE PARITY: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    scope = "operator profile only" if args.operator_only else "Operator/Go parity"
    print(f"M02 PROFILE PARITY: PASS — {scope}; no AI/tool/action.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
