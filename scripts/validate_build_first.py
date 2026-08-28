#!/usr/bin/env python3
"""Validate Build-First Learning Architecture invariants.

Standard-library only. This validator complements curriculum/provenance validators
without redefining canonical lesson or Project authority.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

MISSION_ID_RE = re.compile(r'^mission_id:\s*"(M\d{2})"\s*$', re.MULTILINE)
STATUS_RE = re.compile(r'^status:\s*(planned|draft|ready)\s*$', re.MULTILINE)
REQUIRES_RE = re.compile(r'^requires_missions:\s*\[(.*?)\]\s*$', re.MULTILINE)
VERSION_TO_RE = re.compile(r'^bot_version_to:\s*"(v\d+\.\d+)"\s*$', re.MULTILINE)
LESSON_ID_RE = re.compile(r'"(\d+\.\d+)"')
PROJECTS_RE = re.compile(r'^\s*contributes_to:\s*\[(.*?)\]\s*$', re.MULTILINE)
ROADMAP_MISSION_RE = re.compile(r'^\|\s*(M\d{2})\s*\|\s*(v\d+\.\d+)\s*\|', re.MULTILINE)
CANON_LESSON_RE = re.compile(r'^- \[[ xX]\] \*\*(\d+\.\d+)\*\* — ', re.MULTILINE)

AUTHORITY_FILES = (
    Path("BUILD-FIRST.md"),
    Path("docs/BUILD-FIRST-LEARNING-MODEL.md"),
    Path("docs/MISSION-AUTHORING-STANDARD.md"),
    Path("docs/MISSION-PASS-CRITERIA.md"),
    Path("docs/BOT-EVOLUTION-ROADMAP.md"),
    Path("docs/MISSION-KNOWLEDGE-MAP.md"),
)

READY_HEADINGS = (
    "## Ship Target",
    "## Starting Bot State",
    "## Build First",
    "## Run",
    "## Observe",
    "## Knowledge Pull",
    "## Improve",
    "## Tests",
    "## Operate",
    "## Failure Case",
    "## Evidence",
    "## Explain-back",
    "## Mission PASS",
    "## Bot Version Result",
    "## Next Mission",
)

BOOTSTRAP_FILES = (
    Path("lab/affiliate-bot/go.mod"),
    Path("lab/affiliate-bot/cmd/bot/main.go"),
    Path("lab/affiliate-bot/data/sample-products.json"),
)


@dataclass(frozen=True)
class Problem:
    code: str
    path: str
    message: str

    def __str__(self) -> str:
        return f"{self.code} {self.path}: {self.message}"


def canonical_lesson_ids(root: Path) -> set[str]:
    ids: set[str] = set()
    for path in sorted((root / "roadmap").glob("part-*.md")):
        ids.update(CANON_LESSON_RE.findall(path.read_text(encoding="utf-8")))
    return ids


def check_authority(root: Path, problems: list[Problem]) -> None:
    for rel in AUTHORITY_FILES:
        if not (root / rel).exists():
            problems.append(Problem("BUILD001", str(rel), "required Build-First authority file is missing"))


def parse_list_ids(raw: str, prefix: str) -> list[str]:
    if not raw.strip():
        return []
    return re.findall(rf'"({prefix}\d{{2}})"', raw)


def version_tuple(version: str) -> tuple[int, int]:
    major, minor = version[1:].split(".", 1)
    return int(major), int(minor)


def check_roadmap_spine(root: Path, problems: list[Problem]) -> dict[str, str]:
    path = root / "docs/BOT-EVOLUTION-ROADMAP.md"
    if not path.exists():
        return {}
    rows = ROADMAP_MISSION_RE.findall(path.read_text(encoding="utf-8"))
    expected = [f"M{i:02d}" for i in range(16)]
    ids = [mission for mission, _ in rows]
    if len(ids) != len(set(ids)):
        problems.append(Problem("BUILD002", str(path.relative_to(root)), "duplicate Mission ID in Bot Evolution roadmap"))
    if ids != expected:
        problems.append(Problem("BUILD003", str(path.relative_to(root)), f"mission spine must be exactly M00..M15 in order; found {ids}"))
    versions = [version for _, version in rows]
    for prev, current in zip(versions, versions[1:]):
        if version_tuple(current) <= version_tuple(prev):
            problems.append(Problem("BUILD006", str(path.relative_to(root)), f"bot versions must increase; found {prev} then {current}"))
    return dict(rows)


def mission_files(root: Path) -> list[Path]:
    directory = root / "missions"
    if not directory.exists():
        return []
    return sorted(p for p in directory.glob("M*.md") if p.name != "README.md")


def check_missions(root: Path, canonical_ids: set[str], spine: dict[str, str], problems: list[Problem]) -> None:
    files = mission_files(root)
    seen: dict[str, Path] = {}
    authored_ids: list[str] = []
    dependency_map: dict[str, list[str]] = {}

    for path in files:
        rel = str(path.relative_to(root))
        text = path.read_text(encoding="utf-8")
        match = MISSION_ID_RE.search(text)
        if not match:
            problems.append(Problem("BUILD002", rel, "missing or invalid mission_id metadata"))
            continue
        mission_id = match.group(1)
        authored_ids.append(mission_id)
        if mission_id in seen:
            problems.append(Problem("BUILD002", rel, f"duplicate authored Mission ID also in {seen[mission_id]}"))
        seen[mission_id] = path
        if not path.name.startswith(mission_id + "-"):
            problems.append(Problem("BUILD002", rel, f"filename must start with {mission_id}-"))

        status_match = STATUS_RE.search(text)
        status = status_match.group(1) if status_match else None
        if status is None:
            problems.append(Problem("BUILD007", rel, "missing valid mission status"))

        requires_match = REQUIRES_RE.search(text)
        deps = parse_list_ids(requires_match.group(1), "M") if requires_match else []
        dependency_map[mission_id] = deps
        current_num = int(mission_id[1:])
        for dep in deps:
            if int(dep[1:]) >= current_num:
                problems.append(Problem("BUILD005", rel, f"dependency must point backward: {mission_id} requires {dep}"))

        version_match = VERSION_TO_RE.search(text)
        if version_match and mission_id in spine and version_match.group(1) != spine[mission_id]:
            problems.append(Problem("BUILD006", rel, f"bot_version_to {version_match.group(1)} does not match roadmap {spine[mission_id]}"))

        # Limit lesson-ref validation to the knowledge metadata block so Project numbers and prose do not look like lesson IDs.
        front_end = text.find("---", 3)
        front = text[: front_end + 3] if front_end != -1 else text
        knowledge_start = front.find("knowledge:")
        projects_start = front.find("projects:")
        knowledge_block = front[knowledge_start:projects_start] if knowledge_start != -1 and projects_start != -1 else ""
        for lesson_id in LESSON_ID_RE.findall(knowledge_block):
            if lesson_id not in canonical_ids:
                problems.append(Problem("BUILD004", rel, f"knowledge lesson ID does not resolve in canonical inventory: {lesson_id}"))

        project_match = PROJECTS_RE.search(text)
        if project_match:
            for raw in re.findall(r"\d+", project_match.group(1)):
                project_id = int(raw)
                if not 1 <= project_id <= 14:
                    problems.append(Problem("BUILD009", rel, f"Mission may reference only canonical Projects 1–14; found {project_id}"))

        lowered = text.lower()
        if "lesson_pass:" in lowered or "auto-pass lesson" in lowered or "auto pass lesson" in lowered:
            problems.append(Problem("BUILD008", rel, "Mission must not contain a mechanism that declares lesson PASS"))

        if status == "ready":
            for heading in READY_HEADINGS:
                if heading not in text:
                    problems.append(Problem("BUILD007", rel, f"ready Mission missing required section: {heading}"))

    authored_sorted = sorted(authored_ids)
    expected_prefix = [f"M{i:02d}" for i in range(len(authored_sorted))]
    if authored_sorted != expected_prefix:
        problems.append(Problem("BUILD003", "missions/", f"authored Mission files must form contiguous prefix from M00; found {authored_sorted}"))

    # Generic cycle detection, even though forward refs are independently rejected.
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> bool:
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        for dep in dependency_map.get(node, []):
            if dep in dependency_map and visit(dep):
                return True
        visiting.remove(node)
        visited.add(node)
        return False

    for node in dependency_map:
        if visit(node):
            problems.append(Problem("BUILD005", "missions/", "Mission dependency graph contains a cycle"))
            break


def check_bootstrap(root: Path, problems: list[Problem]) -> None:
    for rel in BOOTSTRAP_FILES:
        if not (root / rel).exists():
            problems.append(Problem("BUILD010", str(rel), "required bootstrap bot file is missing"))


def validate(root: Path) -> list[Problem]:
    problems: list[Problem] = []
    check_authority(root, problems)
    canonical_ids = canonical_lesson_ids(root)
    spine = check_roadmap_spine(root, problems)
    check_missions(root, canonical_ids, spine, problems)
    check_bootstrap(root, problems)
    return problems


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    problems = validate(root)
    if problems:
        for problem in problems:
            print(problem)
        print(f"Build-First validation failed with {len(problems)} problem(s).")
        return 1
    print("Build-First validation passed: M00-M15 spine, authored missions and bootstrap bot are consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
