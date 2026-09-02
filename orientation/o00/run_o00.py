#!/usr/bin/env python3
"""Print/validate the O00 synthetic trace; it never performs an external action."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.validate_contract_registry import validate


def load() -> dict[str, object]:
    return json.loads((ROOT / "contracts/examples/o00-trace.json").read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the safe O00 synthetic orientation")
    parser.add_argument("--validate", action="store_true")
    args = parser.parse_args()
    if args.validate:
        errors = validate(ROOT)
        if errors:
            for error in errors:
                print(error)
            return 1
        print("O00: PASS — synthetic full trace, no external side effect.")
        return 0
    print(json.dumps(load(), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
