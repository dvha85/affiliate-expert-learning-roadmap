#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from baseline import evaluate


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the M02 deterministic baseline")
    parser.add_argument("observations", type=Path)
    args = parser.parse_args()
    data = json.loads(args.observations.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise SystemExit("observations JSON phải là một list")
    print(json.dumps(evaluate(data), ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
