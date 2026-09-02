from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STARTER = ROOT / "starter-kits/M02-deterministic-baseline"
sys.path.insert(0, str(STARTER))
from baseline import evaluate
from scripts.validate_m02_deterministic_pack import validate


class M02DeterministicPackTests(unittest.TestCase):
    def test_evaluator_pack_passes(self):
        self.assertEqual(validate(), [])

    def test_missing_value_abstains_without_action(self):
        result = evaluate([
            {"subject_id": "x", "source_url": "https://example.invalid/x", "observed_at": "2026-09-02T00:00:00Z", "price": 0, "commission_rate": None}
        ])
        self.assertEqual(result["recommended_state"], "GET_MORE_DATA")
        self.assertIsNone(result["action"])
        self.assertFalse(result["ai_or_tool_called"])

    def test_equal_scores_use_stable_subject_tie_break(self):
        rows = [
            {"subject_id": "z", "source_url": "x", "observed_at": "t", "price": 10, "commission_rate": 0.1},
            {"subject_id": "a", "source_url": "x", "observed_at": "t", "price": 10, "commission_rate": 0.1},
        ]
        self.assertEqual([row["subject_id"] for row in evaluate(rows)["ranking"]], ["a", "z"])
