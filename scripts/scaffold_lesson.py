#!/usr/bin/env python3
"""Safely scaffold lesson files from roadmap metadata.

Key guarantees:
- reads lesson IDs/titles from roadmap/part-XX.md;
- uses templates/LESSON.md as the source template;
- writes status=planned only;
- creates active CUR:P/C/L curriculum ref;
- best-effort chapter-level T/R refs from docs/SOURCE-MAPPING.md;
- never overwrites an existing lesson file;
- supports lesson, chapter, and part targets;
- supports --dry-run and --validate.
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = ROOT / "templates" / "LESSON.md"
SOURCE_MAP_PATH = ROOT / "docs" / "SOURCE-MAPPING.md"

LESSON_RE = re.compile(r"^- \[[ xX]\] \*\*(\d+\.\d+)\*\* — (?:\[[^\]]+\]\([^\)]+\)|(.+))$")
LINKED_LESSON_RE = re.compile(r"^- \[[ xX]\] \*\*(\d+\.\d+)\*\* — \[([^\]]+)\]\([^\)]+\)$")
CHAPTER_RE = re.compile(r"^### Chương (\d+) — (.+)$")
PART_TITLE_RE = re.compile(r"^# Phần (\d+) — (.+)$")
MAP_PART_RE = re.compile(r"^### Part (\d+) — (.+)$")
MAP_ROW_RE = re.compile(r"^\|\s*(\d+)\s+—\s+([^|]+)\|\s*`S:P(\d+)/C(\d+)`\s*\|\s*([^|]+)\|\s*([^|]+)\|")


@dataclass(frozen=True)
class Lesson:
    lesson_id: str
    title: str
    part: int
    chapter: int
    part_title: str
    chapter_title: str


@dataclass(frozen=True)
class SourceHints:
    training: list[str]
    research: list[str]


def slugify(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    ascii_text = ascii_text.lower()
    ascii_text = re.sub(r"[^a-z0-9]+", "-", ascii_text).strip("-")
    return ascii_text or "lesson"


def parse_part_file(part: int) -> list[Lesson]:
    path = ROOT / "roadmap" / f"part-{part:02d}.md"
    if not path.exists():
        raise ValueError(f"Roadmap part not found: {path.relative_to(ROOT)}")

    part_title = ""
    chapter = None
    chapter_title = ""
    lessons: list[Lesson] = []

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        m = PART_TITLE_RE.match(line)
        if m:
            part_title = m.group(2).strip()
            continue
        m = CHAPTER_RE.match(line)
        if m:
            chapter = int(m.group(1))
            chapter_title = m.group(2).strip()
            continue
        m = LINKED_LESSON_RE.match(line)
        if m and chapter is not None:
            lessons.append(Lesson(m.group(1), m.group(2).strip(), part, chapter, part_title, chapter_title))
            continue
        m = LESSON_RE.match(line)
        if m and chapter is not None:
            title = (m.group(2) or "").strip()
            if title:
                lessons.append(Lesson(m.group(1), title, part, chapter, part_title, chapter_title))

    if not lessons:
        raise ValueError(f"No lessons parsed from {path.relative_to(ROOT)}")
    return lessons


def all_lessons() -> list[Lesson]:
    out: list[Lesson] = []
    for path in sorted((ROOT / "roadmap").glob("part-*.md")):
        part = int(path.stem.split("-")[1])
        out.extend(parse_part_file(part))
    return out


def parse_source_hints() -> dict[tuple[int, int], SourceHints]:
    hints: dict[tuple[int, int], SourceHints] = {}
    if not SOURCE_MAP_PATH.exists():
        return hints
    current_part = None
    for raw in SOURCE_MAP_PATH.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        m = MAP_PART_RE.match(line)
        if m:
            current_part = int(m.group(1))
            continue
        m = MAP_ROW_RE.match(line)
        if not m or current_part is None:
            continue
        chapter = int(m.group(1))
        part_in_ref = int(m.group(3))
        chapter_in_ref = int(m.group(4))
        if part_in_ref != current_part or chapter_in_ref != chapter:
            continue
        training_cell = m.group(5).strip()
        research_cell = m.group(6).strip()
        hints[(current_part, chapter)] = SourceHints(
            training=[] if training_cell.startswith("—") else [training_cell],
            research=[] if research_cell.startswith("—") else [research_cell],
        )
    return hints


def yaml_list(values: list[str], indent: int = 4) -> str:
    if not values:
        return "[]"
    prefix = " " * indent
    return "\n" + "\n".join(f'{prefix}- "{v.replace(chr(34), chr(39))}"' for v in values)


def lesson_path(lesson: Lesson) -> Path:
    return ROOT / "lessons" / f"part-{lesson.part:02d}" / f"chapter-{lesson.chapter:02d}" / f"{lesson.lesson_id}-{slugify(lesson.title)}.md"


def existing_lesson_paths(lesson: Lesson) -> list[Path]:
    """Find authored files by stable lesson ID; slugs may improve over time."""
    directory = ROOT / "lessons" / f"part-{lesson.part:02d}" / f"chapter-{lesson.chapter:02d}"
    return sorted(directory.glob(f"{lesson.lesson_id}-*.md")) if directory.exists() else []


def render(
    lesson: Lesson,
    hints: SourceHints,
    effort: str,
    minutes: int,
    prerequisites: list[str],
    mission_refs: list[str],
) -> str:
    text = TEMPLATE_PATH.read_text(encoding="utf-8")
    active_ref = f"CUR:P{lesson.part}/C{lesson.chapter}/L{lesson.lesson_id}"

    # Replace YAML front matter wholesale to avoid fragile placeholder substitution.
    body = text.split("---", 2)[2].lstrip("\n")
    front = [
        "---",
        f'lesson_id: "{lesson.lesson_id}"',
        f'title: "{lesson.title.replace(chr(34), chr(39))}"',
        f"part: {lesson.part}",
        f"chapter: {lesson.chapter}",
        "track: core",
        "mission_refs: [" + ", ".join(f'\"{m}\"' for m in mission_refs) + "]",
        "practice_first: true",
        f"effort: {effort}",
        f"estimated_minutes: {minutes}",
        "status: planned",
    ]
    if prerequisites:
        front.append("prerequisites:")
        front.extend(f'  - "{p}"' for p in prerequisites)
    else:
        front.append("prerequisites: []")
    front += [
        "source_refs:",
        "  active:",
        f'    - "{active_ref}"',
        "  historical: []",
        "  training:" + (yaml_list(hints.training, 4) if hints.training else " []"),
        "  research:" + (yaml_list(hints.research, 4) if hints.research else " []"),
        "  external: []",
        "last_verified: null",
        "---",
        "",
    ]

    replacements = {
        "# Bài X.Y — Tên micro-lesson": f"# Bài {lesson.lesson_id} — {lesson.title}",
        "**Track:** `core` · **Mission:** `MXX` · **Thời lượng dự kiến:** 30 phút":
            f"**Track:** `core` · **Mission:** `{', '.join(mission_refs) or 'chưa map'}` · **Thời lượng dự kiến:** {minutes} phút",
        "CUR:PX/CY/LX.Y": active_ref,
        "artifacts/part-XX/<lesson-id>-<artifact-slug>.md": f"artifacts/part-{lesson.part:02d}/{lesson.lesson_id}-<artifact-slug>.md",
        "Tiêu chí PASS bài X.Y": f"Tiêu chí PASS bài {lesson.lesson_id}",
        "PASS X.Y": f"PASS {lesson.lesson_id}",
        "RETRY X.Y": f"RETRY {lesson.lesson_id}",
    }
    for old, new in replacements.items():
        body = body.replace(old, new)
    return "\n".join(front) + body


def select_lessons(args: argparse.Namespace) -> list[Lesson]:
    lessons = all_lessons()
    if args.lesson:
        selected = [x for x in lessons if x.lesson_id == args.lesson]
    elif args.chapter is not None:
        selected = [x for x in lessons if x.chapter == args.chapter]
    else:
        selected = [x for x in lessons if x.part == args.part]
    if not selected:
        raise ValueError("No matching lesson(s) found in roadmap")
    return selected


def validate_selection(selected: Iterable[Lesson]) -> int:
    errors = 0
    for lesson in selected:
        existing = existing_lesson_paths(lesson)
        path = existing[0] if existing else lesson_path(lesson)
        if existing:
            content = path.read_text(encoding="utf-8")
            required = [
                f'lesson_id: "{lesson.lesson_id}"',
                "status:",
                "effort:",
                "track:",
                "mission_refs:",
                "practice_first: true",
                "prerequisites:",
                "source_refs:",
                f"CUR:P{lesson.part}/C{lesson.chapter}/L{lesson.lesson_id}",
            ]
            missing = [x for x in required if x not in content]
            if missing:
                errors += 1
                print(f"INVALID {path.relative_to(ROOT)} missing={missing}")
            else:
                print(f"OK      {path.relative_to(ROOT)}")
        else:
            print(f"PLANNED {path.relative_to(ROOT)} (file not created)")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Safely scaffold curriculum lessons")
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--lesson", help="Lesson ID, e.g. 0.2")
    target.add_argument("--chapter", type=int, help="Chapter number, e.g. 38")
    target.add_argument("--part", type=int, help="Part number, e.g. 12")
    parser.add_argument("--effort", choices=["S", "M", "L"], default="S")
    parser.add_argument("--minutes", type=int, default=30)
    parser.add_argument("--prerequisite", action="append", default=[], help="Repeatable prerequisite value")
    parser.add_argument("--mission", action="append", default=[], help="Repeatable Mission ID, e.g. M00")
    parser.add_argument("--dry-run", action="store_true", help="Print planned/existing files, write nothing")
    parser.add_argument("--validate", action="store_true", help="Validate matching existing files, write nothing")
    args = parser.parse_args()

    if not TEMPLATE_PATH.exists():
        print(f"ERROR missing template: {TEMPLATE_PATH}", file=sys.stderr)
        return 2
    if args.minutes <= 0:
        print("ERROR --minutes must be > 0", file=sys.stderr)
        return 2

    try:
        selected = select_lessons(args)
    except ValueError as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        return 2

    if args.validate:
        return 1 if validate_selection(selected) else 0

    hints_map = parse_source_hints()
    collisions = [path for lesson in selected for path in existing_lesson_paths(lesson)]
    if collisions and not args.dry_run:
        print("ERROR refusing to overwrite existing lesson file(s):", file=sys.stderr)
        for path in collisions:
            print(f"  - {path.relative_to(ROOT)}", file=sys.stderr)
        return 3

    for lesson in selected:
        existing = existing_lesson_paths(lesson)
        path = existing[0] if existing else lesson_path(lesson)
        if existing:
            print(f"EXISTS {lesson.lesson_id}: {path.relative_to(ROOT)} (dry-run; would not overwrite)")
            continue
        hints = hints_map.get((lesson.part, lesson.chapter), SourceHints([], []))
        print(f"PLAN {lesson.lesson_id}: {path.relative_to(ROOT)}")
        print(f"     source={lesson.part}/{lesson.chapter} effort={args.effort} status=planned")
        if args.dry_run:
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            render(lesson, hints, args.effort, args.minutes, args.prerequisite, args.mission),
            encoding="utf-8",
        )
        print(f"CREATED {path.relative_to(ROOT)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
