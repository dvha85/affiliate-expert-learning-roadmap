from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.validate_m00_market_evidence_bundle import validate

ROOT = Path(__file__).resolve().parents[1]


class M00MarketEvidenceBundleTests(unittest.TestCase):
    def test_fixture_passes(self):
        self.assertEqual(validate(ROOT / "evals/M00-market-evidence-bundle"), [])

    def test_two_observations_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            bundle = Path(tmp) / "bundle"
            shutil.copytree(ROOT / "evals/M00-market-evidence-bundle", bundle)
            path = bundle / "audience-observations.json"
            path.write_text("[]", encoding="utf-8")
            self.assertTrue(any("three" in error for error in validate(bundle)))
