#!/usr/bin/env python3
"""Validate Hybrid Go-core / n8n / AgentRuntime ownership and maturity invariants.

This validator protects runtime ownership introduced by ADR-003 without making
n8n or Hermes mandatory implementation dependencies.
"""
from __future__ import annotations

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


def check_adr(root: Path, problems: list[Problem]) -> None:
    require_markers(
        root,
        "docs/ADR-003-HYBRID-GO-N8N-AGENT-RUNTIME.md",
        "HYB001",
        (
            "GO CORE FIRST",
            "Go Domain / Governance Core",
            "n8n Orchestration Reference",
            "Agent Runtime Intelligence Layer",
            "Go decides what is true / allowed.",
            "Agent investigates / reasons / proposes.",
            "n8n coordinates when / where / how workflows run.",
            "Go Policy unavailable\n→ no consequential execution",
        ),
        problems,
    )
    require_markers(
        root,
        "docs/ADR-001-GO-FIRST-BOT-STACK.md",
        "HYB002",
        (
            "runtime ownership superseded by ADR-003",
            "PRIMARY DOMAIN / GOVERNANCE IMPLEMENTATION LANGUAGE = Go",
            "Go owns every runtime concern",
        ),
        problems,
    )


def check_roadmap_maturity(root: Path, problems: list[Problem]) -> None:
    require_markers(
        root,
        "ROADMAP.md",
        "HYB003",
        (
            "DOMAIN / GOVERNANCE",
            "AUTOMATION / ORCHESTRATION",
            "INTELLIGENCE / AGENT",
            "M04 read-only import learning slice",
            "M06 reliable orchestration",
            "M08 read-only tools",
            "M09 propose ActionIntent",
            "M10 governed participation",
        ),
        problems,
    )


def check_no_early_runtime_adoption(root: Path, problems: list[Problem]) -> None:
    # Early Missions teach evidence/history/grounded advisory. Referencing these
    # concrete runtimes here would pull implementation complexity/authority too early.
    early_paths = (
        "roadmap/part-00.md",
        "roadmap/part-01.md",
        "missions/M00-first-evidence-backed-decision.md",
        "missions/M01-trustworthy-history.md",
        "missions/M02-grounded-ai-advisor.md",
        "missions/M03-first-tracked-manual-publish.md",
    )
    forbidden = ("n8n", "Hermes Agent")
    for rel in early_paths:
        text = read(root, rel)
        if not text:
            continue
        for marker in forbidden:
            if marker in text:
                problems.append(
                    Problem(
                        "HYB004",
                        rel,
                        f"concrete runtime {marker!r} must not be adopted in M00-M03/Part00-01",
                    )
                )


def check_part02_boundary(root: Path, problems: list[Problem]) -> None:
    require_markers(
        root,
        "roadmap/part-02.md",
        "HYB005",
        (
            "First orchestration learning slice — M04",
            "manual trigger",
            "n8n read-only/import workflow",
            "Go validate + reconcile",
            "không có external mutation",
            "Human\n= actor duy nhất được publish",
        ),
        problems,
    )


def check_part04_ownership(root: Path, problems: list[Problem]) -> None:
    require_markers(
        root,
        "roadmap/part-04.md",
        "HYB006",
        (
            "n8n\n= primary watcher/orchestration reference",
            "Go creates/validates DecisionPacket",
            "n8n routes DecisionPacket",
            "Go Policy owns final state",
            "Go validation/policy unavailable\n→ no consequential downstream execution",
        ),
        problems,
    )


def check_part05_governance(root: Path, problems: list[Problem]) -> None:
    require_markers(
        root,
        "roadmap/part-05.md",
        "HYB007",
        (
            "AgentRuntime\n= investigate + read-only tool use + propose",
            "Go\n= Tool Registry contract + validation + ActionIntent + deterministic risk/policy + authorization",
            "n8n\n= invoke/route Agent + shadow workflow + durable approval routing + bounded execution",
            "Hermes Agent là **primary Agent runtime reference/candidate**",
            "CandidateEvidence\n→ Go validate / ground",
            "n8n IF/Switch node không được tự reclassify `RISK2` thành auto-executable",
            "kill switch ON\n→ execution blocked even with prior approval",
        ),
        problems,
    )


def check_part06_fail_safe(root: Path, problems: list[Problem]) -> None:
    require_markers(
        root,
        "roadmap/part-06.md",
        "HYB008",
        (
            "Agent unavailable\n≠ core deterministic decision unavailable",
            "n8n unavailable\n≠ canonical evidence/history corrupted",
            "Go Policy unavailable\n→ no consequential execution",
            "Correlation ID phải survive cross-runtime boundaries",
            "kill switch ON\n→ NO EXECUTION",
        ),
        problems,
    )


def check_reference_replaceability(root: Path, problems: list[Problem]) -> None:
    require_markers(
        root,
        "docs/TECHNOLOGY-CANDIDATES.md",
        "HYB009",
        (
            "n8n\n= primary orchestration reference",
            "AgentRuntime\n= intelligence role",
            "Hermes Agent\n= primary reference/candidate implementation",
            "n8n | Không; contract/behavior mới là gate",
            "Hermes Agent candidate/reference | Không",
        ),
        problems,
    )


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
    return problems


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    problems = validate(root)
    if problems:
        for problem in problems:
            print(problem)
        print(f"Hybrid runtime validation failed with {len(problems)} problem(s).")
        return 1
    print("Hybrid runtime validation passed: Go/n8n/Agent ownership, maturity and fail-safe boundaries are consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
