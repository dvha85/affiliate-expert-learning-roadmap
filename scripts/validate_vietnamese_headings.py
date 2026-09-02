#!/usr/bin/env python3
"""Guard Vietnamese-first navigation for learner-facing roadmap Part titles."""
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

PART_H1_RE = re.compile(r"^# Phần (\d+) — (.+)$", re.M)
ASCII_WORD_RE = re.compile(r"[A-Za-z]{2,}")


@dataclass(frozen=True)
class Problem:
    code: str
    path: str
    message: str

    def __str__(self) -> str:
        return f"{self.code} {self.path}: {self.message}"


def is_english_all_caps_subtitle(text: str) -> bool:
    words = ASCII_WORD_RE.findall(text)
    if len(words) < 2:
        return False
    letters = "".join(words)
    return letters.isupper()


def validate(root: Path) -> list[Problem]:
    root = root.resolve()
    problems: list[Problem] = []
    folder = root / "roadmap"
    if not folder.exists():
        problems.append(Problem("VHEAD001", "roadmap/", "thiếu roadmap directory"))
        return problems

    for path in sorted(folder.glob("part-*.md")):
        rel = path.relative_to(root)
        text = path.read_text(encoding="utf-8")
        match = PART_H1_RE.search(text)
        if not match:
            problems.append(Problem("VHEAD002", str(rel), "thiếu H1 '# Phần N — ...'"))
            continue
        subtitle = match.group(2).strip()
        if is_english_all_caps_subtitle(subtitle):
            problems.append(
                Problem(
                    "VHEAD003",
                    str(rel),
                    f"Part subtitle English-first toàn chữ hoa: {subtitle!r}; phải Việt-first",
                )
            )
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description="Kiểm tra Part heading Việt-first")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    problems = validate(args.root)
    if problems:
        print(f"VIETNAMESE HEADING CI: FAIL ({len(problems)} problem(s))")
        for problem in problems:
            print(f"- {problem}")
        return 1
    print("VIETNAMESE HEADING CI: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
