#!/usr/bin/env python3
"""Machine-checkable simulation of the manual M02 operator rule card."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

BASELINE = Path(__file__).resolve().parents[1] / "M02-deterministic-baseline"
sys.path.insert(0, str(BASELINE))
from baseline import evaluate


def main() -> int:
    parser = argparse.ArgumentParser(description="Apply the M02 operator rule card")
    parser.add_argument("observations", type=Path)
    args = parser.parse_args()
    rows = json.loads(args.observations.read_text(encoding="utf-8"))
    if not isinstance(rows, list):
        raise SystemExit("observations JSON phải là list")
    print(json.dumps(evaluate(rows), ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
