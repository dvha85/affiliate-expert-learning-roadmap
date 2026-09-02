#!/usr/bin/env python3
"""Print a compact Markdown view of Mission delivery readiness."""
from __future__ import annotations

import argparse
from pathlib import Path

try:
    from scripts.validate_readiness import collect
except ModuleNotFoundError:
    from validate_readiness import collect


def main() -> int:
    parser = argparse.ArgumentParser(description="Báo cáo readiness metadata của Mission")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    records, problems = collect(args.root.resolve())
    if problems:
        for problem in problems:
            print(problem)
        return 1
    print("| Mission | Curriculum | Release | Delivery | Pilot |")
    print("|---|---:|---|---|---|")
    for record in records:
        delivery = "complete" if record.delivery_complete else "incomplete"
        print(f"| {record.mission_id} | v{record.curriculum_version} | {record.release_kind} | {delivery} | {record.pilot_status} |")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
