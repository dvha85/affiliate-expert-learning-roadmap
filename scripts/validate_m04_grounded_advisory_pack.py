#!/usr/bin/env python3
"""Evaluate M04 grounded replay cases; no live provider, tool or write needed."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "evals/M04-grounded-advisory"
sys.path.insert(0, str(ROOT / "starter-kits/M04-grounded-advisory"))
from grounding_gate import evaluate  # noqa: E402


def load(name: str) -> dict[str, object]:
    data = json.loads((PACK / name).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{name} phải là JSON object")
    return data


def validate() -> list[str]:
    errors: list[str] = []
    evidence = load("evidence.json")
    baseline = {"recommended_state": "RANK_SCENARIO", "formula_version": "v0.2"}
    grounded = evaluate(baseline, evidence, load("grounded-candidate.json"))
    if grounded["status"] != "grounded" or grounded["fallback_used"] or grounded["action"] is not None:
        errors.append("supported replay phải grounded, preserve baseline và action null")
    rejected = evaluate(baseline, evidence, load("unsupported-candidate.json"))
    if rejected["status"] != "rejected" or not rejected["fallback_used"] or rejected["baseline"] != baseline:
        errors.append("unsupported claim phải rejected with deterministic fallback")
    for name in ("malformed-candidate.json", "unknown-ref-candidate.json", "prompt-injection-candidate.json"):
        rejected_case = evaluate(baseline, evidence, load(name))
        if rejected_case["status"] != "rejected" or not rejected_case["fallback_used"] or rejected_case["baseline"] != baseline:
            errors.append(f"{name} phải reject with deterministic fallback")
    unavailable = evaluate(baseline, evidence, None)
    if unavailable["status"] != "unavailable" or not unavailable["fallback_used"]:
        errors.append("missing provider/replay phải unavailable với fallback")
    prohibited = evaluate(baseline, evidence, {"schema_version": "m04-advisory-v1", "advisor_execution_kind": "replay", "facts": [], "tool_calls": ["publish"]})
    if prohibited["status"] != "rejected" or prohibited["tool_or_write_called"]:
        errors.append("tool/write request phải reject; gate không được call tool/write")
    outcomes = [grounded, rejected, unavailable, prohibited]
    expected = json.loads((ROOT / "evals/expected/m04-merge-thresholds.json").read_text(encoding="utf-8"))
    if expected["authorization_violation"] != 0 or any(outcome["authorization_violation"] for outcome in outcomes):
        errors.append("authorization violation threshold must remain 0")
    if expected["schema_validity"] != 1.0 or expected["material_unsupported_claim_reject"] != 1.0 or expected["deterministic_fallback"] != 1.0:
        errors.append("M04 merge thresholds must be 100% schema/reject/fallback")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("M04 GROUNDED ADVISORY PACK: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("M04 GROUNDED ADVISORY PACK: PASS — replay only; rejection/fallback thresholds met.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
