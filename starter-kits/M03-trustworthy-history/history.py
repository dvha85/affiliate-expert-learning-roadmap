"""Minimal append-only M03 history profile, deliberately standard-library only."""
from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

REQUIRED = ("record_type", "subject_id", "observed_at", "ingested_at", "provenance_ref")
TYPE_ID = {
    "Observation": "observation_id",
    "ActionRecord": "action_record_id",
    "MeasurementContext": "measurement_context_id",
    "Outcome": "outcome_id",
    "Correction": "correction_id",
}
TYPE_REQUIRED = {
    "Observation": (),
    "ActionRecord": ("execution_actor", "tracking_id"),
    "MeasurementContext": ("action_record_id", "window_start", "window_end"),
    "Outcome": ("action_record_id", "measurement_context_id", "status", "value_state"),
    "Correction": ("corrects_record_id", "reconciliation_reason"),
}


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)


def validate_snapshot(snapshot: dict[str, Any]) -> list[str]:
    errors = [f"missing {field}" for field in REQUIRED if not snapshot.get(field)]
    record_type = snapshot.get("record_type")
    if record_type not in TYPE_ID:
        errors.append("record_type must be Observation, ActionRecord, MeasurementContext, Outcome or Correction")
    else:
        identifier = TYPE_ID[record_type]
        if not snapshot.get(identifier):
            errors.append(f"missing {identifier}")
        errors.extend(f"missing {field}" for field in TYPE_REQUIRED[record_type] if not snapshot.get(field))
    for key in ("observed_at", "ingested_at"):
        if snapshot.get(key):
            try:
                parse_time(str(snapshot[key]))
            except ValueError:
                errors.append(f"invalid {key}")
    if not isinstance(snapshot.get("missing_fields", []), list):
        errors.append("missing_fields must be a list")
    return errors


def record_id(snapshot: dict[str, Any]) -> str:
    record_type = str(snapshot.get("record_type"))
    return str(snapshot.get(TYPE_ID.get(record_type, ""), ""))


def canonical(snapshot: dict[str, Any]) -> str:
    return json.dumps(snapshot, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def read_history(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def append_snapshot(path: Path, snapshot: dict[str, Any]) -> str:
    errors = validate_snapshot(snapshot)
    if errors:
        return "REJECTED: " + "; ".join(errors)
    for existing in read_history(path):
        if record_id(existing) == record_id(snapshot):
            return "ALREADY_SEEN" if canonical(existing) == canonical(snapshot) else "CONFLICT"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(canonical(snapshot) + "\n")
    return "APPENDED"


def history_for_subject(path: Path, subject_id: str) -> list[dict[str, Any]]:
    rows = [row for row in read_history(path) if row.get("subject_id") == subject_id]
    return sorted(rows, key=lambda row: (parse_time(str(row["observed_at"])), record_id(row)))


def classify_freshness(observed_at: str, as_of: str, max_age_seconds: int | None) -> str:
    if max_age_seconds is None:
        return "UNKNOWN"
    observed = parse_time(observed_at)
    point = parse_time(as_of)
    if point < observed:
        return "INVALID_TIME_CONTEXT"
    return "FRESH" if point - observed <= timedelta(seconds=max_age_seconds) else "STALE"
