#!/usr/bin/env python3
"""Validate the structural contract for the v2 M00 human-only market loop."""
from __future__ import annotations

import argparse
from pathlib import Path

REQUIRED_MARKERS = (
    "evidence_kind: real",
    "source_url:",
    "observed_at:",
    "access_method: public_manual",
    "disclosure status:",
    "tracking context/reference:",
    "execution_actor: human_only",
    "action: manual publish",
    "outcome window:",
    "Bot/AI publish or external execution: no",
)


def validate(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors = [f"thiếu marker {marker!r}" for marker in REQUIRED_MARKERS if marker not in text]
    if "evidence_kind: synthetic" in text or "evidence_kind: test" in text:
        errors.append("synthetic/test không thể làm M00 reality evidence")
    if "execution_actor: bot" in text.lower() or "action: bot publish" in text.lower():
        errors.append("M00 chỉ cho human_only manual publish")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Kiểm M00 safe market-loop evidence pack")
    parser.add_argument(
        "--evidence",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "evals/M00-safe-market-loop/valid-evidence-summary.md",
    )
    args = parser.parse_args()
    errors = validate(args.evidence)
    if errors:
        print("M00 MARKET LOOP PACK: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("M00 MARKET LOOP PACK: PASS — structure only; human reviews E1/E2 reality.")
    return 0
