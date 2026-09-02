"""Minimal append-only M03 history profile, deliberately standard-library only."""
from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

REQUIRED = ("subject_id", "observation_id", "observed_at", "ingested_at", "provenance_ref")


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)


def validate_snapshot(snapshot: dict[str, Any]) -> list[str]:
    errors = [f"missing {field}" for field in REQUIRED if not snapshot.get(field)]
    for key in ("observed_at", "ingested_at"):
        if snapshot.get(key):
            try:
                parse_time(str(snapshot[key]))
            except ValueError:
                errors.append(f"invalid {key}")
    if not isinstance(snapshot.get("missing_fields", []), list):
        errors.append("missing_fields must be a list")
    return errors


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
        if existing.get("observation_id") == snapshot["observation_id"]:
            return "ALREADY_SEEN" if canonical(existing) == canonical(snapshot) else "CONFLICT"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(canonical(snapshot) + "\n")
    return "APPENDED"


def history_for_subject(path: Path, subject_id: str) -> list[dict[str, Any]]:
    rows = [row for row in read_history(path) if row.get("subject_id") == subject_id]
    return sorted(rows, key=lambda row: (parse_time(str(row["observed_at"])), str(row["observation_id"])))


def classify_freshness(observed_at: str, as_of: str, max_age_seconds: int | None) -> str:
    if max_age_seconds is None:
        return "UNKNOWN"
    observed = parse_time(observed_at)
    point = parse_time(as_of)
    if point < observed:
        return "INVALID_TIME_CONTEXT"
    return "FRESH" if point - observed <= timedelta(seconds=max_age_seconds) else "STALE"
