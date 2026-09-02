#!/usr/bin/env python3
"""Validate the O00 safety invariant: synthetic orientation never acts."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED = {
    "orientation_only": True,
    "evidence_kind": "synthetic",
    "recommended_state": "GET_MORE_DATA",
    "action": None,
}


def validate(path: Path) -> list[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    errors: list[str] = []
    for key, expected in REQUIRED.items():
        if data.get(key) != expected:
            errors.append(f"{key} phải là {expected!r}; hiện là {data.get(key)!r}")
    if data.get("observation", {}).get("source_url") is not None:
        errors.append("O00 không được chứa public/real source_url")
    if not data.get("missing_evidence"):
        errors.append("O00 phải nêu missing_evidence")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Kiểm O00 synthetic walkthrough")
    parser.add_argument("--fixture", type=Path, default=Path(__file__).resolve().parents[1] / "orientation/o00/o00-synthetic-decision.json")
    args = parser.parse_args()
    errors = validate(args.fixture)
    if errors:
        print("O00: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("O00: PASS — synthetic orientation is non-actionable.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
