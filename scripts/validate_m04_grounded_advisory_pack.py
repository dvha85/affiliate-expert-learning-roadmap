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
    unavailable = evaluate(baseline, evidence, None)
    if unavailable["status"] != "unavailable" or not unavailable["fallback_used"]:
        errors.append("missing provider/replay phải unavailable với fallback")
    prohibited = evaluate(baseline, evidence, {"facts": [], "tool_calls": ["publish"]})
    if prohibited["status"] != "rejected" or prohibited["tool_or_write_called"]:
        errors.append("tool/write request phải reject; gate không được call tool/write")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("M04 GROUNDED ADVISORY PACK: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("M04 GROUNDED ADVISORY PACK: PASS — replay only; no tool/write/execution.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
