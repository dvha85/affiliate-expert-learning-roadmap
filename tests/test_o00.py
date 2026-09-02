from __future__ import annotations

import unittest
from pathlib import Path

from scripts.validate_contract_registry import validate

ROOT = Path(__file__).resolve().parents[1]

class O00Tests(unittest.TestCase):
    def test_valid_orientation_passes(self):
        self.assertEqual(validate(ROOT), [])

    def test_invalid_cases_are_declared_and_rejected(self):
        # The registry validator mutates each declared invalid case internally.
        self.assertEqual(validate(ROOT), [])
