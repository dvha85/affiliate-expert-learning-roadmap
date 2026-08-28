#!/usr/bin/env python3
"""Kiểm tra các bất biến của Build-First Learning Architecture.

Validator chỉ dùng standard library. Nó bổ sung các semantic guard cho Mission,
learner workspace và reference implementation mà không thay authority của
canonical Lesson/Project.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

MISSION_ID_RE = re.compile(r'^mission_id:\s*"(M\d{2})"\s*$', re.MULTILINE)
STATUS_RE = re.compile(r'^status:\s*(planned|draft|ready)\s*$', re.MULTILINE)
REQUIRES_RE = re.compile(r'^requires_missions:\s*\[(.*?)\]\s*$', re.MULTILINE)
VERSION_FROM_RE = re.compile(r'^bot_version_from:\s*(null|"v\d+\.\d+")\s*$', re.MULTILINE)
VERSION_TO_RE = re.compile(r'^bot_version_to:\s*"(v\d+\.\d+)"\s*$', re.MULTILINE)
REQUIRED_RE = re.compile(r'^\s*required:\s*\[(.*?)\]\s*$', re.MULTILINE)
LESSON_ID_RE = re.compile(r'"(\d+\.\d+)"')
PROJECTS_RE = re.compile(r'^\s*contributes_to:\s*\[(.*?)\]\s*$', re.MULTILINE)
ROADMAP_MISSION_RE = re.compile(r'^\|\s*(M\d{2})\s*\|\s*(v\d+\.\d+)\s*\|', re.MULTILINE)
PROJECT_MAP_RE = re.compile(r'^-\s+((?:M\d{2})(?:\s+\+\s+M\d{2})*)\s+→\s+Project\s+(\d+)\b', re.MULTILINE)
CANON_LESSON_RE = re.compile(r'^- \[[ xX]\] \*\*(\d+\.\d+)\*\* — ', re.MULTILINE)
GO_DIRECTIVE_RE = re.compile(r'^go\s+(\d+\.\d+)\s*$', re.MULTILINE)
CURRENT_MISSION_RE = re.compile(r'\|\s*Current Mission[^|]*\|\s*\*\*(M\d{2})\b', re.MULTILINE)

AUTHORITY_FILES = (
    Path("BUILD-FIRST.md"),
    Path("docs/BUILD-FIRST-LEARNING-MODEL.md"),
    Path("docs/MISSION-AUTHORING-STANDARD.md"),
    Path("docs/MISSION-PASS-CRITERIA.md"),
    Path("docs/BOT-EVOLUTION-ROADMAP.md"),
    Path("docs/MISSION-KNOWLEDGE-MAP.md"),
    Path("docs/LANGUAGE-POLICY.md"),
)

LANGUAGE_AUTHORITY_DOCS = (
    Path("README.md"),
    Path("BUILD-FIRST.md"),
    Path("CONTRIBUTING.md"),
    Path("docs/MISSION-AUTHORING-STANDARD.md"),
    Path("docs/CURRICULUM-CI.md"),
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

REFERENCE_BOOTSTRAP_FILES = (
    Path("lab/affiliate-bot/go.mod"),
    Path("lab/affiliate-bot/cmd/bot/main.go"),
    Path("lab/affiliate-bot/data/sample-products.json"),
)

LEARNER_BOOTSTRAP_FILES = (
    Path("lab/learner/affiliate-bot/go.mod"),
    Path("lab/learner/affiliate-bot/README.md"),
    Path("lab/learner/affiliate-bot/cmd/bot/main.go"),
    Path("lab/learner/affiliate-bot/data/sample-products.json"),
)

# Capability ceiling (trần năng lực) theo Mission đang học.
# Guard này chỉ bảo vệ M00-M03 đã author; khi PROGRESS tiến lên, capability tương ứng
# được phép xuất hiện trong learner workspace.
FORBIDDEN_BY_CURRENT_MISSION = {
    "M00": (
        "encoding/json",
        "internal/product",
        "internal/ingest",
        "internal/store",
        "internal/ranking",
        "Loaded products:",
        "Stored snapshots:",
        "Commission-only ranking:",
        "Expected-value ranking:",
    ),
    "M01": (
        "internal/store",
        "internal/ranking",
        "Stored snapshots:",
        "Commission-only ranking:",
        "Expected-value ranking:",
    ),
    "M02": (
        "internal/ranking",
        "Commission-only ranking:",
        "Expected-value ranking:",
    ),
    "M03": (),
}


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
            problems.append(Problem("BUILD001", str(rel), "thiếu file authority bắt buộc của Build-First"))


def check_language_policy(root: Path, problems: list[Problem]) -> None:
    policy = root / "docs/LANGUAGE-POLICY.md"
    if policy.exists():
        text = policy.read_text(encoding="utf-8")
        if "Tiếng Việt là ngôn ngữ chính thức" not in text:
            problems.append(Problem("LANG001", "docs/LANGUAGE-POLICY.md", "Language Policy phải xác định tiếng Việt là ngôn ngữ chính thức"))

    for rel in LANGUAGE_AUTHORITY_DOCS:
        path = root / rel
        if path.exists() and "LANGUAGE-POLICY.md" not in path.read_text(encoding="utf-8"):
            problems.append(Problem("LANG001", str(rel), "authority document phải tham chiếu docs/LANGUAGE-POLICY.md"))


def parse_list_ids(raw: str, prefix: str) -> list[str]:
    if not raw.strip():
        return []
    return re.findall(rf'"({prefix}\d{{2}})"', raw)


def parse_project_ids(raw: str) -> set[int]:
    return {int(value) for value in re.findall(r"\d+", raw)}


def parse_version_from(raw: str) -> str | None:
    if raw == "null":
        return None
    return raw.strip('"')


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
        problems.append(Problem("BUILD002", str(path.relative_to(root)), "Mission ID bị trùng trong Bot Evolution Roadmap"))
    if ids != expected:
        problems.append(Problem("BUILD003", str(path.relative_to(root)), f"Mission spine phải đúng M00..M15 theo thứ tự; hiện có {ids}"))
    versions = [version for _, version in rows]
    for prev, current in zip(versions, versions[1:]):
        if version_tuple(current) <= version_tuple(prev):
            problems.append(Problem("BUILD006", str(path.relative_to(root)), f"Bot Version phải tăng; gặp {prev} rồi {current}"))
    return dict(rows)


def central_project_map(root: Path) -> dict[str, set[int]]:
    path = root / "docs/BOT-EVOLUTION-ROADMAP.md"
    mapping: dict[str, set[int]] = {}
    if not path.exists():
        return mapping
    text = path.read_text(encoding="utf-8")
    for missions_raw, project_raw in PROJECT_MAP_RE.findall(text):
        project_id = int(project_raw)
        for mission_id in re.findall(r"M\d{2}", missions_raw):
            mapping.setdefault(mission_id, set()).add(project_id)
    return mapping


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
    version_from_map: dict[str, str | None] = {}
    version_to_map: dict[str, str] = {}
    mission_projects: dict[str, set[int]] = {}
    project_map = central_project_map(root)

    for path in files:
        rel = str(path.relative_to(root))
        text = path.read_text(encoding="utf-8")
        match = MISSION_ID_RE.search(text)
        if not match:
            problems.append(Problem("BUILD002", rel, "thiếu hoặc sai mission_id metadata"))
            continue
        mission_id = match.group(1)
        authored_ids.append(mission_id)
        if mission_id in seen:
            problems.append(Problem("BUILD002", rel, f"Mission ID bị trùng; đã có tại {seen[mission_id]}"))
        seen[mission_id] = path
        if not path.name.startswith(mission_id + "-"):
            problems.append(Problem("BUILD002", rel, f"filename phải bắt đầu bằng {mission_id}-"))

        status_match = STATUS_RE.search(text)
        status = status_match.group(1) if status_match else None
        if status is None:
            problems.append(Problem("BUILD007", rel, "thiếu mission status hợp lệ"))

        requires_match = REQUIRES_RE.search(text)
        deps = parse_list_ids(requires_match.group(1), "M") if requires_match else []
        dependency_map[mission_id] = deps
        current_num = int(mission_id[1:])
        for dep in deps:
            if int(dep[1:]) >= current_num:
                problems.append(Problem("BUILD005", rel, f"dependency phải trỏ về Mission trước: {mission_id} requires {dep}"))

        version_from_match = VERSION_FROM_RE.search(text)
        if version_from_match:
            version_from_map[mission_id] = parse_version_from(version_from_match.group(1))
        else:
            problems.append(Problem("BUILD012", rel, "thiếu hoặc sai bot_version_from"))

        version_match = VERSION_TO_RE.search(text)
        if version_match:
            version_to_map[mission_id] = version_match.group(1)
            if mission_id in spine and version_match.group(1) != spine[mission_id]:
                problems.append(Problem("BUILD006", rel, f"bot_version_to {version_match.group(1)} không khớp roadmap {spine[mission_id]}"))
        else:
            problems.append(Problem("BUILD006", rel, "thiếu bot_version_to hợp lệ"))

        # Chỉ đọc lesson refs trong knowledge metadata để Project/prose không bị hiểu nhầm là Lesson ID.
        front_end = text.find("---", 3)
        front = text[: front_end + 3] if front_end != -1 else text
        knowledge_start = front.find("knowledge:")
        projects_start = front.find("projects:")
        knowledge_block = front[knowledge_start:projects_start] if knowledge_start != -1 and projects_start != -1 else ""
        knowledge_ids = LESSON_ID_RE.findall(knowledge_block)
        for lesson_id in knowledge_ids:
            if lesson_id not in canonical_ids:
                problems.append(Problem("BUILD004", rel, f"knowledge Lesson ID không resolve trong canonical inventory: {lesson_id}"))

        if status == "ready":
            required_match = REQUIRED_RE.search(knowledge_block)
            required_ids = LESSON_ID_RE.findall(required_match.group(1)) if required_match else []
            if not required_ids:
                problems.append(Problem("BUILD004", rel, "Mission ready phải có ít nhất một canonical Lesson ID trong knowledge.required"))

        project_match = PROJECTS_RE.search(text)
        projects = parse_project_ids(project_match.group(1)) if project_match else set()
        mission_projects[mission_id] = projects
        for project_id in projects:
            if not 1 <= project_id <= 14:
                problems.append(Problem("BUILD009", rel, f"Mission chỉ được tham chiếu canonical Projects 1–14; gặp {project_id}"))

        lowered = text.lower()
        if "lesson_pass:" in lowered or "auto-pass lesson" in lowered or "auto pass lesson" in lowered:
            problems.append(Problem("BUILD008", rel, "Mission không được có cơ chế tự tuyên bố Lesson PASS"))

        if status == "ready":
            for heading in READY_HEADINGS:
                if heading not in text:
                    problems.append(Problem("BUILD007", rel, f"Mission ready thiếu section bắt buộc: {heading}"))

            if int(mission_id[1:]) <= 3:
                if "lab/learner/affiliate-bot/" not in text:
                    problems.append(Problem("BUILD011", rel, "bootstrap Mission ready phải chỉ rõ learner workspace"))
                if "cd lab/affiliate-bot" in text:
                    problems.append(Problem("BUILD011", rel, "bootstrap Mission không được dùng reference implementation làm Run/Build workspace"))

    authored_sorted = sorted(authored_ids)
    expected_prefix = [f"M{i:02d}" for i in range(len(authored_sorted))]
    if authored_sorted != expected_prefix:
        problems.append(Problem("BUILD003", "missions/", f"authored Mission files phải là prefix liên tục từ M00; hiện có {authored_sorted}"))

    # Dependency phải tồn tại trong authored prefix, không chỉ trỏ ngược về số nhỏ hơn.
    for mission_id, deps in dependency_map.items():
        for dep in deps:
            if dep not in seen:
                problems.append(Problem("BUILD005", str(seen[mission_id].relative_to(root)), f"dependency {dep} chưa có authored Mission file"))

    # Bot Version continuity: M00 bắt đầu từ null; mỗi Mission sau bắt đầu từ bot_version_to của Mission ngay trước.
    for index, mission_id in enumerate(authored_sorted):
        rel = str(seen[mission_id].relative_to(root))
        if index == 0:
            if version_from_map.get(mission_id) is not None:
                problems.append(Problem("BUILD012", rel, "M00 bot_version_from phải là null"))
            continue
        previous = authored_sorted[index - 1]
        expected_from = version_to_map.get(previous)
        if expected_from is not None and version_from_map.get(mission_id) != expected_from:
            problems.append(Problem("BUILD012", rel, f"bot_version_from phải bằng {previous}.bot_version_to ({expected_from})"))

    # Mission frontmatter và central Bot Evolution Project map phải cùng một nguồn sự thật.
    for mission_id in authored_sorted:
        expected_projects = project_map.get(mission_id, set())
        actual_projects = mission_projects.get(mission_id, set())
        if expected_projects != actual_projects:
            rel = str(seen[mission_id].relative_to(root))
            problems.append(Problem("BUILD013", rel, f"Project contribution lệch central map: frontmatter={sorted(actual_projects)} central={sorted(expected_projects)}"))

    # Generic cycle detection, dù forward refs đã bị chặn độc lập.
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
            problems.append(Problem("BUILD005", "missions/", "Mission dependency graph có cycle"))
            break


def go_directive(path: Path) -> str | None:
    if not path.exists():
        return None
    match = GO_DIRECTIVE_RE.search(path.read_text(encoding="utf-8"))
    return match.group(1) if match else None


def current_mission(root: Path) -> str | None:
    path = root / "PROGRESS.md"
    if not path.exists():
        return None
    match = CURRENT_MISSION_RE.search(path.read_text(encoding="utf-8"))
    return match.group(1) if match else None


def learner_go_text(root: Path) -> str:
    base = root / "lab/learner/affiliate-bot"
    texts: list[str] = []
    if not base.exists():
        return ""
    for path in sorted(base.rglob("*.go")):
        texts.append(path.read_text(encoding="utf-8"))
    return "\n".join(texts)


def check_bootstrap(root: Path, problems: list[Problem]) -> None:
    for rel in REFERENCE_BOOTSTRAP_FILES:
        if not (root / rel).exists():
            problems.append(Problem("BUILD010", str(rel), "thiếu file reference bootstrap bắt buộc"))
    for rel in LEARNER_BOOTSTRAP_FILES:
        if not (root / rel).exists():
            problems.append(Problem("BUILD010", str(rel), "thiếu file learner bootstrap bắt buộc"))

    reference_go = go_directive(root / "lab/affiliate-bot/go.mod")
    learner_go = go_directive(root / "lab/learner/affiliate-bot/go.mod")
    if reference_go and learner_go and reference_go != learner_go:
        problems.append(Problem("BUILD014", "lab/", f"learner/reference Go directive phải đồng bộ; learner={learner_go}, reference={reference_go}"))

    mission_id = current_mission(root)
    if mission_id in FORBIDDEN_BY_CURRENT_MISSION:
        text = learner_go_text(root)
        for token in FORBIDDEN_BY_CURRENT_MISSION[mission_id]:
            if token in text:
                problems.append(Problem("BUILD011", "lab/learner/affiliate-bot/", f"learner workspace vượt capability ceiling của {mission_id}: gặp {token!r}"))


def validate(root: Path) -> list[Problem]:
    problems: list[Problem] = []
    check_authority(root, problems)
    check_language_policy(root, problems)
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
    print("Build-First validation passed: Mission spine, semantic continuity, learner/reference boundaries and language authority are consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
