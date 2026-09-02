from __future__ import annotations

import json
import unittest
from pathlib import Path

from scripts.validate_m05_reviewed_improvement_pack import validate

ROOT = Path(__file__).resolve().parents[1]


class M05ReviewedImprovementTests(unittest.TestCase):
    def setUp(self) -> None:
        self.data = json.loads((ROOT / "evals/M05-reviewed-improvement/valid-reviewed-improvement.json").read_text(encoding="utf-8"))

    def test_valid_fixture_passes(self):
        self.assertEqual(validate(self.data), [])

    def test_production_mutation_is_rejected(self):
        self.data["change_proposal"]["production_mutation"] = True
        self.assertTrue(any("cannot mutate" in error for error in validate(self.data)))

    def test_inconclusive_must_remain_honest(self):
        self.data["evaluation"]["result"] = "SUPPORTED"
        self.assertTrue(any("inconclusive" in error for error in validate(self.data)))
