from __future__ import annotations

import unittest

from scripts.validate_m02_profile_parity import validate


class M02ProfileParityTests(unittest.TestCase):
    def test_operator_profile_covers_shared_cases_without_go_requirement(self):
        self.assertEqual(validate(include_go=False), [])
