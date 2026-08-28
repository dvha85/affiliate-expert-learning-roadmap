#!/usr/bin/env python3
"""Validate post-Go curriculum hardening invariants.

No third-party dependencies. This validator complements validate_curriculum.py
with provenance, external-source registry, project-inventory and authority-doc
checks introduced by Issue #25.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

LESSON_RE = re.compile(r"^- \[[ xX]\] \*\*(\d+\.\d+)\*\* — ")
CHAPTER_RE = re.compile(r"^### Chương (\d+) — ")
EXT_RE = re.compile(r"\bEXT:[A-Z0-9][A-Z0-9:_-]*\b")
PROJECT_RE = re.compile(r"^- \[[ xX]\] \*\*PROJECT\s+(\d+)\s+—")

EXPECTED_PROJECT_PART = {
    1: 1,
    2: 3,
    3: 6,
    4: 8,
    5: 9,
    6: 11,
    7: 12,
    8: 13,
    9: 14,
    10: 15,
    11: 16,
    12: 17,
    13: 19,
    14: 21,
}

REGISTER_PATHS = (
    Path("docs/AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md"),
    Path("docs/BOT-ENGINEERING-REFRESH-2026.08.md"),
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


def collect_roadmap_inventory(root: Path, problems: list[Problem]):
    part_files = sorted((root / "roadmap").glob("part-*.md"))
    if len(part_files) != 23:
        problems.append(Problem("PROV002", "roadmap/", f"expected 23 Part files, found {len(part_files)}"))

    lesson_ids: list[str] = []
    chapter_ids: list[int] = []
    project_locations: dict[int, list[int]] = {}

    for path in part_files:
        try:
            part = int(path.stem.split("-", 1)[1])
        except (IndexError, ValueError):
            continue
        for raw in path.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            lm = LESSON_RE.match(line)
            if lm:
                lesson_ids.append(lm.group(1))
            cm = CHAPTER_RE.match(line)
            if cm:
                chapter_ids.append(int(cm.group(1)))
            pm = PROJECT_RE.match(line)
            if pm:
                project_locations.setdefault(int(pm.group(1)), []).append(part)

    unique_lessons = set(lesson_ids)
    if len(lesson_ids) != 671 or len(unique_lessons) != 671:
        problems.append(
            Problem(
                "PROV003",
                "roadmap/",
                f"normalized lesson inventory must contain exactly 671 unique IDs; found {len(lesson_ids)} rows / {len(unique_lessons)} unique",
            )
        )

    if len(chapter_ids) != 89 or len(set(chapter_ids)) != 89:
        problems.append(
            Problem(
                "PROV004",
                "roadmap/",
                f"normalized chapter inventory must contain exactly 89 unique chapters; found {len(chapter_ids)} rows / {len(set(chapter_ids))} unique",
            )
        )

    return unique_lessons, project_locations


def check_provenance_index(root: Path, lessons: set[str], problems: list[Problem]) -> None:
    rel = Path("sources/CURRICULUM-INDEX-v2026.09.md")
    path = root / rel
    if not path.exists():
        problems.append(Problem("PROV001", str(rel), "normalized canonical provenance index is missing"))
        return
    text = path.read_text(encoding="utf-8")
    markers = (
        "source_explicit",
        "normalized_from_chapter",
        "normalized_then_overridden",
        "S:P{part}/C{chapter}/L{lesson}",
        "Lessons: 671",
    )
    for marker in markers:
        if marker not in text:
            problems.append(Problem("PROV005", str(rel), f"missing provenance marker: {marker}"))
    if len(lessons) == 671 and "validated roadmap inventory" not in text:
        problems.append(Problem("PROV006", str(rel), "index must state that the 671 lessons resolve from the validated roadmap inventory"))


def check_projects(project_locations: dict[int, list[int]], problems: list[Problem]) -> None:
    found_ids = set(project_locations)
    expected_ids = set(EXPECTED_PROJECT_PART)
    missing = sorted(expected_ids - found_ids)
    extra = sorted(found_ids - expected_ids)
    if missing or extra:
        problems.append(Problem("PROJECT001", "roadmap/", f"main project inventory mismatch; missing={missing}, extra={extra}"))

    for project, expected_part in EXPECTED_PROJECT_PART.items():
        locations = project_locations.get(project, [])
        if len(locations) != 1:
            problems.append(Problem("PROJECT001", "roadmap/", f"PROJECT {project} must appear exactly once; found in Parts {locations}"))
            continue
        if locations[0] != expected_part:
            problems.append(
                Problem(
                    "PROJECT002",
                    f"roadmap/part-{locations[0]:02d}.md",
                    f"PROJECT {project} must be in Part {expected_part}, found in Part {locations[0]}",
                )
            )


def check_authority_docs(root: Path, problems: list[Problem]) -> None:
    checks = {
        Path("sources/README.md"): (
            "SYLLABUS-v2026.09.md",
            "CURRICULUM-INDEX-v2026.09.md",
            "normalized_from_chapter",
            "BOT-ENGINEERING-REFRESH-2026.08.md",
        ),
        Path("docs/FRESHNESS-POLICY.md"): (
            "SYLLABUS-v2026.09",
            "CURRICULUM-INDEX-v2026.09.md",
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
    for rel, markers in checks.items():
        path = root / rel
        if not path.exists():
            problems.append(Problem("AUTH001", str(rel), "authority document is missing"))
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                problems.append(Problem("AUTH001", str(rel), f"missing authority-consistency marker: {marker}"))


def validate(root: Path) -> list[Problem]:
    problems: list[Problem] = []
    registry_ids = collect_registry_ids(root, problems)
    check_external_refs(root, registry_ids, problems)
    lessons, project_locations = collect_roadmap_inventory(root, problems)
    check_provenance_index(root, lessons, problems)
    check_projects(project_locations, problems)
    check_authority_docs(root, problems)
    return problems


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    problems = validate(root)
    if problems:
        for problem in problems:
            print(problem)
        print(f"Hardening validation failed with {len(problems)} problem(s).")
        return 1
    print("Hardening validation passed: 671 lessons, 14 projects, external refs resolved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
