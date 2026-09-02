from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.validate_m01_outcome_snapshot_pack import REQUIRED_MARKERS, validate


class M01OutcomeSnapshotPackTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "snapshot.md"

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def valid_text(self) -> str:
        return "\n".join(REQUIRED_MARKERS) + "\noutcome_status: zero\nobserved_value: 0\n"

    def test_valid_structural_fixture_passes(self):
        self.path.write_text(self.valid_text(), encoding="utf-8")
        self.assertEqual(validate(self.path), [])

    def test_pending_cannot_be_zero(self):
        self.path.write_text(self.valid_text().replace("outcome_status: zero", "outcome_status: pending"), encoding="utf-8")
        self.assertTrue(any("pending" in error for error in validate(self.path)))

    def test_publish_is_rejected(self):
        self.path.write_text(self.valid_text() + "action: manual publish\n", encoding="utf-8")
        self.assertTrue(any("read-only" in error for error in validate(self.path)))
