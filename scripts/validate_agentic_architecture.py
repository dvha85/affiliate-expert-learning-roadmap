#!/usr/bin/env python3
"""Validate Agentic Decision Intelligence v1 architecture invariants.

Standard-library only. This validator protects the AI/Agent execution layer without
redefining canonical curriculum counts, learner PASS, or provider-specific choices.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

MISSION_ROW_RE = re.compile(r"^\|\s*(M\d{2})\s*\|(.+)$", re.MULTILINE)

REQUIRED_AUTHORITY_FILES = (
    Path("docs/AI-AGENT-DECISION-ARCHITECTURE.md"),
    Path("docs/AI-CAPABILITY-LEVELS.md"),
    Path("docs/DECISION-CONTRACTS.md"),
    Path("docs/AI-PROVIDER-CAPABILITY-MATRIX.md"),
    Path("docs/AI-ADVISORY-PATTERNS.md"),
    Path("docs/AI-EARLY-MISSION-MAP.md"),
    Path("docs/DECISION-INTELLIGENCE-STANDARD.md"),
    Path("docs/CONFIDENCE-AND-UNCERTAINTY.md"),
    Path("docs/MODEL-ROUTING-STANDARD.md"),
    Path("docs/DATA-FRESHNESS-FOR-DECISIONS.md"),
    Path("docs/TOOL-REGISTRY-STANDARD.md"),
    Path("docs/AGENT-RUNTIME-STANDARD.md"),
    Path("docs/PROGRAMMATIC-TOOL-ORCHESTRATION.md"),
    Path("docs/MCP-2026-OPERATING-NOTES.md"),
    Path("docs/AGENT-EVALUATION-STANDARD.md"),
    Path("docs/DECISION-OUTCOME-MEMORY.md"),
    Path("docs/AGENT-HITL-RUNTIME.md"),
)

EXPECTED_LEVELS = {
    "M00": "A0",
    "M01": "A0",
    "M02": "A0",
    "M03": "A0",
    "M04": "A1",
    "M05": "A1",
    "M06": "A0 core + A1 triage",
    "M07": "A1",
    "M08": "A2-RO",
    "M09": "A3-shadow",
    "M10": "A3-limited",
    "M11": "A3-production",
}


@dataclass(frozen=True)
class Problem:
    code: str
    path: str
    message: str

    def __str__(self) -> str:
        return f"{self.code} {self.path}: {self.message}"


def read(root: Path, rel: Path) -> str:
    path = root / rel
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def require_markers(
    root: Path,
    rel: Path,
    code: str,
    markers: tuple[str, ...],
    problems: list[Problem],
) -> None:
    text = read(root, rel)
    if not text:
        problems.append(Problem(code, str(rel), "required file is missing or empty"))
        return
    for marker in markers:
        if marker not in text:
            problems.append(Problem(code, str(rel), f"missing required marker: {marker}"))


def check_authority(root: Path, problems: list[Problem]) -> None:
    for rel in REQUIRED_AUTHORITY_FILES:
        if not (root / rel).exists():
            problems.append(Problem("AI001", str(rel), "required Agentic Decision Intelligence authority file is missing"))


def capability_rows(text: str) -> dict[str, str]:
    """Read the last cell of each Mission row in the evolution table.

    The table gained Part/reality columns in the outcome-driven curriculum, so
    the AI column must not be located by a fixed numeric index.
    """
    rows: dict[str, str] = {}
    for match in MISSION_ROW_RE.finditer(text):
        mission = match.group(1)
        cells = [cell.strip() for cell in match.group(2).split("|")]
        if cells and cells[-1] == "":
            cells.pop()
        # Only the product-spine table has Bot version as its first remaining
        # cell. Later reality/safety tables may legitimately reuse Mission IDs.
        if cells and re.fullmatch(r"(?:v\d+\.\d+|pre-bot)", cells[0]):
            rows[mission] = cells[-1]
    return rows


def level_matches(mission: str, value: str) -> bool:
    expected = EXPECTED_LEVELS[mission]
    normalized = re.sub(r"\s+", " ", value.strip())
    if mission == "M06":
        return bool(re.match(r"^A0\s+core\s*\+\s*A1\s+triage(?:\b|$)", normalized, re.IGNORECASE))
    if expected in {"A0", "A1"}:
        # Descriptors such as "A1 advisory; human execute" are informative and
        # allowed, but another capability token later in the cell is not.
        return bool(re.match(rf"^{re.escape(expected)}(?:\b|$)", normalized)) and not re.search(
            rf"\bA(?!{expected[1]}\b)[0-4](?:-[A-Za-z]+)?\b", normalized
        )
    return bool(re.match(rf"^{re.escape(expected)}(?:\b|$)", normalized, re.IGNORECASE))


def check_capability_levels(root: Path, problems: list[Problem]) -> None:
    rel = Path("docs/BOT-EVOLUTION-ROADMAP.md")
    text = read(root, rel)
    rows = capability_rows(text)
    if set(rows) != set(EXPECTED_LEVELS):
        problems.append(
            Problem(
                "AI002",
                str(rel),
                f"AI level table must cover exactly M00..M11; found {sorted(rows)}",
            )
        )
        return
    for mission, expected in EXPECTED_LEVELS.items():
        if not level_matches(mission, rows[mission]):
            problems.append(
                Problem(
                    "AI002",
                    str(rel),
                    f"{mission} AI level must be {expected}; found {rows[mission]}",
                )
            )


def check_decision_contract(root: Path, problems: list[Problem]) -> None:
    require_markers(
        root,
        Path("docs/DECISION-CONTRACTS.md"),
        "AI003",
        (
            "DecisionPacket",
            "evidence_refs",
            "confidence",
            "uncertainty",
            "missing_evidence",
            "freshness",
            "expires_at",
            "risk_level",
            "policy_decision",
            "ActionIntent **không** đồng nghĩa execution permission",
            "Execution Record",
        ),
        problems,
    )


def check_tool_governance(root: Path, problems: list[Problem]) -> None:
    rel = Path("docs/TOOL-REGISTRY-STANDARD.md")
    require_markers(
        root,
        rel,
        "AI004",
        (
            "EXTERNAL_SIDE_EFFECT",
            "ActionIntent",
            "Policy/Risk",
            "approval",
        ),
        problems,
    )
    require_markers(
        root,
        rel,
        "AI005",
        (
            "permission:",
            "risk_ceiling:",
            "requires_approval:",
            "audit_fields:",
        ),
        problems,
    )


def check_untrusted_boundary(root: Path, problems: list[Problem]) -> None:
    require_markers(
        root,
        Path("docs/AI-AGENT-DECISION-ARCHITECTURE.md"),
        "AI006",
        (
            "MODEL OUTPUT = UNTRUSTED INPUT",
            "DECISION ≠ EXECUTION",
            "AI ADVICE ≠ EXECUTION AUTHORITY",
            "POLICY BEFORE CONSEQUENTIAL ACTION",
        ),
        problems,
    )


def check_evaluation(root: Path, problems: list[Problem]) -> None:
    require_markers(
        root,
        Path("docs/AGENT-EVALUATION-STANDARD.md"),
        "AI007",
        (
            "task_success",
            "tool_selection_accuracy",
            "tool_argument_accuracy",
            "unsupported_claim_rate",
            "policy_block_accuracy",
            "confidence_calibration",
            "decision_latency",
            "cost_per_decision",
            "human intervention rate",
        ),
        problems,
    )


def _section(text: str, heading: str) -> str:
    start = text.find(heading)
    if start < 0:
        return ""
    next_heading = text.find("\n## ", start + len(heading))
    return text[start:] if next_heading < 0 else text[start:next_heading]


def check_freshness(root: Path, problems: list[Problem]) -> None:
    require_markers(
        root,
        Path("docs/MCP-2026-OPERATING-NOTES.md"),
        "AI008",
        ("**Verified:**", "**Volatility:**", "freshness/implementation note"),
        problems,
    )

    rel = Path("docs/BOT-ENGINEERING-REFRESH-2026.08.md")
    text = read(root, rel)
    for source_id in (
        "## EXT:MCP:2026-07-28",
        "## EXT:AGENT:TOOL-SEARCH-PROGRAMMATIC",
        "## EXT:AGENT:DURABLE-HITL",
    ):
        section = _section(text, source_id)
        if not section:
            problems.append(Problem("AI008", str(rel), f"missing volatile source section: {source_id}"))
            continue
        for marker in ("**Source:**", "**URL:**", "**Verified:**", "**Volatility:**"):
            if marker not in section:
                problems.append(Problem("AI008", str(rel), f"{source_id} missing freshness marker: {marker}"))


def check_provider_neutrality(root: Path, problems: list[Problem]) -> None:
    require_markers(
        root,
        Path("docs/AI-PROVIDER-CAPABILITY-MATRIX.md"),
        "AI009",
        (
            "không được phụ thuộc trực tiếp vào một provider SDK",
            "AI Provider Interface",
            "Provider Adapter(s)",
            "Exact provider/model mapping nằm config/freshness layer",
        ),
        problems,
    )


def check_multi_agent_boundary(root: Path, problems: list[Problem]) -> None:
    require_markers(
        root,
        Path("docs/AI-CAPABILITY-LEVELS.md"),
        "AI010",
        (
            "A4 — Multi-Agent Optional Advanced",
            "sau M11",
            "không phải core Mission",
        ),
        problems,
    )
    # The exact M00-M11 mapping is independently protected by AI002. A4 must
    # not be assigned to any Core row; it is only an optional post-M11 module.
    evolution_rel = Path("docs/BOT-EVOLUTION-ROADMAP.md")
    evolution = read(root, evolution_rel)
    rows = capability_rows(evolution)
    if any(re.search(r"\bA4\b", level) for level in rows.values()):
        problems.append(Problem("AI010", str(evolution_rel), "A4 must not be assigned to a Core Mission"))
    if "advanced option sau khi M11" not in evolution:
        problems.append(Problem("AI010", str(evolution_rel), "A4/multi-agent must remain optional advanced work after M11"))


def check_outcome_learning(root: Path, problems: list[Problem]) -> None:
    require_markers(
        root,
        Path("docs/DECISION-OUTCOME-MEMORY.md"),
        "AI011",
        (
            "Decision\n→ Action\n→ Outcome\n→ Evaluation\n→ Proposed Improvement\n→ Offline Test / Experiment\n→ Review\n→ Deploy",
            "Policy authority không được tự sửa",
            "không tự rewrite production policy/prompt/weights",
        ),
        problems,
    )


def check_programmatic_orchestration(root: Path, problems: list[Problem]) -> None:
    require_markers(
        root,
        Path("docs/PROGRAMMATIC-TOOL-ORCHESTRATION.md"),
        "AI012",
        (
            "READ_ONLY",
            "Không cho free orchestration",
            "publish;",
            "spend;",
            "account/security change;",
            "destructive delete;",
            "allowlisted tools",
        ),
        problems,
    )


def validate(root: Path) -> list[Problem]:
    problems: list[Problem] = []
    check_authority(root, problems)
    check_capability_levels(root, problems)
    check_decision_contract(root, problems)
    check_tool_governance(root, problems)
    check_untrusted_boundary(root, problems)
    check_evaluation(root, problems)
    check_freshness(root, problems)
    check_provider_neutrality(root, problems)
    check_multi_agent_boundary(root, problems)
    check_outcome_learning(root, problems)
    check_programmatic_orchestration(root, problems)
    return problems


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    problems = validate(root)
    if problems:
        for problem in problems:
            print(problem)
        print(f"Agentic architecture validation failed with {len(problems)} problem(s).")
        return 1
    print("Agentic architecture validation passed: M00-M11 AI levels and decision/tool/HITL/evaluation boundaries are consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
