#!/usr/bin/env python3
"""Evaluate M02's deterministic baseline fixtures without any AI/tool call."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STARTER = ROOT / "starter-kits/M02-deterministic-baseline"
sys.path.insert(0, str(STARTER))
from baseline import evaluate  # noqa: E402


def load(name: str) -> list[dict[str, object]]:
    data = json.loads((ROOT / "evals/M02-deterministic-baseline" / name).read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError(f"{name} phải là JSON list")
    return data


def validate() -> list[str]:
    errors: list[str] = []
    ranked = evaluate(load("rankable-observations.json"))
    if ranked["recommended_state"] != "RANK_SCENARIO":
        errors.append("rankable fixture phải trả RANK_SCENARIO")
    if [row["subject_id"] for row in ranked["ranking"]] != ["synthetic-a", "synthetic-b"]:
        errors.append("ranking phải deterministic với stable subject_id tie-break")
    if ranked["action"] is not None or ranked["ai_or_tool_called"] is not False:
        errors.append("M02 không được gọi AI/tool hoặc tạo action")
    missing = evaluate(load("missing-evidence-observations.json"))
    if missing["recommended_state"] != "GET_MORE_DATA" or missing["action"] is not None:
        errors.append("missing evidence phải abstain GET_MORE_DATA với action null")
    if not missing["missing_evidence"]:
        errors.append("GET_MORE_DATA phải nêu missing_evidence")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("M02 DETERMINISTIC PACK: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("M02 DETERMINISTIC PACK: PASS — synthetic evaluator only; no AI/tool/action.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
