#!/usr/bin/env python3
"""Validate the structural contract for a v2 M01 read-only outcome snapshot."""
from __future__ import annotations

import argparse
from pathlib import Path

REQUIRED_MARKERS = (
    "evidence_kind: real",
    "measurement_source/reference:",
    "observed_at:",
    "window_start:",
    "window_end:",
    "outcome_status:",
    "observed_value:",
    "missing_vs_zero:",
    "attribution limitation:",
    "execution_actor: human_only",
    "action: none (read-only snapshot)",
    "raw/private location:",
)
ALLOWED_STATUSES = {"zero", "pending", "partial", "final", "inconclusive"}


def value_after(text: str, marker: str) -> str:
    for line in text.splitlines():
        if marker in line:
            value = line.split(marker, 1)[1].strip()
            if value:
                return value
    return ""


def validate(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors = [f"thiếu marker {marker!r}" for marker in REQUIRED_MARKERS if marker not in text]
    if "evidence_kind: synthetic" in text or "evidence_kind: test" in text:
        errors.append("synthetic/test không thể làm M01 reality evidence")
    status_value = value_after(text, "outcome_status:")
    observed_value = value_after(text, "observed_value:")
    status = status_value.split()[0] if status_value else ""
    value = observed_value.split()[0] if observed_value else ""
    if status and status not in ALLOWED_STATUSES:
        errors.append("outcome_status phải là zero, pending, partial, final hoặc inconclusive")
    if status == "zero" and value != "0":
        errors.append("outcome_status zero phải ghi observed_value: 0")
    if status == "pending" and value == "0":
        errors.append("pending không được giả làm observed zero")
    if "action: manual publish" in text.lower() or "action: bot publish" in text.lower():
        errors.append("M01 là read-only snapshot, không được publish")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Kiểm M01 outcome-snapshot evidence pack")
    parser.add_argument(
        "--snapshot",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "evals/M01-outcome-snapshot/valid-outcome-snapshot.md",
    )
    args = parser.parse_args()
    errors = validate(args.snapshot)
    if errors:
        print("M01 OUTCOME SNAPSHOT PACK: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("M01 OUTCOME SNAPSHOT PACK: PASS — structure only; human reviews E3 reality.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
