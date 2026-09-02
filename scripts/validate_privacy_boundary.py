#!/usr/bin/env python3
"""Check repository-level privacy boundaries for learner evidence.

This intentionally catches only deterministic mistakes: missing local-ignore
paths, missing templates/docs, and obvious plaintext credential assignments in
committed Markdown. Human review remains required for redaction quality.
"""
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

REQUIRED_FILES = (
    Path("docs/PRIVACY-AND-LEARNER-EVIDENCE.md"),
    Path("templates/DATA-ACCESS-CONTEXT.md"),
    Path("templates/REDACTED-EVIDENCE-SUMMARY.md"),
)
GITIGNORE_MARKERS = (
    ".env",
    "artifacts/local/",
    "artifacts/private/",
    "artifacts/missions/*/private/",
    "artifacts/missions/*/raw/",
)
SUSPICIOUS_ASSIGNMENT = re.compile(
    r"(?im)^\s*(?:api[_-]?key|secret|password|authorization|access[_-]?token)\s*:\s*(?!$|<redacted>|\[redacted\]|REDACTED|\$\{)[^\s]+"
)


@dataclass(frozen=True)
class Problem:
    code: str
    path: str
    message: str

    def __str__(self) -> str:
        return f"{self.code} {self.path}: {self.message}"


def validate(root: Path) -> list[Problem]:
    root = root.resolve()
    problems: list[Problem] = []
    for rel in REQUIRED_FILES:
        if not (root / rel).is_file():
            problems.append(Problem("PRIV001", str(rel), "thiếu privacy/evidence resource bắt buộc"))
    ignore = root / ".gitignore"
    text = ignore.read_text(encoding="utf-8") if ignore.exists() else ""
    for marker in GITIGNORE_MARKERS:
        if marker not in text:
            problems.append(Problem("PRIV002", ".gitignore", f"thiếu local-ignore marker {marker!r}"))
    artifacts = root / "artifacts"
    if artifacts.exists():
        for path in artifacts.rglob("*.md"):
            if path.name in {"REDACTED-EVIDENCE-SUMMARY.md"}:
                continue
            if SUSPICIOUS_ASSIGNMENT.search(path.read_text(encoding="utf-8")):
                problems.append(Problem("PRIV003", str(path.relative_to(root)), "có vẻ chứa credential/plaintext secret"))
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description="Kiểm privacy boundary của learner evidence")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    problems = validate(args.root)
    if problems:
        print(f"PRIVACY BOUNDARY: FAIL ({len(problems)} problem(s))")
        for problem in problems:
            print(f"- {problem}")
        return 1
    print("PRIVACY BOUNDARY: PASS")
    return 0
