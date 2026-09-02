from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_o00 import validate


class O00Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "o00.json"
        self.valid = {
            "orientation_only": True,
            "evidence_kind": "synthetic",
            "observation": {"source_url": None},
            "recommended_state": "GET_MORE_DATA",
            "action": None,
            "missing_evidence": ["source"],
        }

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def write(self, data: dict) -> None:
        self.path.write_text(json.dumps(data), encoding="utf-8")

    def test_valid_orientation_passes(self):
        self.write(self.valid)
        self.assertEqual(validate(self.path), [])

    def test_action_is_rejected(self):
        self.valid["action"] = {"type": "publish"}
        self.write(self.valid)
        self.assertTrue(any("action" in error for error in validate(self.path)))

    def test_real_source_is_rejected(self):
        self.valid["observation"] = {"source_url": "https://example.test"}
        self.write(self.valid)
        self.assertTrue(any("source_url" in error for error in validate(self.path)))
