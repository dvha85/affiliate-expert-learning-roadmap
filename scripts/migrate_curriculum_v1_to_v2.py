#!/usr/bin/env python3
"""Report the v1 → v2 Mission mapping without modifying learner state."""
from __future__ import annotations

import argparse
from pathlib import Path

MAPPING = (
    ("M03 First Tracked Manual Publish", "M00 First Safe Market Loop", "human-owned E1→E2 market loop"),
    ("M04 Real Outcome Analytics", "M01 First Outcome Snapshot", "manual/read-only E3 measurement"),
    ("M00 First Evidence-Backed Decision", "M02 Smallest Deterministic Bot", "deterministic A0 baseline"),
    ("M01 Trustworthy History", "M03 Trustworthy History & Measurement", "append-only evidence history"),
    ("M02 Grounded AI Advisor", "M04 Grounded AI Advisor", "A1 advisory with fallback"),
)


def report(root: Path) -> str:
    lines = [
        "CURRICULUM V1 → V2: DRY RUN ONLY",
        "No files, learner progress, evidence or PASS state will be changed.",
        "",
        "| v1 reference | v2 next Mission | scope |",
        "|---|---|---|",
    ]
    for old, new, scope in MAPPING:
        lines.append(f"| {old} | {new} | {scope} |")
    lines.extend(
        [
            "",
            "Keep completed lesson IDs as knowledge credit only.",
            "Reuse evidence only when provenance/freshness/scope still fit; do not relabel it.",
            "Personal state belongs in workspace/ (ignored), not in this report.",
        ]
    )
    if not (root / "docs/CURRICULUM-MIGRATION-v2.md").exists():
        lines.append("WARNING: migration guide is missing.")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Report the Curriculum v1 → v2 mapping")
    parser.add_argument("--dry-run", action="store_true", help="required acknowledgement; no write mode exists")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    if not args.dry_run:
        parser.error("only --dry-run is supported; this tool never migrates learner files")
    print(report(args.root.resolve()), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
