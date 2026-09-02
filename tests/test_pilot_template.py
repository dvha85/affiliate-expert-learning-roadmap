from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_pilot_template import validate

ROOT = Path(__file__).resolve().parents[1]


class PilotTemplateTests(unittest.TestCase):
    def test_tracked_template_passes(self):
        self.assertEqual(validate(ROOT / "pilot/aggregate-template.json"), [])

    def test_participant_claim_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "pilot.json"
            data = json.loads((ROOT / "pilot/aggregate-template.json").read_text(encoding="utf-8"))
            data["participant_count"] = 5
            path.write_text(json.dumps(data), encoding="utf-8")
            self.assertTrue(any("participants" in error for error in validate(path)))
