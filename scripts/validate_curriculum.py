#!/usr/bin/env python3
"""Validate curriculum structure, canonical source direction, freshness contract, and Markdown links.

No third-party dependencies. Intended for local use and GitHub Actions.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from urllib.parse import unquote

SUMMARY_RE = re.compile(r"Tổng cộng:\s*\*\*(\d+) phần · (\d+) chương · (\d+) bài học\*\*")
PART_LINK_RE = re.compile(r"\[Phần\s+(\d+)\]\(([^)]+)\)")
PART_TITLE_RE = re.compile(r"^# Phần (\d+) — (.+)$")
TIMELINE_RE = re.compile(r"^- Timeline: \*\*(.+)\*\*(?: — (.+))?\.?$")
CHAPTER_RE = re.compile(r"^### Chương (\d+) — (.+)$")
LESSON_RE = re.compile(r"^- \[[ xX]\] \*\*(\d+\.\d+)\*\* — (.+)$")
LESSON_LINK_RE = re.compile(r"^\[([^\]]+)\]\(([^)]+)\)$")
MD_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
FRONT_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
TOP_KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s*(.*))?$")
FILE_ID_RE = re.compile(r"^(\d+\.\d+)-")
PART_DIR_RE = re.compile(r"^part-(\d{2})$")
CHAPTER_DIR_RE = re.compile(r"^chapter-(\d{2})$")

ALLOWED_STATUS = {"planned", "draft", "ready"}
ALLOWED_EFFORT = {"S", "M", "L"}
REQUIRED_META = {
    "lesson_id", "title", "part", "chapter", "effort", "estimated_minutes",
    "status", "prerequisites", "source_refs", "last_verified",
}

ACTIVE_CANONICAL = "SYLLABUS-v2026.09.md"
HISTORICAL_BASELINE = "SYLLABUS-v2026.08.md"
LEGACY_PRIMARY_STACK_TOKENS = (
    "C#/.NET",
    "C# / .NET",
    "ASP.NET Core",
    "EF Core",
    "Hangfire",
    "Quartz",
)


@dataclass(frozen=True)
class Problem:
    code: str
    path: str
    message: str

    def __str__(self) -> str:
        return f"{self.code} {self.path}: {self.message}"


@dataclass(frozen=True)
class RoadmapLesson:
    lesson_id: str
    part: int
    chapter: int
    title: str
    linked_path: Path | None


@dataclass(frozen=True)
class PartExpectation:
    part: int
    path: Path
    chapters: tuple[int, ...]
    lesson_count: int


def strip_fenced_code(text: str) -> str:
    out: list[str] = []
    in_fence = False
    marker = ""
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            current = stripped[:3]
            if not in_fence:
                in_fence = True
                marker = current
            elif current == marker:
                in_fence = False
                marker = ""
            out.append("")
        elif in_fence:
            out.append("")
        else:
            out.append(line)
    return "\n".join(out)


def parse_chapter_spec(spec: str) -> tuple[int, ...]:
    spec = spec.strip().replace("–", "-").replace("—", "-")
    values: list[int] = []
    for token in (x.strip() for x in spec.split(",")):
        if not token:
            continue
        if "-" in token:
            a, b = token.split("-", 1)
            values.extend(range(int(a), int(b) + 1))
        else:
            values.append(int(token))
    return tuple(values)


def parse_roadmap(root: Path, problems: list[Problem]):
    path = root / "ROADMAP.md"
    if not path.exists():
        problems.append(Problem("ROADMAP001", "ROADMAP.md", "missing ROADMAP.md"))
        return None, {}
    text = path.read_text(encoding="utf-8")
    m = SUMMARY_RE.search(text)
    summary = tuple(map(int, m.groups())) if m else None
    if summary is None:
        problems.append(Problem("ROADMAP002", "ROADMAP.md", "missing canonical total summary"))

    expected: dict[int, PartExpectation] = {}
    for line in text.splitlines():
        if not line.startswith("|") or "[Phần " not in line:
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 5:
            continue
        pm = PART_LINK_RE.search(cells[0])
        if not pm:
            continue
        part = int(pm.group(1))
        rel = Path(pm.group(2).split("#", 1)[0])
        try:
            chapters = parse_chapter_spec(cells[2])
            lesson_count = int(cells[3])
        except ValueError:
            problems.append(Problem("ROADMAP003", "ROADMAP.md", f"invalid chapter/count cells for Part {part}"))
            continue
        if part in expected:
            problems.append(Problem("ROADMAP004", "ROADMAP.md", f"duplicate Part {part} row"))
        expected[part] = PartExpectation(part, rel, chapters, lesson_count)
    return summary, expected


def parse_part_file(root: Path, exp: PartExpectation, problems: list[Problem]):
    path = root / exp.path
    if not path.exists():
        problems.append(Problem("COUNT001", str(exp.path), "part file referenced by ROADMAP does not exist"))
        return [], set()

    part_title_seen = False
    timeline_seen = False
    current_chapter: int | None = None
    chapters: set[int] = set()
    lessons: list[RoadmapLesson] = []
    text = path.read_text(encoding="utf-8")
    for raw in text.splitlines():
        line = raw.strip()
        pm = PART_TITLE_RE.match(line)
        if pm:
            part_title_seen = True
            if int(pm.group(1)) != exp.part:
                problems.append(Problem("STRUCT001", str(exp.path), f"H1 says Part {pm.group(1)}, expected {exp.part}"))
            continue
        if TIMELINE_RE.match(line):
            timeline_seen = True
            continue
        cm = CHAPTER_RE.match(line)
        if cm:
            current_chapter = int(cm.group(1))
            if current_chapter in chapters:
                problems.append(Problem("ID003", str(exp.path), f"duplicate Chapter {current_chapter} heading"))
            chapters.add(current_chapter)
            continue
        lm = LESSON_RE.match(line)
        if lm:
            if current_chapter is None:
                problems.append(Problem("STRUCT002", str(exp.path), f"lesson {lm.group(1)} appears before a chapter heading"))
                continue
            lesson_id = lm.group(1)
            rest = lm.group(2).strip()
            title = rest
            linked: Path | None = None
            linkm = LESSON_LINK_RE.match(rest)
            if linkm:
                title = linkm.group(1).strip()
                linked = ((root / exp.path).parent / linkm.group(2).split("#", 1)[0]).resolve().relative_to(root.resolve())
            prefix = int(lesson_id.split(".", 1)[0])
            if prefix != current_chapter:
                problems.append(Problem("ID004", str(exp.path), f"lesson {lesson_id} is under Chapter {current_chapter}"))
            lessons.append(RoadmapLesson(lesson_id, exp.part, current_chapter, title, linked))

    if not part_title_seen:
        problems.append(Problem("STRUCT003", str(exp.path), "missing Part H1"))
    if not timeline_seen:
        problems.append(Problem("TIME001", str(exp.path), "missing normalized '- Timeline:' metadata line"))
    if "- Lịch đề xuất:" in text:
        problems.append(Problem("TIME002", str(exp.path), "legacy '- Lịch đề xuất:' timeline remains"))
    return lessons, chapters


def parse_front_matter(text: str):
    m = FRONT_RE.match(text)
    if not m:
        return None
    raw = m.group(1)
    values: dict[str, str] = {}
    for line in raw.splitlines():
        if not line or line[0].isspace():
            continue
        km = TOP_KEY_RE.match(line)
        if km:
            values[km.group(1)] = (km.group(2) or "").strip().strip('"\'')
    return values, raw


def nested_external_refs(raw_front: str) -> list[str]:
    refs: list[str] = []
    in_source_refs = False
    in_external = False
    for raw in raw_front.splitlines():
        if raw == "source_refs:":
            in_source_refs = True
            in_external = False
            continue
        if in_source_refs and raw and not raw.startswith(" "):
            break
        if not in_source_refs:
            continue
        m = re.match(r"^  external:\s*(.*)$", raw)
        if m:
            inline = m.group(1).strip()
            in_external = inline != "[]"
            if inline and inline != "[]":
                if inline.startswith("[") and inline.endswith("]"):
                    body = inline[1:-1].strip()
                    if body:
                        refs.extend(x.strip().strip('"\'') for x in body.split(",") if x.strip())
            continue
        if in_external:
            item = re.match(r"^    -\s*[\"']?(.*?)[\"']?\s*$", raw)
            if item:
                refs.append(item.group(1).strip())
                continue
            if re.match(r"^  [A-Za-z_][A-Za-z0-9_-]*:", raw):
                in_external = False
    return [x for x in refs if x]


def check_freshness_contract(rel: Path, meta: dict[str, str], raw_front: str, problems: list[Problem]) -> None:
    refs = nested_external_refs(raw_front)
    verified = (meta.get("last_verified") or "").strip()
    has_date = verified not in {"", "null", "None", "~"}

    if refs and not has_date:
        problems.append(Problem("FRESH001", str(rel), "external source_refs require last_verified date"))
    if has_date and not refs:
        problems.append(Problem("FRESH002", str(rel), "last_verified date requires at least one external source ref"))
    if has_date:
        try:
            date.fromisoformat(verified)
        except ValueError:
            problems.append(Problem("FRESH003", str(rel), "last_verified must use YYYY-MM-DD"))


def check_active_canonical(root: Path, problems: list[Problem]) -> None:
    active = root / "sources" / ACTIVE_CANONICAL
    historical = root / "sources" / HISTORICAL_BASELINE
    index = root / "sources" / "README.md"

    if not active.exists():
        problems.append(Problem("CANON001", f"sources/{ACTIVE_CANONICAL}", "active canonical manifest is missing"))
        return
    if not historical.exists():
        problems.append(Problem("CANON002", f"sources/{HISTORICAL_BASELINE}", "historical structural baseline is missing"))
    if not index.exists():
        problems.append(Problem("CANON003", "sources/README.md", "source index is missing"))
    else:
        text = index.read_text(encoding="utf-8")
        if ACTIVE_CANONICAL not in text or "active canonical" not in text.lower():
            problems.append(Problem("CANON004", "sources/README.md", f"source index must declare {ACTIVE_CANONICAL} as active canonical"))

    active_text = active.read_text(encoding="utf-8")
    required_markers = (
        "PRIMARY IMPLEMENTATION LANGUAGE = Go",
        "Parts: 23",
        "Chapters: 89",
        "Lessons: 671",
        "Main projects: 14",
    )
    for marker in required_markers:
        if marker not in active_text:
            problems.append(Problem("CANON005", f"sources/{ACTIVE_CANONICAL}", f"missing canonical invariant/decision marker: {marker}"))


def check_primary_technology_direction(root: Path, problems: list[Problem]) -> None:
    part15 = root / "roadmap" / "part-15.md"
    if not part15.exists():
        return
    text = part15.read_text(encoding="utf-8")
    if "51.1** — Go runtime" not in text:
        problems.append(Problem("TECH001", "roadmap/part-15.md", "active Ch51 must begin with the Go-first primary stack"))
    for token in LEGACY_PRIMARY_STACK_TOKENS:
        if token in text:
            problems.append(Problem("TECH002", "roadmap/part-15.md", f"legacy primary-stack token reintroduced in active Part 15: {token}"))


def headings_without_code(text: str) -> list[int]:
    text = strip_fenced_code(text)
    result: list[int] = []
    for line in text.splitlines():
        m = re.match(r"^(#{1,6})\s+\S", line)
        if m:
            result.append(len(m.group(1)))
    return result


def check_heading_structure(rel: Path, text: str, problems: list[Problem]) -> None:
    levels = headings_without_code(text)
    if not levels:
        problems.append(Problem("HEAD001", str(rel), "lesson has no Markdown heading"))
        return
    if levels.count(1) != 1 or levels[0] != 1:
        problems.append(Problem("HEAD002", str(rel), "lesson must have exactly one H1 and it must be first"))
    prev = levels[0]
    for level in levels[1:]:
        if level > prev + 1:
            problems.append(Problem("HEAD003", str(rel), f"heading level jumps H{prev} -> H{level}"))
            break
        prev = level


def markdown_files_for_links(root: Path) -> list[Path]:
    paths: set[Path] = set(root.glob("*.md"))
    for directory in ["docs", "roadmap", "lessons", "templates", "artifacts", "sources"]:
        d = root / directory
        if d.exists():
            paths.update(d.rglob("*.md"))
    return sorted(paths)


def normalize_link_target(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith("<") and ">" in raw:
        return raw[1:raw.index(">")]
    if " " in raw and not raw.startswith(("http://", "https://")):
        raw = raw.split(" ", 1)[0]
    return raw


def check_relative_links(root: Path, problems: list[Problem]) -> None:
    for path in markdown_files_for_links(root):
        rel = path.relative_to(root)
        text = strip_fenced_code(path.read_text(encoding="utf-8"))
        for raw in MD_LINK_RE.findall(text):
            target = normalize_link_target(raw)
            if not target or target.startswith(("#", "http://", "https://", "mailto:", "tel:")):
                continue
            if "<" in target or ">" in target:
                continue
            target_no_anchor = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target_no_anchor:
                continue
            resolved = (path.parent / target_no_anchor).resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                problems.append(Problem("LINK002", str(rel), f"relative link escapes repository: {target}"))
                continue
            if not resolved.exists():
                problems.append(Problem("LINK001", str(rel), f"broken relative link: {target}"))


def validate(root: Path) -> list[Problem]:
    root = root.resolve()
    problems: list[Problem] = []

    check_active_canonical(root, problems)
    check_primary_technology_direction(root, problems)

    summary, expectations = parse_roadmap(root, problems)

    all_roadmap_lessons: list[RoadmapLesson] = []
    all_chapters: set[int] = set()
    actual_part_files = {int(p.stem.split("-")[1]): p for p in (root / "roadmap").glob("part-*.md")} if (root / "roadmap").exists() else {}

    for _, exp in sorted(expectations.items()):
        lessons, chapters = parse_part_file(root, exp, problems)
        all_roadmap_lessons.extend(lessons)
        all_chapters.update(chapters)
        if len(lessons) != exp.lesson_count:
            problems.append(Problem("COUNT002", str(exp.path), f"ROADMAP expects {exp.lesson_count} lessons, found {len(lessons)}"))
        if tuple(sorted(chapters)) != tuple(exp.chapters):
            problems.append(Problem("COUNT003", str(exp.path), f"ROADMAP chapters {exp.chapters}, found {tuple(sorted(chapters))}"))

    extra_parts = sorted(set(actual_part_files) - set(expectations))
    for part in extra_parts:
        problems.append(Problem("COUNT004", str(actual_part_files[part].relative_to(root)), f"Part {part} file is not indexed by ROADMAP"))

    ids: dict[str, list[RoadmapLesson]] = {}
    by_chapter: dict[int, list[int]] = {}
    for lesson in all_roadmap_lessons:
        ids.setdefault(lesson.lesson_id, []).append(lesson)
        by_chapter.setdefault(lesson.chapter, []).append(int(lesson.lesson_id.split(".", 1)[1]))
    for lesson_id, items in ids.items():
        if len(items) > 1:
            problems.append(Problem("ID001", "roadmap/", f"duplicate lesson ID {lesson_id} appears {len(items)} times"))
    for chapter, suffixes in sorted(by_chapter.items()):
        unique = sorted(set(suffixes))
        expected_seq = list(range(1, max(unique) + 1)) if unique else []
        if unique != expected_seq:
            missing = sorted(set(expected_seq) - set(unique))
            problems.append(Problem("ID002", "roadmap/", f"Chapter {chapter} lesson suffix gap; missing {missing}"))

    if summary:
        exp_parts, exp_chapters, exp_lessons = summary
        if len(expectations) != exp_parts:
            problems.append(Problem("COUNT005", "ROADMAP.md", f"summary says {exp_parts} parts, table has {len(expectations)}"))
        if len(all_chapters) != exp_chapters:
            problems.append(Problem("COUNT006", "ROADMAP.md", f"summary says {exp_chapters} chapters, part files have {len(all_chapters)}"))
        if len(all_roadmap_lessons) != exp_lessons:
            problems.append(Problem("COUNT007", "ROADMAP.md", f"summary says {exp_lessons} lessons, part files have {len(all_roadmap_lessons)}"))

    roadmap_by_id = {x.lesson_id: x for x in all_roadmap_lessons}
    linked_ids = {x.lesson_id for x in all_roadmap_lessons if x.linked_path is not None}
    for lesson in all_roadmap_lessons:
        if lesson.linked_path is not None and not (root / lesson.linked_path).exists():
            problems.append(Problem("LINK003", str(expectations[lesson.part].path), f"lesson {lesson.lesson_id} links to missing file {lesson.linked_path}"))

    lesson_files = sorted((root / "lessons").glob("part-*/chapter-*/*.md")) if (root / "lessons").exists() else []
    file_ids: dict[str, list[Path]] = {}
    for path in lesson_files:
        rel = path.relative_to(root)
        fm = FILE_ID_RE.match(path.name)
        if not fm:
            problems.append(Problem("META000", str(rel), "lesson filename must start with X.Y-"))
            continue
        file_id = fm.group(1)
        file_ids.setdefault(file_id, []).append(rel)
        if file_id not in roadmap_by_id:
            problems.append(Problem("META003", str(rel), f"lesson ID {file_id} not found in roadmap"))

        text = path.read_text(encoding="utf-8")
        parsed = parse_front_matter(text)
        if not parsed:
            problems.append(Problem("META001", str(rel), "missing YAML front matter"))
            check_heading_structure(rel, text, problems)
            continue
        meta, raw_front = parsed
        missing = sorted(REQUIRED_META - set(meta))
        if missing:
            problems.append(Problem("META002", str(rel), f"missing required metadata: {', '.join(missing)}"))

        if meta.get("lesson_id") and meta["lesson_id"] != file_id:
            problems.append(Problem("META004", str(rel), f"metadata lesson_id={meta['lesson_id']} does not match filename {file_id}"))
        try:
            part_dir = int(PART_DIR_RE.match(path.parent.parent.name).group(1))
            chapter_dir = int(CHAPTER_DIR_RE.match(path.parent.name).group(1))
        except (AttributeError, ValueError):
            problems.append(Problem("META005", str(rel), "invalid part/chapter directory naming"))
            part_dir = chapter_dir = -1
        if meta.get("part") and meta["part"] != str(part_dir):
            problems.append(Problem("META006", str(rel), f"metadata part={meta['part']} does not match directory {part_dir}"))
        if meta.get("chapter") and meta["chapter"] != str(chapter_dir):
            problems.append(Problem("META007", str(rel), f"metadata chapter={meta['chapter']} does not match directory {chapter_dir}"))
        if file_id in roadmap_by_id and roadmap_by_id[file_id].chapter != chapter_dir:
            problems.append(Problem("META008", str(rel), f"roadmap places {file_id} in Chapter {roadmap_by_id[file_id].chapter}, file is in Chapter {chapter_dir}"))

        status = meta.get("status")
        if status and status not in ALLOWED_STATUS:
            problems.append(Problem("META009", str(rel), f"invalid status {status!r}"))
        effort = meta.get("effort")
        if effort and effort not in ALLOWED_EFFORT:
            problems.append(Problem("META010", str(rel), f"invalid effort {effort!r}"))
        minutes = meta.get("estimated_minutes")
        if minutes:
            try:
                if int(minutes) <= 0:
                    raise ValueError
            except ValueError:
                problems.append(Problem("META011", str(rel), "estimated_minutes must be a positive integer"))
        canonical = f"S:P{part_dir}/C{chapter_dir}/L{file_id}"
        if "source_refs:" in raw_front and canonical not in raw_front:
            problems.append(Problem("META012", str(rel), f"canonical source ref missing: {canonical}"))

        check_freshness_contract(rel, meta, raw_front, problems)

        if status == "planned" and file_id in linked_ids:
            problems.append(Problem("STATE001", str(rel), "planned scaffold must remain unlinked from roadmap until draft/ready"))
        if status in {"draft", "ready"} and file_id not in linked_ids:
            problems.append(Problem("STATE002", str(rel), f"status={status} lesson must be linked from roadmap"))
        if status == "ready":
            m = FRONT_RE.match(text)
            body = text[m.end():] if m else text
            authored_body = strip_fenced_code(body)
            if re.search(r"(?m)^\s*\.\.\.\s*$|<artifact-slug>|Bài X\.Y|Tên bài", authored_body):
                problems.append(Problem("STATE003", str(rel), "ready lesson still contains scaffold placeholders outside fenced evidence examples"))

        check_heading_structure(rel, text, problems)

    for lesson_id, paths in file_ids.items():
        if len(paths) > 1:
            problems.append(Problem("ID005", "lessons/", f"duplicate lesson file ID {lesson_id}: {', '.join(map(str, paths))}"))

    check_relative_links(root, problems)
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate affiliate curriculum repository consistency")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="repository root")
    parser.add_argument("--quiet", action="store_true", help="print only failures")
    args = parser.parse_args()

    problems = validate(args.root)
    if problems:
        print(f"CURRICULUM CI: FAIL ({len(problems)} problem(s))")
        for problem in problems:
            print(problem)
        return 1
    if not args.quiet:
        print("CURRICULUM CI: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
