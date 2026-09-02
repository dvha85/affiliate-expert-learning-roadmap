from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "starter-kits/M03-trustworthy-history"))
from history import append_snapshot, classify_freshness
from scripts.validate_m03_history_pack import validate


class M03HistoryPackTests(unittest.TestCase):
    def snapshot(self) -> dict[str, object]:
        return {
            "record_type": "Observation",
            "subject_id": "a",
            "observation_id": "obs-1",
            "observed_at": "2026-09-01T00:00:00Z",
            "ingested_at": "2026-09-02T00:00:00Z",
            "provenance_ref": "fixture",
            "missing_fields": [],
        }

    def test_evaluator_pack_passes(self):
        self.assertEqual(validate(), [])

    def test_conflicting_duplicate_does_not_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "history.jsonl"
            self.assertEqual(append_snapshot(path, self.snapshot()), "APPENDED")
            changed = self.snapshot()
            changed["provenance_ref"] = "different"
            self.assertEqual(append_snapshot(path, changed), "CONFLICT")
            self.assertEqual(len(path.read_text(encoding="utf-8").splitlines()), 1)

    def test_freshness_requires_explicit_policy(self):
        self.assertEqual(classify_freshness("2026-09-01T00:00:00Z", "2026-09-02T00:00:00Z", None), "UNKNOWN")
