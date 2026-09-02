#!/usr/bin/env python3
"""Kiểm tra các bất biến của Build-First Learning Architecture.

Validator chỉ dùng standard library. Nó bổ sung các semantic guard cho Mission,
learner workspace và reference implementation mà không thay authority của
CURRICULUM/ROADMAP.
"""
from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

MISSION_ID_RE = re.compile(r'^mission_id:\s*"(M\d{2})"\s*$', re.MULTILINE)
STATUS_RE = re.compile(r'^status:\s*(planned|draft|ready)\s*$', re.MULTILINE)
CURRICULUM_VERSION_RE = re.compile(r'^curriculum_version:\s*(\d+)\s*$', re.MULTILINE)
REQUIRES_RE = re.compile(r'^requires_missions:\s*\[(.*?)\]\s*$', re.MULTILINE)
VERSION_FROM_RE = re.compile(r'^bot_version_from:\s*(null|"v\d+\.\d+")\s*$', re.MULTILINE)
VERSION_TO_RE = re.compile(r'^bot_version_to:\s*(null|"v\d+\.\d+")\s*$', re.MULTILINE)
REQUIRED_RE = re.compile(r'^\s*required:\s*\[(.*?)\]\s*$', re.MULTILINE)
LESSON_ID_RE = re.compile(r'"(\d+\.\d+)"')
ROADMAP_MISSION_RE = re.compile(r'^\|\s*(M\d{2})\s*\|\s*((?:v\d+\.\d+)|pre-bot)\s*\|', re.MULTILINE)
CANON_LESSON_RE = re.compile(r'^- \[[ xX]\] \*\*(\d+\.\d+)\*\* — ', re.MULTILINE)
CANON_LESSON_LINK_RE = re.compile(
    r'^- \[[ xX]\] \*\*(\d+\.\d+)\*\* — \[[^]]+\]\(([^)]+)\)',
    re.MULTILINE,
)
CHAPTER_RE = re.compile(r'^### Chương\s+(\d+)\s+—', re.MULTILINE)
DECLARED_COUNTS_RE = re.compile(
    r'(?:Tổng cộng:\s*)?\*\*(\d+)\s+(?:phần|Parts?)\s*·\s*'
    r'(\d+)\s+(?:chương|Chapters?)\s*·\s*'
    r'(\d+)\s+(?:bài học|Lessons?|micro-lessons?)\*\*',
    re.IGNORECASE,
)
TABLE_MISSION_RE = re.compile(r'^\|\s*(M\d{2})(?:\s+—[^|]*)?\s*\|', re.MULTILINE)
ROADMAP_EVIDENCE_RE = re.compile(r'^\|\s*(M\d{2})\s*\|[^\n|]*\|\s*(E[0-6])\s*\|', re.MULTILINE)
MINIMUM_LEVEL_RE = re.compile(r'^\s{2}minimum_level:\s*"(E[0-6])"\s*$', re.MULTILINE)
REALITY_REQUIRED_RE = re.compile(r'^\s{2}reality_required:\s*(true|false)\s*$', re.MULTILINE)
SAFETY_GATE_RE = re.compile(r'^safety_gate:\s*"(S[0-6])"\s*$', re.MULTILINE)
LESSON_FRONT_ID_RE = re.compile(r'^lesson_id:\s*"(\d+\.\d+)"\s*$', re.MULTILINE)
LESSON_STATUS_RE = re.compile(r'^status:\s*(planned|draft|ready)\s*$', re.MULTILINE)
GO_DIRECTIVE_RE = re.compile(r'^go\s+(\d+\.\d+)\s*$', re.MULTILINE)
CURRENT_MISSION_RES = (
    re.compile(r'\|\s*Current Mission[^|]*\|\s*\*\*(M\d{2})\b', re.MULTILINE),
    re.compile(r'^Current Mission:\s*(M\d{2})\s*$', re.MULTILINE),
)

AUTHORITY_FILES = (
    Path("CURRICULUM.md"),
    Path("ROADMAP.md"),
    Path("BUILD-FIRST.md"),
    Path("docs/BUILD-FIRST-LEARNING-MODEL.md"),
    Path("docs/MISSION-AUTHORING-STANDARD.md"),
    Path("docs/MISSION-PASS-CRITERIA.md"),
    Path("docs/BOT-EVOLUTION-ROADMAP.md"),
    Path("docs/MISSION-KNOWLEDGE-MAP.md"),
    Path("docs/LANGUAGE-POLICY.md"),
)

LANGUAGE_AUTHORITY_DOCS = (
    Path("docs/CURRICULUM-CI.md"),
)

READY_HEADINGS = (
    "## Ship Target",
    "## Starting Bot State",
    "## Try First",
    "## Run",
    "## Observe",
    "## Knowledge Pull",
    "## Improve",
    "## Tests",
    "## Reality Check",
    "## Operate",
    "## Failure Case",
    "## Safety Gate",
    "## Evidence",
    "## Explain-back",
    "## Mission PASS",
    "## Bot Version Result",
    "## Next Mission",
)

REFERENCE_BOOTSTRAP_FILES = (
    Path("lab/affiliate-bot/README.md"),
    Path("lab/affiliate-bot/go.mod"),
    Path("lab/affiliate-bot/cmd/bot/main.go"),
    Path("lab/affiliate-bot/data/sample-products.json"),
)

LEARNER_BOOTSTRAP_FILES = (
    Path("lab/learner/affiliate-bot/go.mod"),
    Path("lab/learner/affiliate-bot/README.md"),
    Path("lab/learner/affiliate-bot/cmd/bot/main.go"),
    Path("lab/learner/affiliate-bot/cmd/bot/main_test.go"),
    Path("lab/learner/affiliate-bot/internal/observation/observation.go"),
    Path("lab/learner/affiliate-bot/internal/decision/ranking.go"),
    Path("lab/learner/affiliate-bot/data/m00-missing-input.json"),
    Path("lab/learner/affiliate-bot/data/m00-conflicting-input.json"),
    Path("lab/learner/affiliate-bot/HINTS-M00.md"),
)

# Capability ceiling (trần năng lực) theo Mission đang học. M00 nay hợp lệ với
# JSON/Observation/ranking; guard chỉ chặn AI/tool/action authority xuất hiện sớm.
FORBIDDEN_BY_CURRENT_MISSION = {
    "M00": (
        "internal/ai",
        "internal/agent",
        "ActionIntent",
        "ApprovalRequest",
        "ExecutionRecord",
    ),
    "M01": (
        "internal/ai",
        "internal/agent",
        "ActionIntent",
        "ApprovalRequest",
        "ExecutionRecord",
    ),
    "M02": (
        "internal/agent",
        "ActionIntent",
        "ApprovalRequest",
        "ExecutionRecord",
    ),
    **{
        f"M{i:02d}": ("internal/agent", "ActionIntent", "ApprovalRequest", "ExecutionRecord")
        for i in range(3, 8)
    },
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


def declared_counts(path: Path) -> tuple[int, int, int] | None:
    if not path.exists():
        return None
    match = DECLARED_COUNTS_RE.search(path.read_text(encoding="utf-8"))
    return tuple(map(int, match.groups())) if match else None


def check_dynamic_inventory_authority(root: Path, problems: list[Problem]) -> None:
    """Protect agreement, not a frozen inventory size.

    CURRICULUM/ROADMAP currently declare 7/21/63, but an intentional future
    redesign may change those numbers without requiring validator code edits.
    """
    curriculum_rel = Path("CURRICULUM.md")
    roadmap_rel = Path("ROADMAP.md")
    curriculum_counts = declared_counts(root / curriculum_rel)
    roadmap_counts = declared_counts(root / roadmap_rel)
    if curriculum_counts is None:
        problems.append(Problem("BUILD015", str(curriculum_rel), "không đọc được tổng Part/Chapter/Lesson động"))
    if roadmap_counts is None:
        problems.append(Problem("BUILD015", str(roadmap_rel), "không đọc được tổng Part/Chapter/Lesson động"))
    if curriculum_counts is None or roadmap_counts is None:
        return
    if curriculum_counts != roadmap_counts:
        problems.append(
            Problem(
                "BUILD015",
                str(roadmap_rel),
                f"tổng inventory lệch CURRICULUM: curriculum={curriculum_counts}, roadmap={roadmap_counts}",
            )
        )

    part_files = sorted((root / "roadmap").glob("part-*.md"))
    chapters: list[str] = []
    lessons: list[str] = []
    for path in part_files:
        text = path.read_text(encoding="utf-8")
        chapters.extend(CHAPTER_RE.findall(text))
        lessons.extend(CANON_LESSON_RE.findall(text))
    actual = len(part_files), len(chapters), len(lessons)
    if actual != curriculum_counts:
        problems.append(
            Problem(
                "BUILD015",
                "roadmap/",
                f"inventory thực tế {actual} không khớp authority {curriculum_counts}",
            )
        )


def roadmap_lesson_links(root: Path) -> dict[str, Path]:
    links: dict[str, Path] = {}
    for roadmap_path in sorted((root / "roadmap").glob("part-*.md")):
        text = roadmap_path.read_text(encoding="utf-8")
        for lesson_id, raw_target in CANON_LESSON_LINK_RE.findall(text):
            target = (roadmap_path.parent / raw_target).resolve()
            links[lesson_id] = target
    return links


def ready_lesson_problem(root: Path, lesson_id: str, links: dict[str, Path]) -> str | None:
    path = links.get(lesson_id)
    if path is None:
        return f"required Lesson {lesson_id} phải có link active trong ROADMAP"
    try:
        path.relative_to(root.resolve())
    except ValueError:
        return f"required Lesson {lesson_id} link ra ngoài repository"
    if not path.is_file():
        return f"required Lesson {lesson_id} link tới file không tồn tại"
    text = path.read_text(encoding="utf-8")
    front_end = text.find("---", 3)
    front = text[: front_end + 3] if text.startswith("---") and front_end != -1 else ""
    id_match = LESSON_FRONT_ID_RE.search(front)
    status_match = LESSON_STATUS_RE.search(front)
    if not id_match or id_match.group(1) != lesson_id:
        return f"required Lesson {lesson_id} không khớp lesson_id trong file linked"
    if not status_match or status_match.group(1) != "ready":
        status = status_match.group(1) if status_match else "missing"
        return f"required Lesson {lesson_id} phải status=ready; hiện là {status}"
    return None


def indented_block(front: str, key: str) -> str:
    match = re.search(rf"(?ms)^{re.escape(key)}:\s*\n((?:^[ \t]+.*(?:\n|$))*)", front)
    return match.group(1) if match else ""


def roadmap_evidence_levels(root: Path) -> dict[str, str]:
    path = root / "ROADMAP.md"
    if not path.exists():
        return {}
    return dict(ROADMAP_EVIDENCE_RE.findall(path.read_text(encoding="utf-8")))


def check_authority(root: Path, problems: list[Problem]) -> None:
    for rel in AUTHORITY_FILES:
        path = root / rel
        if not path.exists():
            problems.append(Problem("BUILD001", str(rel), "thiếu file authority bắt buộc của Build-First"))
            continue
        text = path.read_text(encoding="utf-8")
        if re.search(r"Technical PASS|Evidence PASS", text, re.IGNORECASE):
            problems.append(
                Problem(
                    "BUILD018",
                    str(rel),
                    "active authority phải dùng Capability PASS / Reality verified / Operated, không dùng PASS vocabulary cũ",
                )
            )

    progress = root / "PROGRESS.md"
    if progress.exists():
        text = progress.read_text(encoding="utf-8")
        if not re.search(r"\|\s*E5\s*\|[^\n]*(?:governed canary|bounded governed canary)", text, re.IGNORECASE):
            problems.append(Problem("BUILD018", "PROGRESS.md", "E5 phải là bounded governed canary, đồng bộ CURRICULUM"))
        if "Learner Bot: pre-v0.1 scaffold" not in text:
            problems.append(Problem("BUILD018", "PROGRESS.md", "starting Bot version phải là pre-v0.1 scaffold"))


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
    expected = [f"M{i:02d}" for i in range(12)]
    ids = [mission for mission, _ in rows]
    if len(ids) != len(set(ids)):
        problems.append(Problem("BUILD002", str(path.relative_to(root)), "Mission ID bị trùng trong Bot Evolution Roadmap"))
    if ids != expected:
        problems.append(Problem("BUILD003", str(path.relative_to(root)), f"Mission spine phải đúng M00..M11 theo thứ tự; hiện có {ids}"))

    # Root authority and normalized ROADMAP must expose the same Mission spine.
    for rel in (Path("CURRICULUM.md"), Path("ROADMAP.md")):
        authority = root / rel
        if not authority.exists():
            continue
        authority_ids = TABLE_MISSION_RE.findall(authority.read_text(encoding="utf-8"))
        if authority_ids != expected:
            problems.append(Problem("BUILD003", str(rel), f"Mission table phải đúng M00..M11 theo thứ tự; hiện có {authority_ids}"))
    versions = [version for _, version in rows if version != "pre-bot"]
    for prev, current in zip(versions, versions[1:]):
        if version_tuple(current) <= version_tuple(prev):
            problems.append(Problem("BUILD006", str(path.relative_to(root)), f"Bot Version phải tăng; gặp {prev} rồi {current}"))
    return dict(rows)


def mission_files(root: Path) -> list[Path]:
    directory = root / "missions"
    if not directory.exists():
        return []
    return sorted(p for p in directory.glob("M*.md") if p.name != "README.md")


def require_semantic(
    text: str,
    patterns: tuple[str, ...],
    rel: str,
    message: str,
    problems: list[Problem],
) -> None:
    if not all(re.search(pattern, text, re.IGNORECASE | re.DOTALL) for pattern in patterns):
        problems.append(Problem("BUILD017", rel, message))


def check_mission_semantics(
    mission_id: str,
    text: str,
    front: str,
    rel: str,
    problems: list[Problem],
) -> None:
    """Guard the reality-first sequence at its first irreversible milestones."""
    if mission_id == "M00":
        actor = re.search(r'^\s{2}execution_actor:\s*"([^"]+)"\s*$', front, re.MULTILINE)
        side_effect = re.search(r'^\s{2}external_side_effects:\s*(true|false)\s*$', front, re.MULTILINE)
        if not actor or actor.group(1) != "human_only" or not side_effect or side_effect.group(1) != "true":
            problems.append(Problem("BUILD017", rel, "M00 phải khai báo external side effect do human_only thực hiện"))
        require_semantic(
            text,
            (
                r"(?:public\s+(?:product\s+)?observations?|E1\s+public)",
                r"(?:manual publish|tự tay publish|human\s+(?:manual\s+)?publish)",
                r"disclosure|công bố",
                r"tracking|theo dõi",
            ),
            rel,
            "M00 phải có E1 public evidence, human manual publish và disclosure/tracking",
            problems,
        )
        require_semantic(
            text,
            (r"(?:Bot|AI).{0,120}(?:không có|no|never).{0,100}(?:publish|external execution)",),
            rel,
            "M00 phải cấm Bot/AI publish hoặc external execution",
            problems,
        )

    if mission_id == "M01":
        require_semantic(
            text,
            (r"(?:real|thật)[^\n]{0,80}(?:analytics|export|outcome)|(?:analytics|export|outcome)[^\n]{0,80}(?:real|thật)", r"missing", r"zero|\b0\b"),
            rel,
            "M01 phải dùng analytics/export/outcome thật và giữ missing khác observed zero",
            problems,
        )

    if mission_id == "M02":
        require_semantic(
            text,
            (r"deterministic|tất định", r"GET_MORE_DATA|HUMAN_REVIEW|abstain", r"(?:không|no).{0,100}(?:AI|model call|tool)"),
            rel,
            "M02 phải có deterministic baseline, abstain state và không gọi AI/tool",
            problems,
        )

    if mission_id == "M03":
        require_semantic(
            text,
            (r"append-only|bất biến", r"provenance|nguồn gốc", r"freshness|độ mới", r"missing"),
            rel,
            "M03 phải có history append-only, provenance/freshness và missing semantics",
            problems,
        )

    if mission_id == "M04":
        require_semantic(
            text,
            (r"grounded|căn cứ bằng chứng", r"evidence refs?|tham chiếu bằng chứng", r"fallback|từ chối", r"(?:không|no).{0,100}(?:tool|write|publish|execution)"),
            rel,
            "M04 phải có grounded advisory, evidence refs, fallback và cấm tool/write/execute",
            problems,
        )

    if mission_id == "M05":
        require_semantic(
            text,
            (r"(?:improvement|cải tiến|ChangeProposal)", r"(?:Outcome|outcome).{0,160}(?:Evaluation|evaluation)|(?:Evaluation|evaluation).{0,160}(?:Outcome|outcome)", r"(?:review|rollback|version)"),
            rel,
            "M05 phải tạo improvement từ Outcome→Evaluation và đi qua review/version/rollback",
            problems,
        )


def check_missions(root: Path, canonical_ids: set[str], spine: dict[str, str], problems: list[Problem]) -> None:
    files = mission_files(root)
    seen: dict[str, Path] = {}
    authored_ids: list[str] = []
    dependency_map: dict[str, list[str]] = {}
    version_from_map: dict[str, str | None] = {}
    version_to_map: dict[str, str | None] = {}
    lesson_links = roadmap_lesson_links(root)
    expected_evidence = roadmap_evidence_levels(root)

    for path in files:
        rel = str(path.relative_to(root))
        text = path.read_text(encoding="utf-8")
        # v1 files are immutable migration/reference material. Their own
        # schema is checked by validate_readiness; only v2 files participate
        # in the active dependency/evidence/version graph.
        curriculum_match = CURRICULUM_VERSION_RE.search(text)
        if curriculum_match and int(curriculum_match.group(1)) != 2:
            continue
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
            version_to = parse_version_from(version_match.group(1))
            version_to_map[mission_id] = version_to
            if version_to is not None and mission_id in spine and version_to != spine[mission_id]:
                problems.append(Problem("BUILD006", rel, f"bot_version_to {version_to} không khớp roadmap {spine[mission_id]}"))
        else:
            problems.append(Problem("BUILD006", rel, "thiếu bot_version_to hợp lệ"))

        # Chỉ đọc Lesson refs trong knowledge metadata để prose không bị hiểu nhầm là Lesson ID.
        front_end = text.find("---", 3)
        front = text[: front_end + 3] if front_end != -1 else text
        knowledge_block = indented_block(front, "knowledge")
        knowledge_ids = LESSON_ID_RE.findall(knowledge_block)
        for lesson_id in knowledge_ids:
            if lesson_id not in canonical_ids:
                problems.append(Problem("BUILD004", rel, f"knowledge Lesson ID không resolve trong canonical inventory: {lesson_id}"))

        required_ids: list[str] = []
        if status == "ready":
            required_match = REQUIRED_RE.search(knowledge_block)
            required_ids = LESSON_ID_RE.findall(required_match.group(1)) if required_match else []
            if not required_ids:
                problems.append(Problem("BUILD004", rel, "Mission ready phải có ít nhất một canonical Lesson ID trong knowledge.required"))
            for lesson_id in required_ids:
                lesson_problem = ready_lesson_problem(root, lesson_id, lesson_links)
                if lesson_problem:
                    problems.append(Problem("BUILD016", rel, lesson_problem))

        minimum_match = MINIMUM_LEVEL_RE.search(front)
        reality_match = REALITY_REQUIRED_RE.search(front)
        safety_match = SAFETY_GATE_RE.search(front)
        if not minimum_match:
            problems.append(Problem("BUILD016", rel, "thiếu evidence.minimum_level hợp lệ E0–E6"))
        elif mission_id in expected_evidence and minimum_match.group(1) != expected_evidence[mission_id]:
            problems.append(
                Problem(
                    "BUILD016",
                    rel,
                    f"evidence.minimum_level phải là {expected_evidence[mission_id]} theo ROADMAP; hiện là {minimum_match.group(1)}",
                )
            )
        if not reality_match:
            problems.append(Problem("BUILD016", rel, "thiếu evidence.reality_required boolean"))
        elif mission_id in expected_evidence and reality_match.group(1) != "true":
            problems.append(Problem("BUILD016", rel, "Mission có E-level trong ROADMAP phải đặt reality_required: true"))
        if not safety_match:
            problems.append(Problem("BUILD016", rel, "thiếu safety_gate hợp lệ S0–S6"))

        check_mission_semantics(mission_id, text, front, rel, problems)

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
    text = path.read_text(encoding="utf-8")
    if "Curriculum version: 1" in text:
        return None
    for pattern in CURRENT_MISSION_RES:
        match = pattern.search(text)
        if match:
            return match.group(1)
    return None


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

    reference_readme = root / "lab/affiliate-bot/README.md"
    if reference_readme.exists():
        text = reference_readme.read_text(encoding="utf-8")
        required = ("legacy engineering reference", "Curriculum v2 maps the first", "M04 is Grounded AI Advisor")
        if not all(marker in text for marker in required):
            problems.append(Problem("BUILD020", str(reference_readme.relative_to(root)), "reference snapshot phải cảnh báo mapping v1 và nêu v2 M02/M04 hiện hành"))
    learner_data = root / "lab/learner/affiliate-bot/data"
    if not learner_data.exists() or not any(learner_data.glob("*.json")):
        problems.append(Problem("BUILD010", str(learner_data.relative_to(root)), "learner bootstrap phải có ít nhất một JSON fixture được gắn nhãn rõ"))

    observation_path = root / "lab/learner/affiliate-bot/internal/observation/observation.go"
    if observation_path.exists():
        text = observation_path.read_text(encoding="utf-8")
        required_patterns = (
            r"Price\s+\*float64",
            r"CommissionRate\s+\*float64",
            r"Currency\s+string",
            r'AccessPublicManual\s*=\s*"public_manual"',
            r"DecisionIssues\(\)",
        )
        if not all(re.search(pattern, text) for pattern in required_patterns):
            problems.append(Problem("BUILD019", str(observation_path.relative_to(root)), "M00 scaffold phải giữ nullable price/commission và minimal public-evidence gate"))

    decision_path = root / "lab/learner/affiliate-bot/internal/decision/ranking.go"
    if decision_path.exists():
        text = decision_path.read_text(encoding="utf-8")
        for state in ("RANK_SCENARIO", "RECOMMEND", "GET_MORE_DATA", "HUMAN_REVIEW"):
            if state not in text:
                problems.append(Problem("BUILD019", str(decision_path.relative_to(root)), f"M00 scaffold thiếu decision state {state}"))

    main_path = root / "lab/learner/affiliate-bot/cmd/bot/main.go"
    test_path = root / "lab/learner/affiliate-bot/cmd/bot/main_test.go"
    if main_path.exists() and "io.Writer" not in main_path.read_text(encoding="utf-8"):
        problems.append(Problem("BUILD019", str(main_path.relative_to(root)), "M00 output phải injectable để beginner test behavior không cần tự refactor"))
    if test_path.exists() and "TestRunShowsSafeStarterState" not in test_path.read_text(encoding="utf-8"):
        problems.append(Problem("BUILD019", str(test_path.relative_to(root)), "M00 phải có output-test skeleton cho beginner"))

    for name in ("m00-missing-input.json", "m00-conflicting-input.json"):
        path = learner_data / name
        if not path.exists():
            continue
        try:
            records = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            problems.append(Problem("BUILD019", str(path.relative_to(root)), "M00 failure fixture phải là JSON hợp lệ"))
            continue
        if any(record.get("evidence_kind") == "real" for record in records if isinstance(record, dict)):
            problems.append(Problem("BUILD019", str(path.relative_to(root)), "provided failure fixture không được giả nhãn real evidence"))

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
    check_dynamic_inventory_authority(root, problems)
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
    print("Build-First validation passed: dynamic inventory, M00-M11 spine, reality gates and learner/reference boundaries are consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
