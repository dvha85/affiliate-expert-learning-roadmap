#!/usr/bin/env python3
"""Evaluate M03 append-only/provenance/freshness invariants on synthetic data."""
from __future__ import annotations

import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "starter-kits/M03-trustworthy-history"))
from history import append_snapshot, classify_freshness, history_for_subject, read_history  # noqa: E402


def validate() -> list[str]:
    errors: list[str] = []
    fixture = ROOT / "evals/M03-trustworthy-history/history.jsonl"
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "history.jsonl"
        shutil.copyfile(fixture, path)
        rows = read_history(path)
        ordered = history_for_subject(path, "synthetic-offer")
        if [row["record_type"] for row in rows] != ["Observation", "Observation", "ActionRecord", "MeasurementContext", "Outcome"]:
            errors.append("fixture must cover Observation, ActionRecord, MeasurementContext and Outcome")
        if [row.get("observation_id") for row in ordered[:2]] != ["obs-t1", "obs-t2"]:
            errors.append("history query phải sort theo observed_at, không theo ingested/arrival order")
        if append_snapshot(path, rows[0]) != "ALREADY_SEEN" or len(read_history(path)) != 5:
            errors.append("exact duplicate phải idempotent và không append thêm dòng")
        conflict = dict(rows[0])
        conflict["provenance_ref"] = "different-content"
        if append_snapshot(path, conflict) != "CONFLICT" or len(read_history(path)) != 5:
            errors.append("same observation_id với content khác phải conflict, không overwrite")
        correction = {
            "record_type": "Correction", "subject_id": "synthetic-offer", "correction_id": "cor-1",
            "observed_at": "2026-09-05T00:00:00Z", "ingested_at": "2026-09-05T00:00:00Z",
            "provenance_ref": "fixture-correction", "corrects_record_id": "out-1",
            "reconciliation_reason": "late source reconciliation", "missing_fields": [],
        }
        if append_snapshot(path, correction) != "APPENDED" or len(read_history(path)) != 6:
            errors.append("correction must append a new immutable record")
    if classify_freshness("2026-09-01T00:00:00Z", "2026-09-02T00:00:00Z", None) != "UNKNOWN":
        errors.append("freshness không có policy phải UNKNOWN")
    if classify_freshness("2026-09-02T00:00:00Z", "2026-09-01T00:00:00Z", 60) != "INVALID_TIME_CONTEXT":
        errors.append("as_of trước observed_at phải invalid time context")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("M03 HISTORY PACK: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("M03 HISTORY PACK: PASS — synthetic evaluator only; no external action.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
