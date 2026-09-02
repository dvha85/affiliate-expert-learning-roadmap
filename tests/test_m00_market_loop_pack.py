from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.validate_m00_market_loop_pack import REQUIRED_MARKERS, validate


class M00MarketLoopPackTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "evidence.md"

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_valid_structural_fixture_passes(self):
        self.path.write_text("\n".join(REQUIRED_MARKERS), encoding="utf-8")
        self.assertEqual(validate(self.path), [])

    def test_missing_tracking_is_rejected(self):
        markers = [marker for marker in REQUIRED_MARKERS if marker != "tracking context/reference:"]
        self.path.write_text("\n".join(markers), encoding="utf-8")
        self.assertTrue(any("tracking" in error for error in validate(self.path)))

    def test_bot_publish_is_rejected(self):
        self.path.write_text("\n".join(REQUIRED_MARKERS) + "\naction: bot publish\n", encoding="utf-8")
        self.assertTrue(any("human_only" in error for error in validate(self.path)))
