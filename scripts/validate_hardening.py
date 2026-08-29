#!/usr/bin/env python3
"""Validate goal-first curriculum hardening invariants.

This validator deliberately derives inventory size from the active roadmap. It
protects the root authority model, source registries, unique active IDs, and
stale-authority boundaries without freezing a particular curriculum size.
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

LESSON_RE = re.compile(r"^- \[[ xX]\] \*\*(\d+\.\d+)\*\* — ")
CHAPTER_RE = re.compile(r"^### Chương (\d+) — ")
EXT_RE = re.compile(r"\bEXT:[A-Z0-9][A-Z0-9:_-]*\b")

CANONICAL_PATH = Path("CURRICULUM.md")
CANONICAL_MARKERS = (
    "Mission-first",
    "Real Evidence Ladder",
    "Core / Advanced / Reference",
)

REGISTER_PATHS = (
    Path("docs/AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md"),
    Path("docs/BOT-ENGINEERING-REFRESH-2026.08.md"),
)

# These active entry points must all lead maintainers and learners back to the
# same root authority. Historical material under sources/ is intentionally not
# part of this contract.
AUTHORITY_DOCS = {
    Path("README.md"): ("CURRICULUM.md",),
    Path("ROADMAP.md"): ("CURRICULUM.md",),
    Path("BUILD-FIRST.md"): ("CURRICULUM.md",),
    Path("CONTRIBUTING.md"): ("CURRICULUM.md",),
    Path("docs/FRESHNESS-POLICY.md"): (
        "CURRICULUM.md",
        "AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md",
        "BOT-ENGINEERING-REFRESH-2026.08.md",
    ),
    Path("docs/EXECUTION-MODEL.md"): (
        "Governed Action / Approval",
        "RISK 0",
        "RISK 1",
        "RISK 2",
    ),
}

# These documents describe superseded decisions and may truthfully retain the
# old inventory numbers. Additions to this tuple require an explicit review.
HISTORICAL_DOC_ALLOWLIST = {
    Path("docs/ADR-001-GO-FIRST-BOT-STACK.md"),
    Path("docs/ADR-002-OUTCOME-DRIVEN-CURRICULUM.md"),
    Path("docs/EFFORT-RECALIBRATION-v2026.09.md"),
}

HISTORICAL_CONTEXT_RE = re.compile(
    r"\b(?:historical|legacy|previous|old|supersed(?:e|ed|es|ing)|cũ|trước|thay thế|lịch sử)\b",
    re.IGNORECASE,
)

STALE_ACTIVE_PATTERNS = (
    (
        "legacy fixed Part count",
        re.compile(
            r"(?:\b23(?:\*\*)?\s+(?:Parts?|Part|phần)\b|\b(?:Parts?|Part|phần)\s*:\s*(?:\*\*)?23\b)",
            re.IGNORECASE,
        ),
    ),
    (
        "legacy fixed Chapter count",
        re.compile(
            r"(?:\b89(?:\*\*)?\s+(?:Chapters?|Chapter|chương)\b|\b(?:Chapters?|Chapter|chương)\s*:\s*(?:\*\*)?89\b)",
            re.IGNORECASE,
        ),
    ),
    (
        "legacy fixed Lesson count",
        re.compile(
            r"(?:\b671(?:\*\*)?\s+(?:Lessons?|Lesson|bài học)\b|\b(?:Lessons?|Lesson|bài học)\s*:\s*(?:\*\*)?671\b)",
            re.IGNORECASE,
        ),
    ),
    (
        "legacy fixed Project count",
        re.compile(
            r"(?:\b14(?:\*\*)?\s+(?:main\s+)?Projects?\b|\b(?:Main\s+)?Projects?\s*:\s*(?:\*\*)?14\b)",
            re.IGNORECASE,
        ),
    ),
    (
        "legacy compact inventory invariant",
        re.compile(r"\b23\s*/\s*89\s*/\s*671(?:\s*/\s*14)?\b"),
    ),
    (
        "superseded syllabus declared active",
        re.compile(r"active canonical[^\n]{0,100}SYLLABUS-v2026\.09", re.IGNORECASE),
    ),
    (
        "superseded syllabus declared active",
        re.compile(r"SYLLABUS-v2026\.09[^\n]{0,100}active canonical", re.IGNORECASE),
    ),
)

AFFILIATE_REGISTER_LEGACY_MAP_RE = re.compile(
    r"(?:\bP(?:0?[7-9]|1[0-9]|2[0-2])(?:/C\d+)?\b|\bCh(?:2[1-9]|[3-9]\d)\b|change\s+671\s+count)",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class Problem:
    code: str
    path: str
    message: str

    def __str__(self) -> str:
        return f"{self.code} {self.path}: {self.message}"


def collect_registry_ids(root: Path, problems: list[Problem]) -> set[str]:
    ids: set[str] = set()
    for rel in REGISTER_PATHS:
        path = root / rel
        if not path.exists():
            problems.append(Problem("AUTH002", str(rel), "external source register is missing"))
            continue
        text = path.read_text(encoding="utf-8")
        ids.update(EXT_RE.findall(text))
    return ids


def check_active_register_mapping(root: Path, problems: list[Problem]) -> None:
    rel = Path("docs/AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md")
    path = root / rel
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    if "CURRICULUM.md" not in text:
        problems.append(Problem("AUTH004", str(rel), "current affiliate register phải link active CURRICULUM"))
    match = AFFILIATE_REGISTER_LEGACY_MAP_RE.search(text)
    if match:
        problems.append(Problem("STALE002", str(rel), f"current affiliate register còn legacy curriculum mapping: {match.group(0)}"))


def check_external_refs(root: Path, registry_ids: set[str], problems: list[Problem]) -> None:
    lessons = root / "lessons"
    if not lessons.exists():
        return
    for path in lessons.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for ref in sorted(set(EXT_RE.findall(text))):
            if ref not in registry_ids:
                problems.append(
                    Problem(
                        "FRESH004",
                        str(path.relative_to(root)),
                        f"external source ref does not resolve in current registers: {ref}",
                    )
                )


def _duplicates(values: list[int] | list[str]) -> list[int] | list[str]:
    return sorted(value for value, count in Counter(values).items() if count > 1)


def collect_roadmap_inventory(root: Path, problems: list[Problem]) -> set[str]:
    part_files = sorted((root / "roadmap").glob("part-*.md"))
    if not part_files:
        problems.append(Problem("PROV002", "roadmap/", "active roadmap has no Part files"))
        return set()

    lesson_ids: list[str] = []
    chapter_ids: list[int] = []
    for path in part_files:
        for raw in path.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            lesson_match = LESSON_RE.match(line)
            if lesson_match:
                lesson_ids.append(lesson_match.group(1))
            chapter_match = CHAPTER_RE.match(line)
            if chapter_match:
                chapter_ids.append(int(chapter_match.group(1)))

    duplicate_lessons = _duplicates(lesson_ids)
    if duplicate_lessons:
        problems.append(
            Problem(
                "PROV003",
                "roadmap/",
                f"active lesson IDs must be unique; duplicates={duplicate_lessons}",
            )
        )

    duplicate_chapters = _duplicates(chapter_ids)
    if duplicate_chapters:
        problems.append(
            Problem(
                "PROV004",
                "roadmap/",
                f"active chapter IDs must be unique; duplicates={duplicate_chapters}",
            )
        )

    return set(lesson_ids)


def check_canonical_model(root: Path, problems: list[Problem]) -> None:
    path = root / CANONICAL_PATH
    if not path.exists():
        problems.append(Problem("AUTH001", str(CANONICAL_PATH), "root active canonical is missing"))
        return
    text = path.read_text(encoding="utf-8")
    for marker in CANONICAL_MARKERS:
        if marker not in text:
            problems.append(Problem("AUTH003", str(CANONICAL_PATH), f"missing curriculum model marker: {marker}"))


def check_authority_docs(root: Path, problems: list[Problem]) -> None:
    for rel, markers in AUTHORITY_DOCS.items():
        path = root / rel
        if not path.exists():
            problems.append(Problem("AUTH001", str(rel), "active authority document is missing"))
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                problems.append(Problem("AUTH001", str(rel), f"missing authority-consistency marker: {marker}"))


def active_markdown_files(root: Path) -> list[Path]:
    paths: set[Path] = set(root.glob("*.md"))
    for directory in ("docs", "roadmap", "lessons", "missions", "templates", "artifacts"):
        base = root / directory
        if base.exists():
            paths.update(base.rglob("*.md"))
    return sorted(paths)


def check_stale_active_references(root: Path, problems: list[Problem]) -> None:
    for path in active_markdown_files(root):
        rel = path.relative_to(root)
        if rel in HISTORICAL_DOC_ALLOWLIST:
            continue
        text = path.read_text(encoding="utf-8")
        stale_description: str | None = None
        for line in text.splitlines():
            for description, pattern in STALE_ACTIVE_PATTERNS:
                if not pattern.search(line):
                    continue
                is_old_count = description.startswith("legacy")
                if is_old_count and HISTORICAL_CONTEXT_RE.search(line):
                    continue
                stale_description = description
                break
            if stale_description:
                break
        if stale_description:
            problems.append(Problem("STALE001", str(rel), stale_description))


def validate(root: Path) -> list[Problem]:
    problems: list[Problem] = []
    registry_ids = collect_registry_ids(root, problems)
    check_active_register_mapping(root, problems)
    check_external_refs(root, registry_ids, problems)
    collect_roadmap_inventory(root, problems)
    check_canonical_model(root, problems)
    check_authority_docs(root, problems)
    check_stale_active_references(root, problems)
    return problems


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    problems = validate(root)
    if problems:
        for problem in problems:
            print(problem)
        print(f"Hardening validation failed with {len(problems)} problem(s).")
        return 1
    print("Hardening validation passed: active authority, unique inventory, and external refs are consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
