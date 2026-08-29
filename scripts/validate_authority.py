#!/usr/bin/env python3
"""Fail when repository guidance contradicts the active curriculum authority."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACTIVE = ROOT / "CURRICULUM.md"
SOURCES_README = ROOT / "sources" / "README.md"

COUNT_RE = re.compile(
    r"(?:Tổng cộng:\s*)?\*\*(\d+)\s+(?:phần|Parts?)\s*·\s*(\d+)\s+(?:chương|Chapters?)\s*·\s*(\d+)\s+(?:bài học|Lessons?)\*\*",
    re.IGNORECASE,
)

FORBIDDEN_ACTIVE_CLAIMS = (
    "SYLLABUS-v2026.09.md`** là active canonical",
    "v2026.09 active canonical",
    "Active curriculum vẫn giữ **23 Part / 89 Chapter / 671 lesson",
    "NORMALIZED ACTIVE LESSON INVENTORY:\nROADMAP.md + roadmap/part-00..22.md",
)


def active_counts() -> tuple[int, int, int] | None:
    text = ACTIVE.read_text(encoding="utf-8")
    match = COUNT_RE.search(text)
    return tuple(map(int, match.groups())) if match else None


def validate() -> list[str]:
    problems: list[str] = []
    if not ACTIVE.exists():
        return ["AUTH001 CURRICULUM.md: active canonical is missing"]
    if not SOURCES_README.exists():
        return ["AUTH002 sources/README.md: source guide is missing"]

    guide = SOURCES_README.read_text(encoding="utf-8")
    if "CURRICULUM.md" not in guide or "active canonical" not in guide.lower():
        problems.append("AUTH003 sources/README.md: must point to CURRICULUM.md as active canonical authority")

    for phrase in FORBIDDEN_ACTIVE_CLAIMS:
        if phrase in guide:
            problems.append(f"AUTH004 sources/README.md: stale active-authority claim remains: {phrase!r}")

    counts = active_counts()
    if counts is None:
        problems.append("AUTH005 CURRICULUM.md: cannot parse active Part/Chapter/Lesson totals")

    return problems


def main() -> int:
    problems = validate()
    if problems:
        print("Authority validation failed:")
        for problem in problems:
            print(f"- {problem}")
        return 1
    print("Authority validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
