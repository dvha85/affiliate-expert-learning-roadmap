#!/usr/bin/env python3
"""Validate Hybrid Go-core / n8n / AgentRuntime ownership and maturity invariants."""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Problem:
    code: str
    path: str
    message: str

    def __str__(self) -> str:
        return f"{self.code} {self.path}: {self.message}"


def read(root: Path, rel: str) -> str:
    path = root / rel
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def require_markers(root: Path, rel: str, code: str, markers: tuple[str, ...], problems: list[Problem]) -> None:
    text = read(root, rel)
    if not text:
        problems.append(Problem(code, rel, "required file is missing or empty"))
        return
    for marker in markers:
        if marker not in text:
            problems.append(Problem(code, rel, f"missing hybrid invariant marker: {marker}"))


def reject_patterns(root: Path, rel: str, code: str, patterns: tuple[str, ...], problems: list[Problem]) -> None:
    text = read(root, rel)
    if not text:
        return
    for pattern in patterns:
        if re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
            problems.append(Problem(code, rel, f"forbidden authority-drift pattern matched: {pattern}"))


def check_adr(root: Path, problems: list[Problem]) -> None:
    require_markers(root, "docs/ADR-003-HYBRID-GO-N8N-AGENT-RUNTIME.md", "HYB001", (
        "GO CORE FIRST", "Go Domain / Governance Core", "n8n Orchestration Reference",
        "Agent Runtime Intelligence Layer", "Go decides what is true / allowed.",
        "Agent investigates / reasons / proposes.", "n8n coordinates when / where / how workflows run.",
        "Go Policy unavailable\n→ no consequential execution",
    ), problems)
    require_markers(root, "docs/ADR-001-GO-FIRST-BOT-STACK.md", "HYB002", (
        "runtime ownership superseded by ADR-003",
        "PRIMARY DOMAIN / GOVERNANCE IMPLEMENTATION LANGUAGE = Go",
        "Go owns every runtime concern",
    ), problems)


def check_roadmap_maturity(root: Path, problems: list[Problem]) -> None:
    require_markers(root, "ROADMAP.md", "HYB003", (
        "DOMAIN / GOVERNANCE", "AUTOMATION / ORCHESTRATION", "INTELLIGENCE / AGENT",
        "M04 read-only import learning slice", "M06 reliable orchestration", "M08 read-only tools",
        "M09 propose ActionIntent", "M10 governed participation",
    ), problems)


def check_no_early_runtime_adoption(root: Path, problems: list[Problem]) -> None:
    early_paths = (
        "roadmap/part-00.md", "roadmap/part-01.md",
        "missions/M00-first-evidence-backed-decision.md", "missions/M01-trustworthy-history.md",
        "missions/M02-grounded-ai-advisor.md", "missions/M03-first-tracked-manual-publish.md",
    )
    for rel in early_paths:
        text = read(root, rel)
        for marker in ("n8n", "Hermes Agent"):
            if marker in text:
                problems.append(Problem("HYB004", rel, f"concrete runtime {marker!r} must not be adopted in M00-M03/Part00-01"))


def check_part02_boundary(root: Path, problems: list[Problem]) -> None:
    require_markers(root, "roadmap/part-02.md", "HYB005", (
        "First orchestration learning slice — M04", "manual trigger", "n8n read-only/import workflow",
        "Go validate + reconcile", "không có external mutation", "Human\n= actor duy nhất được publish",
    ), problems)


def check_part04_ownership(root: Path, problems: list[Problem]) -> None:
    require_markers(root, "roadmap/part-04.md", "HYB006", (
        "n8n\n= primary watcher/orchestration reference", "Go creates/validates DecisionPacket",
        "n8n routes DecisionPacket", "Go Policy owns final state",
        "Go validation/policy unavailable\n→ no consequential downstream execution",
    ), problems)


def check_part05_governance(root: Path, problems: list[Problem]) -> None:
    require_markers(root, "roadmap/part-05.md", "HYB007", (
        "AgentRuntime\n= investigate + read-only tool use + propose",
        "Go\n= Tool Registry contract + validation + ActionIntent + deterministic risk/policy + authorization",
        "n8n\n= invoke/route Agent + shadow workflow + durable approval routing + bounded execution",
        "Hermes Agent là **primary Agent runtime reference/candidate**", "CandidateEvidence\n→ Go validate / ground",
        "n8n IF/Switch node không được tự reclassify `RISK2` thành auto-executable",
        "kill switch ON\n→ execution blocked even with prior approval",
    ), problems)


def check_part06_fail_safe(root: Path, problems: list[Problem]) -> None:
    require_markers(root, "roadmap/part-06.md", "HYB008", (
        "Agent unavailable\n≠ core deterministic decision unavailable",
        "n8n unavailable\n≠ canonical evidence/history corrupted",
        "Go Policy unavailable\n→ no consequential execution",
        "Correlation ID phải survive cross-runtime boundaries", "kill switch ON\n→ NO EXECUTION",
    ), problems)


def check_reference_replaceability(root: Path, problems: list[Problem]) -> None:
    require_markers(root, "docs/TECHNOLOGY-CANDIDATES.md", "HYB009", (
        "n8n\n= primary orchestration reference", "AgentRuntime\n= intelligence role",
        "Hermes Agent\n= primary reference/candidate implementation",
        "n8n | Không; contract/behavior mới là gate", "Hermes Agent candidate/reference | Không",
    ), problems)


def check_runtime_hardening(root: Path, problems: list[Problem]) -> None:
    require_markers(root, "docs/AGENT-RUNTIME-STANDARD.md", "HYB010", (
        "untrusted intelligence worker", "AGENT SAFE PROFILE — M08", "ALLOWLIST ONLY",
        "Self-modification / skill mutation:\nDENY", "UNTRUSTED UNTIL GO VALIDATION",
        "Canonical state ownership:\nNEVER AGENT-OWNED",
    ), problems)
    require_markers(root, "docs/AGENT-HITL-RUNTIME.md", "HYB011", (
        "n8n execution state/history\n≠ canonical Action / Approval / Execution state",
        "persist ApprovalDecision", "persist ExecutionRecord",
        "không được là nguồn duy nhất", "canonical persisted state",
    ), problems)
    require_markers(root, "docs/N8N-ORCHESTRATION-STANDARD.md", "HYB012", (
        "Workflow-as-code baseline", "Git repo là portable baseline", "Operational security gate từ M06",
        "n8n audit", "public webhook\n→ n8n IF/Switch\n→ consequential action",
        "Git owns reviewable workflow artifacts.",
    ), problems)


def check_negative_authority_drift(root: Path, problems: list[Problem]) -> None:
    paths = (
        "ROADMAP.md", "roadmap/part-04.md", "roadmap/part-05.md", "roadmap/part-06.md",
        "docs/ADR-003-HYBRID-GO-N8N-AGENT-RUNTIME.md", "docs/AGENT-RUNTIME-STANDARD.md",
        "docs/AGENT-HITL-RUNTIME.md", "docs/N8N-ORCHESTRATION-STANDARD.md",
    )
    forbidden = (
        r"n8n\s+(owns|is)\s+(the\s+)?(final\s+)?(risk|policy|authorization)",
        r"agent\s+(owns|decides)\s+(the\s+)?(final\s+)?(risk|policy|authorization)",
        r"agent\s+(confidence|proposal).*→\s*(direct\s+)?(execute|execution)",
        r"n8n\s+execution\s+(state|history)\s*=\s*canonical",
        r"workflow\s+(state|history)\s*=\s*(the\s+)?source\s+of\s+truth",
        r"agent\s+tool\s+result\s*→\s*(canonical|measured)\s+(evidence|fact)",
    )
    for rel in paths:
        reject_patterns(root, rel, "HYB013", forbidden, problems)


def check_readme_status_source(root: Path, problems: list[Problem]) -> None:
    require_markers(root, "README.md", "HYB014", (
        "canonical learner-state source", "canonical authoring-state source",
        "README không phải nguồn chuẩn của tiến độ người học",
    ), problems)
    reject_patterns(root, "README.md", "HYB014", (r"Người học chưa bắt đầu",), problems)


def validate(root: Path) -> list[Problem]:
    problems: list[Problem] = []
    check_adr(root, problems)
    check_roadmap_maturity(root, problems)
    check_no_early_runtime_adoption(root, problems)
    check_part02_boundary(root, problems)
    check_part04_ownership(root, problems)
    check_part05_governance(root, problems)
    check_part06_fail_safe(root, problems)
    check_reference_replaceability(root, problems)
    check_runtime_hardening(root, problems)
    check_negative_authority_drift(root, problems)
    check_readme_status_source(root, problems)
    return problems


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    problems = validate(root)
    if problems:
        for problem in problems:
            print(problem)
        print(f"Hybrid runtime validation failed with {len(problems)} problem(s).")
        return 1
    print("Hybrid runtime validation passed: ownership, state separation, Agent sandbox, n8n security/versioning and negative authority guards are consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
