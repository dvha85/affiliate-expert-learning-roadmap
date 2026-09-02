from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "starter-kits/M04-grounded-advisory"))
from grounding_gate import evaluate
from scripts.validate_m04_grounded_advisory_pack import validate


class M04GroundedAdvisoryPackTests(unittest.TestCase):
    def setUp(self) -> None:
        self.baseline = {"recommended_state": "RANK_SCENARIO"}
        self.evidence = {"OBS-1": {"price": 100}}

    def test_evaluator_pack_passes(self):
        self.assertEqual(validate(), [])

    def test_unknown_ref_falls_back(self):
        result = evaluate(self.baseline, self.evidence, {"facts": [{"evidence_ref": "NOPE", "field": "price", "value": 100}]})
        self.assertEqual(result["status"], "rejected")
        self.assertTrue(result["fallback_used"])
        self.assertEqual(result["baseline"], self.baseline)

    def test_tool_request_is_not_executed(self):
        result = evaluate(self.baseline, self.evidence, {"facts": [], "writes": ["history"]})
        self.assertEqual(result["status"], "rejected")
        self.assertFalse(result["tool_or_write_called"])
        self.assertIsNone(result["action"])
