#!/usr/bin/env python3
"""Semantic guards for the mission-based Build-First curriculum.

The active learner path is Mission-based. This validator protects sequence,
evidence/authority ceilings and bootstrap safety without restoring legacy
Publish-First or numeric-lesson reading order.
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
TABLE_MISSION_RE = re.compile(r'^\|\s*(?:\*\*)?(M\d{2})(?:\*\*)?(?:\s+—[^|]*)?\s*\|', re.MULTILINE)
ROADMAP_EVIDENCE_RE = re.compile(r'^\|\s*(?:\*\*)?(M\d{2})(?:\*\*)?\s*\|[^\n|]*\|\s*(E[0-6](?:→E[0-6])?)\s*\|', re.MULTILINE)
MINIMUM_LEVEL_RE = re.compile(r'^\s{2}minimum_level:\s*"(E[0-6])"\s*$', re.MULTILINE)
REALITY_REQUIRED_RE = re.compile(r'^\s{2}reality_required:\s*(true|false)\s*$', re.MULTILINE)
CANON_LESSON_RE = re.compile(r'^- \[[ xX]\] \*\*(\d+\.\d+)\*\* — ', re.MULTILINE)
CANON_LESSON_LINK_RE = re.compile(r'^- \[[ xX]\] \*\*(\d+\.\d+)\*\* — \[[^]]+\]\(([^)]+)\)', re.MULTILINE)
LESSON_FRONT_ID_RE = re.compile(r'^lesson_id:\s*"(\d+\.\d+)"\s*$', re.MULTILINE)
LESSON_STATUS_RE = re.compile(r'^status:\s*(planned|draft|ready)\s*$', re.MULTILINE)
CHAPTER_RE = re.compile(r'^### Chương\s+(\d+)\s+—', re.MULTILINE)
DECLARED_COUNTS_RE = re.compile(r'(?:Tổng cộng:\s*)?\*\*(\d+)\s+(?:phần|Parts?)\s*·\s*(\d+)\s+(?:chương|Chapters?)\s*·\s*(\d+)\s+(?:bài học|Lessons?|micro-lessons?)\*\*', re.IGNORECASE)
GO_DIRECTIVE_RE = re.compile(r'^go\s+(\d+\.\d+)\s*$', re.MULTILINE)
CURRENT_MISSION_RES = (
    re.compile(r'\|\s*Current Mission[^|]*\|\s*\*\*(M\d{2})\b', re.MULTILINE),
    re.compile(r'^Current Mission:\s*(M\d{2})\s*$', re.MULTILINE),
)

AUTHORITY_FILES = (
    Path("CURRICULUM.md"), Path("ROADMAP.md"), Path("BUILD-FIRST.md"),
    Path("docs/BUILD-FIRST-LEARNING-MODEL.md"), Path("docs/MISSION-AUTHORING-STANDARD.md"),
    Path("docs/MISSION-PASS-CRITERIA.md"), Path("docs/BOT-EVOLUTION-ROADMAP.md"),
    Path("docs/MISSION-KNOWLEDGE-MAP.md"), Path("docs/LANGUAGE-POLICY.md"),
)
LANGUAGE_AUTHORITY_DOCS = (Path("docs/CURRICULUM-CI.md"),)
READY_HEADINGS = (
    "## Ship Target", "## Starting Bot State", "## Try First", "## Run", "## Observe",
    "## Knowledge Pull", "## Improve", "## Tests", "## Reality Check", "## Operate",
    "## Failure Case", "## Safety Gate", "## Evidence", "## Explain-back",
    "## Mission PASS", "## Bot Version Result", "## Next Mission",
)
REFERENCE_BOOTSTRAP_FILES = (
    Path("lab/affiliate-bot/README.md"), Path("lab/affiliate-bot/go.mod"),
    Path("lab/affiliate-bot/cmd/bot/main.go"), Path("lab/affiliate-bot/data/sample-products.json"),
)
LEARNER_BOOTSTRAP_FILES = (
    Path("lab/learner/affiliate-bot/go.mod"), Path("lab/learner/affiliate-bot/README.md"),
    Path("lab/learner/affiliate-bot/cmd/bot/main.go"), Path("lab/learner/affiliate-bot/cmd/bot/main_test.go"),
    Path("lab/learner/affiliate-bot/internal/observation/observation.go"),
    Path("lab/learner/affiliate-bot/internal/decision/ranking.go"),
    Path("lab/learner/affiliate-bot/data/m00-missing-input.json"),
    Path("lab/learner/affiliate-bot/data/m00-conflicting-input.json"),
    Path("lab/learner/affiliate-bot/HINTS-M00.md"),
)
FORBIDDEN_BY_CURRENT_MISSION = {
    "M00": ("internal/ai", "internal/agent", "ActionIntent", "ApprovalRequest", "ExecutionRecord"),
    "M01": ("internal/ai", "internal/agent", "ActionIntent", "ApprovalRequest", "ExecutionRecord"),
    "M02": ("internal/ai", "internal/agent", "ActionIntent", "ApprovalRequest", "ExecutionRecord"),
    "M03": ("internal/agent", "ActionIntent", "ApprovalRequest", "ExecutionRecord"),
}

@dataclass(frozen=True)
class Problem:
    code: str
    path: str
    message: str
    def __str__(self) -> str:
        return f"{self.code} {self.path}: {self.message}"

def _front(text: str) -> str:
    if not text.startswith("---"): return ""
    end = text.find("---", 3)
    return text[: end + 3] if end != -1 else ""

def _list_ids(raw: str, prefix: str = "M") -> list[str]:
    return re.findall(rf'"({prefix}\d{{2}})"', raw or "")

def _version(raw: str | None) -> str | None:
    if not raw or raw == "null": return None
    return raw.strip('"')

def _version_tuple(version: str) -> tuple[int, int]:
    major, minor = version[1:].split(".", 1)
    return int(major), int(minor)

def canonical_lesson_ids(root: Path) -> set[str]:
    ids: set[str] = set()
    for path in sorted((root / "roadmap").glob("part-*.md")):
        ids.update(CANON_LESSON_RE.findall(path.read_text(encoding="utf-8")))
    return ids

def declared_counts(path: Path) -> tuple[int, int, int] | None:
    if not path.exists(): return None
    match = DECLARED_COUNTS_RE.search(path.read_text(encoding="utf-8"))
    return tuple(map(int, match.groups())) if match else None

def check_dynamic_inventory_authority(root: Path, problems: list[Problem]) -> None:
    curriculum = declared_counts(root / "CURRICULUM.md")
    roadmap = declared_counts(root / "ROADMAP.md")
    if curriculum is None: problems.append(Problem("BUILD015", "CURRICULUM.md", "không đọc được tổng Part/Chapter/Lesson động"))
    if roadmap is None: problems.append(Problem("BUILD015", "ROADMAP.md", "không đọc được tổng Part/Chapter/Lesson động"))
    if curriculum is None or roadmap is None: return
    if curriculum != roadmap:
        problems.append(Problem("BUILD015", "ROADMAP.md", f"tổng inventory lệch CURRICULUM: curriculum={curriculum}, roadmap={roadmap}")); return
    part_files = sorted((root / "roadmap").glob("part-*.md"))
    if not part_files: return
    chapters: list[str] = []; lessons: list[str] = []
    for path in part_files:
        text = path.read_text(encoding="utf-8")
        chapters.extend(CHAPTER_RE.findall(text)); lessons.extend(CANON_LESSON_RE.findall(text))
    actual = (len(part_files), len(chapters), len(lessons))
    if actual != curriculum: problems.append(Problem("BUILD015", "roadmap/", f"inventory thực tế {actual} không khớp authority {curriculum}"))

def roadmap_lesson_links(root: Path) -> dict[str, Path]:
    links: dict[str, Path] = {}
    for path in sorted((root / "roadmap").glob("part-*.md")):
        for lesson_id, raw in CANON_LESSON_LINK_RE.findall(path.read_text(encoding="utf-8")):
            links[lesson_id] = (path.parent / raw).resolve()
    return links

def ready_lesson_problem(root: Path, lesson_id: str, links: dict[str, Path]) -> str | None:
    path = links.get(lesson_id)
    if path is None: return f"required Lesson {lesson_id} phải có link active trong ROADMAP"
    if not path.is_file(): return f"required Lesson {lesson_id} link tới file không tồn tại"
    front = _front(path.read_text(encoding="utf-8"))
    id_match = LESSON_FRONT_ID_RE.search(front); status_match = LESSON_STATUS_RE.search(front)
    if not id_match or id_match.group(1) != lesson_id: return f"required Lesson {lesson_id} không khớp lesson_id trong file linked"
    if not status_match or status_match.group(1) != "ready": return f"required Lesson {lesson_id} phải status=ready; hiện là {status_match.group(1) if status_match else 'missing'}"
    return None

def check_authority(root: Path, problems: list[Problem]) -> None:
    for rel in AUTHORITY_FILES:
        path = root / rel
        if not path.exists(): problems.append(Problem("BUILD001", str(rel), "thiếu file authority bắt buộc của Build-First")); continue
        if re.search(r"Technical PASS|Evidence PASS", path.read_text(encoding="utf-8"), re.IGNORECASE):
            problems.append(Problem("BUILD018", str(rel), "active authority phải dùng Capability/Reality/Operated, không dùng PASS vocabulary cũ"))

def check_language_policy(root: Path, problems: list[Problem]) -> None:
    policy = root / "docs/LANGUAGE-POLICY.md"
    if policy.exists() and "Tiếng Việt là ngôn ngữ chính thức" not in policy.read_text(encoding="utf-8"):
        problems.append(Problem("LANG001", "docs/LANGUAGE-POLICY.md", "Language Policy phải xác định tiếng Việt là ngôn ngữ chính thức"))
    for rel in LANGUAGE_AUTHORITY_DOCS:
        path = root / rel
        if path.exists() and "LANGUAGE-POLICY.md" not in path.read_text(encoding="utf-8"):
            problems.append(Problem("LANG001", str(rel), "authority document phải tham chiếu docs/LANGUAGE-POLICY.md"))

def check_roadmap_spine(root: Path, problems: list[Problem]) -> dict[str, str]:
    path = root / "docs/BOT-EVOLUTION-ROADMAP.md"
    if not path.exists(): return {}
    rows = ROADMAP_MISSION_RE.findall(path.read_text(encoding="utf-8"))
    expected = [f"M{i:02d}" for i in range(12)]
    ids = [m for m, _ in rows]
    if ids != expected: problems.append(Problem("BUILD003", str(path.relative_to(root)), f"Mission spine phải đúng M00..M11 theo thứ tự; hiện có {ids}"))
    versions = [v for _, v in rows if v != "pre-bot"]
    for prev, current in zip(versions, versions[1:]):
        if _version_tuple(current) <= _version_tuple(prev): problems.append(Problem("BUILD006", str(path.relative_to(root)), f"Bot Version phải tăng; gặp {prev} rồi {current}"))
    for rel in (Path("CURRICULUM.md"), Path("ROADMAP.md")):
        authority = root / rel
        if authority.exists():
            found = TABLE_MISSION_RE.findall(authority.read_text(encoding="utf-8"))
            if found != expected: problems.append(Problem("BUILD003", str(rel), f"Mission table phải đúng M00..M11 theo thứ tự; hiện có {found}"))
    return dict(rows)

def require_semantic(text: str, patterns: tuple[str, ...], rel: str, message: str, problems: list[Problem]) -> None:
    if not all(re.search(p, text, re.IGNORECASE | re.DOTALL) for p in patterns): problems.append(Problem("BUILD017", rel, message))

def check_mission_semantics(mission_id: str, text: str, front: str, rel: str, problems: list[Problem]) -> None:
    if mission_id == "M00":
        actor = re.search(r'^\s{2}execution_actor:\s*"([^"]+)"\s*$', front, re.MULTILINE)
        side = re.search(r'^\s{2}external_side_effects:\s*(true|false)\s*$', front, re.MULTILINE)
        if not actor or actor.group(1) != "none" or not side or side.group(1) != "false": problems.append(Problem("BUILD017", rel, "M00 phải no external execution; legacy human_only manual market loop không còn là M00"))
        require_semantic(text, (r"public observations|E1", r"DecisionPacket", r"NO external execution|không.*external"), rel, "M00 phải có E1 public evidence + Human DecisionPacket, không external execution; disclosure/tracking thuộc action stage sau", problems)
    elif mission_id == "M01":
        require_semantic(text, (r"deterministic|tất định", r"RANK_SCENARIO", r"GET_MORE_DATA", r"HUMAN_REVIEW", r"no AI|không AI"), rel, "M01 phải là deterministic Bot với abstention và no AI/tool/action; analytics/export/outcome thật thuộc stage sau", problems)
    elif mission_id == "M02":
        require_semantic(text, (r"append-only", r"replay", r"provenance", r"freshness"), rel, "M02 phải có trustworthy append-only history, provenance/freshness và replay", problems)
    elif mission_id == "M03":
        actor = re.search(r'^\s{2}execution_actor:\s*"([^"]+)"\s*$', front, re.MULTILINE)
        side = re.search(r'^\s{2}external_side_effects:\s*(true|false)\s*$', front, re.MULTILINE)
        if not actor or actor.group(1) != "human_only" or not side or side.group(1) != "true": problems.append(Problem("BUILD017", rel, "M03 phải là first external side effect do human_only thực hiện"))
        require_semantic(text, (r"ActionRecord", r"tracking|measurement", r"outcome", r"human.*execute|human manual"), rel, "M03 phải có human action, tracking/measurement, ActionRecord và outcome context", problems)
    elif mission_id == "M04":
        require_semantic(text, (r"grounded|căn cứ", r"evidence refs?|tham chiếu bằng chứng", r"fallback|từ chối", r"(?:không|no).{0,100}(?:tool|write|publish|execution)"), rel, "M04 phải có grounded advisory, evidence refs, fallback và cấm tool/write/execute", problems)
    elif mission_id == "M05":
        require_semantic(text, (r"Outcome", r"Evaluation", r"ChangeProposal|change proposal", r"review|duyệt", r"rollback"), rel, "M05 phải nối Outcome→Evaluation→reviewed ChangeProposal và rollback", problems)

def _mission_files(root: Path) -> list[Path]:
    return sorted(p for p in (root / "missions").glob("M??-*.md")) if (root / "missions").exists() else []

def _roadmap_evidence_levels(root: Path) -> dict[str, str]:
    path = root / "ROADMAP.md"
    return dict(ROADMAP_EVIDENCE_RE.findall(path.read_text(encoding="utf-8"))) if path.exists() else {}

def check_missions(root: Path, lesson_ids: set[str], roadmap_versions: dict[str, str], problems: list[Problem]) -> None:
    files = _mission_files(root); authored: set[str] = set(); records = []
    for path in files:
        text = path.read_text(encoding="utf-8"); front = _front(text)
        cv = CURRICULUM_VERSION_RE.search(front)
        if cv and cv.group(1) != "2": continue
        mid = MISSION_ID_RE.search(front); status = STATUS_RE.search(front)
        if not mid or not status: continue
        mission_id = mid.group(1); authored.add(mission_id)
        req_match = REQUIRES_RE.search(front); required_match = REQUIRED_RE.search(front)
        requires = _list_ids(req_match.group(1) if req_match else "")
        required_lessons = LESSON_ID_RE.findall(required_match.group(1) if required_match else "")
        vf = VERSION_FROM_RE.search(front); vt = VERSION_TO_RE.search(front)
        records.append((path, text, front, mission_id, requires, required_lessons, _version(vf.group(1)) if vf else None, _version(vt.group(1)) if vt else None))
        for lid in required_lessons:
            if lid not in lesson_ids: problems.append(Problem("BUILD004", str(path.relative_to(root)), f"unknown knowledge.required Lesson {lid}"))
        if "lesson_pass" in front: problems.append(Problem("BUILD008", str(path.relative_to(root)), "Mission không được dùng lesson_pass làm PASS shortcut"))
        if status.group(1) == "ready":
            if not required_lessons: problems.append(Problem("BUILD004", str(path.relative_to(root)), "ready Mission phải khai báo knowledge.required rõ ràng"))
            for heading in READY_HEADINGS:
                if heading not in text: problems.append(Problem("BUILD007", str(path.relative_to(root)), f"ready Mission thiếu heading {heading}"))
            if mission_id == "M00" and "lab/learner/affiliate-bot/" not in text: problems.append(Problem("BUILD011", str(path.relative_to(root)), "bootstrap Mission ready phải name learner workspace"))
            links = roadmap_lesson_links(root)
            for lid in required_lessons:
                err = ready_lesson_problem(root, lid, links)
                if err: problems.append(Problem("BUILD016", str(path.relative_to(root)), err))
        check_mission_semantics(mission_id, text, front, str(path.relative_to(root)), problems)
    for path, text, front, mission_id, requires, required_lessons, version_from, version_to in records:
        current_num = int(mission_id[1:])
        for dep in requires:
            if int(dep[1:]) >= current_num: problems.append(Problem("BUILD005", str(path.relative_to(root)), f"forward/self dependency không hợp lệ: {dep}"))
            if dep not in authored: problems.append(Problem("BUILD005", str(path.relative_to(root)), f"dependency {dep} chưa có authored Mission"))
        if version_to and mission_id in roadmap_versions and roadmap_versions[mission_id] != "pre-bot" and roadmap_versions[mission_id] != version_to: problems.append(Problem("BUILD012", str(path.relative_to(root)), f"bot_version_to {version_to} lệch roadmap {roadmap_versions[mission_id]}"))
        if requires and version_from:
            concrete = [roadmap_versions.get(dep) for dep in requires if roadmap_versions.get(dep) and roadmap_versions.get(dep) != "pre-bot"]
            if concrete and version_from not in concrete: problems.append(Problem("BUILD012", str(path.relative_to(root)), f"bot_version_from {version_from} không tiếp tục dependency version {concrete}"))
        minimum = MINIMUM_LEVEL_RE.search(front); reality = REALITY_REQUIRED_RE.search(front); roadmap_level = _roadmap_evidence_levels(root).get(mission_id)
        if roadmap_level and minimum:
            expected = roadmap_level.split("→")[-1]
            if minimum.group(1) != expected and mission_id not in {"M01", "M02", "M09"}: problems.append(Problem("BUILD016", str(path.relative_to(root)), f"minimum_level phải là {expected} theo ROADMAP"))
        if roadmap_level and roadmap_level != "E0" and reality and reality.group(1) != "true": problems.append(Problem("BUILD016", str(path.relative_to(root)), "reality_required: true cho Mission có real evidence gate"))

def _current_mission(root: Path) -> str | None:
    path = root / "PROGRESS.md"
    if not path.exists(): return None
    text = path.read_text(encoding="utf-8")
    for pattern in CURRENT_MISSION_RES:
        m = pattern.search(text)
        if m: return m.group(1)
    return None

def check_bootstrap(root: Path, problems: list[Problem]) -> None:
    for rel in REFERENCE_BOOTSTRAP_FILES + LEARNER_BOOTSTRAP_FILES:
        if not (root / rel).exists(): problems.append(Problem("BUILD010", str(rel), "thiếu bootstrap/reference file"))
    ref_mod = root / "lab/affiliate-bot/go.mod"; learner_mod = root / "lab/learner/affiliate-bot/go.mod"
    if ref_mod.exists() and learner_mod.exists():
        r = GO_DIRECTIVE_RE.search(ref_mod.read_text(encoding="utf-8")); l = GO_DIRECTIVE_RE.search(learner_mod.read_text(encoding="utf-8"))
        if r and l and r.group(1) != l.group(1): problems.append(Problem("BUILD014", "lab/learner/affiliate-bot/go.mod", "learner/reference Go directive phải khớp"))
    ref_readme = root / "lab/affiliate-bot/README.md"
    if ref_readme.exists() and re.search(r"bootstrap Missions? M00-M03|current M02-M03", ref_readme.read_text(encoding="utf-8"), re.I): problems.append(Problem("BUILD020", str(ref_readme.relative_to(root)), "legacy reference không được claim current M02/M03 mapping"))
    obs = root / "lab/learner/affiliate-bot/internal/observation/observation.go"
    if obs.exists() and re.search(r'\bPrice\s+float64\b|\bCommissionRate\s+float64\b', obs.read_text(encoding="utf-8")): problems.append(Problem("BUILD019", str(obs.relative_to(root)), "missing numeric evidence phải nullable"))
    missing_fixture = root / "lab/learner/affiliate-bot/data/m00-missing-input.json"
    if missing_fixture.exists():
        try:
            data = json.loads(missing_fixture.read_text(encoding="utf-8")); rows = data if isinstance(data, list) else [data]
            if any(isinstance(x, dict) and x.get("evidence_kind") == "real" for x in rows): problems.append(Problem("BUILD019", str(missing_fixture.relative_to(root)), "failure fixture không được giả nhãn real"))
        except json.JSONDecodeError: pass
    current = _current_mission(root)
    if current in FORBIDDEN_BY_CURRENT_MISSION:
        learner_root = root / "lab/learner/affiliate-bot"
        if learner_root.exists():
            text = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in learner_root.rglob("*.go"))
            for marker in FORBIDDEN_BY_CURRENT_MISSION[current]:
                if marker in text: problems.append(Problem("BUILD011", "lab/learner/affiliate-bot", f"capability ceiling leak ở {current}: {marker}"))

def validate(root: Path) -> list[Problem]:
    problems: list[Problem] = []
    check_authority(root, problems); check_language_policy(root, problems); check_dynamic_inventory_authority(root, problems)
    versions = check_roadmap_spine(root, problems); check_missions(root, canonical_lesson_ids(root), versions, problems); check_bootstrap(root, problems)
    return problems

def main() -> int:
    root = Path(__file__).resolve().parents[1]; problems = validate(root)
    if problems:
        for problem in problems: print(problem)
        print(f"Build-First validation failed with {len(problems)} problem(s)."); return 1
    print("Build-First validation passed: mission spine, evidence/authority gates and bootstrap safety are consistent."); return 0

if __name__ == "__main__": sys.exit(main())
