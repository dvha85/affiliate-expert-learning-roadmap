#!/usr/bin/env python3
"""Validate current deterministic-core / n8n / AgentRuntime architecture invariants."""
from __future__ import annotations

import re
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
    return path.read_text(encoding="utf-8") if path.exists() else ""


def require(root: Path, rel: str, code: str, markers: tuple[str, ...], problems: list[Problem]) -> None:
    text = read(root, rel)
    if not text:
        problems.append(Problem(code, rel, "required file is missing or empty"))
        return
    for marker in markers:
        if marker not in text:
            problems.append(Problem(code, rel, f"missing architecture marker: {marker}"))


def reject(root: Path, rel: str, code: str, patterns: tuple[str, ...], problems: list[Problem]) -> None:
    text = read(root, rel)
    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE | re.MULTILINE):
            problems.append(Problem(code, rel, f"forbidden architecture drift: {pattern}"))


def check_architecture_authority(root: Path, problems: list[Problem]) -> None:
    require(root, "docs/ADR-004-DETERMINISTIC-CORE-IMPLEMENTATION-FLEXIBILITY.md", "HYB001", (
        "DETERMINISTIC CORE FIRST",
        "Deterministic Domain / Governance Core",
        "Deterministic Core decides what is true / allowed.",
        "NO-CODE WHEN IT IS AUDITABLE",
        "n8n AI Agent",
        "DecisionRules",
        "Development Agent",
        "Deterministic Policy Authority unavailable / invalid / unverified\n→ no consequential execution",
    ), problems)
    require(root, "docs/ADR-003-HYBRID-GO-N8N-AGENT-RUNTIME.md", "HYB002", (
        "GO CORE FIRST", "n8n Orchestration Reference", "Agent Runtime Intelligence Layer",
    ), problems)


def check_implementation_strategy(root: Path, problems: list[Problem]) -> None:
    require(root, "docs/IMPLEMENTATION-STRATEGY.md", "HYB003", (
        "DETERMINISTIC CORE FIRST",
        "Profile A — Visual/no-code deterministic core",
        "Profile B — Go deterministic core",
        "Profile C — Agent-maintained code",
        "golden oracle/reference implementation",
    ), problems)


def check_roadmap_maturity(root: Path, problems: list[Problem]) -> None:
    require(root, "ROADMAP.md", "HYB004", (
        "DETERMINISTIC CORE FIRST ≠ CODE FIRST", "M00 | first safe market loop",
        "M01 | first outcome snapshot", "M02 | smallest deterministic Bot",
        "M04 | grounded AI advisor", "A1 advisory, no tools/write",
        "M08 | read-only evidence agent", "M09 | shadow action + approval",
        "M10 | bounded governed canary", "Development Agent",
    ), problems)


def check_no_early_runtime_adoption(root: Path, problems: list[Problem]) -> None:
    early_paths = (
        "roadmap/part-00.md", "roadmap/part-01.md",
        "missions/M00-first-evidence-backed-decision.md", "missions/M01-trustworthy-history.md",
        "missions/M02-grounded-ai-advisor.md", "missions/M03-first-tracked-manual-publish.md",
    )
    for rel in early_paths:
        text = read(root, rel)
        for marker in ("n8n", "Hermes Agent", "DecisionRules"):
            if marker in text:
                problems.append(Problem("HYB005", rel, f"concrete runtime {marker!r} adopted too early"))


def check_part02_boundary(root: Path, problems: list[Problem]) -> None:
    require(root, "roadmap/part-02.md", "HYB006", (
        "First orchestration learning slice — M04", "manual trigger", "n8n read-only/import workflow",
        "Deterministic Core validate + reconcile", "Human\n= actor duy nhất được publish",
    ), problems)


def check_part04_ownership(root: Path, problems: list[Problem]) -> None:
    require(root, "roadmap/part-04.md", "HYB007", (
        "n8n\n= primary watcher/orchestration reference",
        "Deterministic Core creates/validates DecisionPacket",
        "n8n routes DecisionPacket",
        "Deterministic Policy Authority owns final state",
        "first meaningful visual-rule comparison",
        "Deterministic Policy Authority unavailable / invalid / unverified\n→ no consequential downstream execution",
    ), problems)


def check_part05_governance(root: Path, problems: list[Problem]) -> None:
    require(root, "roadmap/part-05.md", "HYB008", (
        "AgentRuntime\n= investigate + read-only tool use + propose",
        "n8n AI Agent là visual-first candidate ở M08",
        "Deterministic Core\n= Tool Registry contract + validation + ActionIntent + deterministic risk/policy + authorization",
        "CandidateEvidence\n→ Deterministic Core validate / ground",
        "n8n IF/Switch node không được tự reclassify `RISK2` thành auto-executable",
        "Hermes/OpenAI Agents SDK comparison",
        "kill switch ON\n→ execution blocked even with prior approval",
    ), problems)


def check_part06_fail_safe(root: Path, problems: list[Problem]) -> None:
    require(root, "roadmap/part-06.md", "HYB009", (
        "Agent unavailable\n≠ core deterministic decision unavailable",
        "n8n unavailable\n≠ canonical evidence/history corrupted",
        "Deterministic Policy Authority unavailable / invalid / unverified\n→ no consequential execution",
        "rule runtime error / stale rule / unknown active version\n→ fail closed",
        "Correlation ID phải survive cross-runtime boundaries",
        "kill switch ON\n→ NO EXECUTION",
    ), problems)


def check_reference_replaceability(root: Path, problems: list[Problem]) -> None:
    require(root, "docs/TECHNOLOGY-CANDIDATES.md", "HYB010", (
        "Go\n= deterministic core reference/fallback implementation",
        "DecisionRules\n= visual deterministic rule-engine candidate",
        "n8n AI Agent visual-first candidate",
        "GitHub Copilot cloud agent",
        "OpenAI Codex coding agent",
        "Anthropic Claude coding agent",
        "Flowise — watchlist/comparison only",
    ), problems)


def check_runtime_hardening(root: Path, problems: list[Problem]) -> None:
    require(root, "docs/AGENT-RUNTIME-STANDARD.md", "HYB011", (
        "untrusted intelligence worker", "AGENT SAFE PROFILE — M08", "ALLOWLIST ONLY",
        "Self-modification / skill mutation:\nDENY", "UNTRUSTED UNTIL DETERMINISTIC VALIDATION",
        "Canonical state ownership:\nNEVER AGENT-OWNED",
    ), problems)
    require(root, "docs/AGENT-HITL-RUNTIME.md", "HYB012", (
        "n8n execution state/history\n≠ canonical Action / Approval / Execution state",
        "persist ApprovalDecision", "persist ExecutionRecord", "canonical persisted state",
    ), problems)


def check_negative_authority_drift(root: Path, problems: list[Problem]) -> None:
    paths = (
        "ROADMAP.md", "roadmap/part-04.md", "roadmap/part-05.md", "roadmap/part-06.md",
        "docs/ADR-004-DETERMINISTIC-CORE-IMPLEMENTATION-FLEXIBILITY.md", "docs/AGENT-RUNTIME-STANDARD.md",
    )
    forbidden = (
        r"n8n\s+(owns|is)\s+(the\s+)?(final\s+)?(risk|policy|authorization)",
        r"agent\s+(owns|decides)\s+(the\s+)?(final\s+)?(risk|policy|authorization)",
        r"agent\s+(confidence|proposal).*→\s*(direct\s+)?(execute|execution)",
        r"workflow\s+(state|history)\s*=\s*(the\s+)?source\s+of\s+truth",
    )
    for rel in paths:
        reject(root, rel, "HYB013", forbidden, problems)
    for rel in ("ROADMAP.md", "roadmap/part-04.md", "roadmap/part-05.md", "roadmap/part-06.md"):
        reject(root, rel, "HYB014", (
            r"Go decides what is true / allowed\.",
            r"Go Policy unavailable\s*\n?\s*→ no consequential execution",
        ), problems)


def check_readme_status_source(root: Path, problems: list[Problem]) -> None:
    require(root, "README.md", "HYB015", (
        "canonical learner-state source", "canonical authoring-state source",
        "README không phải nguồn chuẩn của tiến độ người học", "DETERMINISTIC CORE FIRST",
        "DecisionRules", "Development Agent",
    ), problems)
    reject(root, "README.md", "HYB015", (r"Người học chưa bắt đầu",), problems)


def validate(root: Path) -> list[Problem]:
    problems: list[Problem] = []
    check_architecture_authority(root, problems)
    check_implementation_strategy(root, problems)
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
