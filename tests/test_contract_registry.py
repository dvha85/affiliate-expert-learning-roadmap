from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_contract_registry import validate

ROOT = Path(__file__).resolve().parents[1]


class ContractRegistryTests(unittest.TestCase):
    def test_current_registry_passes(self):
        self.assertEqual(validate(ROOT), [])

    def test_missing_to_zero_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for path in ROOT.joinpath("contracts").rglob("*"):
                target = root / path.relative_to(ROOT)
                if path.is_dir():
                    target.mkdir(parents=True, exist_ok=True)
                else:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(path.read_bytes())
            for path in ROOT.joinpath("evals/cases").glob("o00-*.json"):
                target = root / path.relative_to(ROOT)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(path.read_bytes())
            (root / "policies").mkdir()
            (root / "policies/v2-authority-policy.json").write_bytes((ROOT / "policies/v2-authority-policy.json").read_bytes())
            trace_path = root / "contracts/examples/o00-trace.json"
            trace = json.loads(trace_path.read_text(encoding="utf-8"))
            trace["records"]["outcome"].update({"value_state": "missing", "observed_value": 0})
            trace_path.write_text(json.dumps(trace), encoding="utf-8")
            self.assertTrue(any("must not become observed zero" in error for error in validate(root)))
