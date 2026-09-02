from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.validate_readiness import validate


def mission(starter: str = "starter/", pilot: str = "untested", include_delivery: bool = True) -> str:
    delivery = "" if not include_delivery else f'''delivery:
  starter_paths:
    - "{starter}"
  eval_pack: null
  verification_commands:
    - "python -m unittest"
  pilot_status: {pilot}
  pilot_evidence_refs: []
'''
    return f'''---
mission_id: "M00"
title: "Example"
status: ready
curriculum_version: 2
release_kind: "bot"
{delivery}---
'''


class ReadinessValidatorTests(unittest.TestCase):
    def make_root(self, text: str) -> Path:
        root = Path(self.tmp.name)
        (root / "missions").mkdir()
        (root / "starter").mkdir()
        (root / "missions" / "M00-example.md").write_text(text, encoding="utf-8")
        return root

    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_valid_metadata_passes_non_strict(self):
        self.assertEqual(validate(self.make_root(mission())), [])

    def test_missing_delivery_is_rejected(self):
        problems = validate(self.make_root(mission(include_delivery=False)))
        self.assertTrue(any(problem.code == "READY005" for problem in problems))

    def test_invalid_pilot_status_is_rejected(self):
        problems = validate(self.make_root(mission(pilot="guessed")))
        self.assertTrue(any(problem.code == "READY009" for problem in problems))

    def test_missing_starter_path_is_rejected(self):
        problems = validate(self.make_root(mission(starter="missing/")))
        self.assertTrue(any(problem.code == "READY011" for problem in problems))

    def test_strict_requires_complete_delivery_for_ready_mission(self):
        problems = validate(self.make_root(mission()), strict=True)
        self.assertTrue(any(problem.code == "READY014" for problem in problems))

    def test_strict_ignores_legacy_ready_mission(self):
        problems = validate(self.make_root(mission().replace("curriculum_version: 2", "curriculum_version: 1")), strict=True)
        self.assertFalse(any(problem.code == "READY014" for problem in problems))
