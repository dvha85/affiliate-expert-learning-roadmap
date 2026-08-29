from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_agentic_architecture",
    ROOT / "scripts" / "validate_agentic_architecture.py",
)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)


def write(root: Path, rel: str, text: str) -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class AgenticArchitectureValidatorTests(unittest.TestCase):
    def test_current_repo_passes(self):
        problems = validator.validate(ROOT)
        self.assertEqual([], problems, "\n".join(str(p) for p in problems))

    def test_missing_authority_file_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            problems = []
            validator.check_authority(Path(tmp), problems)
            self.assertTrue(any(p.code == "AI001" for p in problems))

    def test_wrong_ai_level_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rows = []
            for i in range(16):
                mission = f"M{i:02d}"
                level = validator.EXPECTED_LEVELS[mission]
                if mission == "M05":
                    level = "A2"
                version = f"v0.{i}" if i < 4 else f"v{i - 3}.0"
                rows.append(f"| {mission} | {version} | {level} | target | theme |")
            write(root, "docs/BOT-EVOLUTION-ROADMAP.md", "\n".join(rows))
            problems = []
            validator.check_capability_levels(root, problems)
            self.assertTrue(any(p.code == "AI002" for p in problems))

    def test_decision_contract_missing_confidence_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(
                root,
                "docs/DECISION-CONTRACTS.md",
                "DecisionPacket evidence_refs uncertainty missing_evidence freshness expires_at risk_level policy_decision",
            )
            problems = []
            validator.check_decision_contract(root, problems)
            self.assertTrue(any(p.code == "AI003" and "confidence" in p.message for p in problems))

    def test_external_tool_without_policy_boundary_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(
                root,
                "docs/TOOL-REGISTRY-STANDARD.md",
                "EXTERNAL_SIDE_EFFECT ActionIntent approval permission: risk_ceiling: requires_approval: audit_fields:",
            )
            problems = []
            validator.check_tool_governance(root, problems)
            self.assertTrue(any(p.code == "AI004" and "Policy/Risk" in p.message for p in problems))

    def test_tool_contract_missing_risk_ceiling_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(
                root,
                "docs/TOOL-REGISTRY-STANDARD.md",
                "EXTERNAL_SIDE_EFFECT ActionIntent Policy/Risk approval permission: requires_approval: audit_fields:",
            )
            problems = []
            validator.check_tool_governance(root, problems)
            self.assertTrue(any(p.code == "AI005" and "risk_ceiling:" in p.message for p in problems))

    def test_untrusted_model_output_boundary_is_required(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(
                root,
                "docs/AI-AGENT-DECISION-ARCHITECTURE.md",
                "AI ADVICE ≠ EXECUTION AUTHORITY\nPOLICY BEFORE CONSEQUENTIAL ACTION",
            )
            problems = []
            validator.check_untrusted_boundary(root, problems)
            self.assertTrue(any(p.code == "AI006" and "MODEL OUTPUT" in p.message for p in problems))

    def test_evaluation_standard_requires_tool_and_decision_metrics(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(
                root,
                "docs/AGENT-EVALUATION-STANDARD.md",
                "task_success tool_selection_accuracy tool_argument_accuracy unsupported_claim_rate "
                "policy_block_accuracy decision_latency cost_per_decision human intervention rate",
            )
            problems = []
            validator.check_evaluation(root, problems)
            self.assertTrue(any(p.code == "AI007" and "confidence_calibration" in p.message for p in problems))

    def test_volatile_agent_fact_requires_freshness_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "docs/MCP-2026-OPERATING-NOTES.md", "freshness/implementation note\n**Volatility:** HIGH")
            write(
                root,
                "docs/BOT-ENGINEERING-REFRESH-2026.08.md",
                "## EXT:MCP:2026-07-28\n**Source:** x\n**URL:** x\n**Verified:** x\n**Volatility:** HIGH\n"
                "## EXT:AGENT:TOOL-SEARCH-PROGRAMMATIC\n**Source:** x\n**URL:** x\n**Verified:** x\n**Volatility:** HIGH\n"
                "## EXT:AGENT:DURABLE-HITL\n**Source:** x\n**URL:** x\n**Verified:** x\n**Volatility:** HIGH\n",
            )
            problems = []
            validator.check_freshness(root, problems)
            self.assertTrue(any(p.code == "AI008" and "Verified" in p.message for p in problems))

    def test_provider_neutral_core_marker_is_required(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(
                root,
                "docs/AI-PROVIDER-CAPABILITY-MATRIX.md",
                "AI Provider Interface\nProvider Adapter(s)\nExact provider/model mapping nằm config/freshness layer",
            )
            problems = []
            validator.check_provider_neutrality(root, problems)
            self.assertTrue(any(p.code == "AI009" for p in problems))

    def test_multi_agent_must_remain_optional_and_m15_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(
                root,
                "docs/AI-CAPABILITY-LEVELS.md",
                "A4 — Optional Multi-Agent\nChỉ cân nhắc ở M15\nkhông phải dependency mặc định",
            )
            write(root, "docs/BOT-EVOLUTION-ROADMAP.md", "| M14 | v9.0 | A4 optional | bad |\n")
            problems = []
            validator.check_multi_agent_boundary(root, problems)
            self.assertTrue(any(p.code == "AI010" for p in problems))

    def test_outcome_learning_cannot_self_modify_policy(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(
                root,
                "docs/DECISION-OUTCOME-MEMORY.md",
                "Decision\n→ Action\n→ Outcome\n→ Evaluation\n→ Proposed Improvement\n"
                "→ Offline Test / Experiment\n→ Review\n→ Deploy\n"
                "Agent/learning loop không tự rewrite production policy/prompt/weights",
            )
            problems = []
            validator.check_outcome_learning(root, problems)
            self.assertTrue(any(p.code == "AI011" and "Policy authority" in p.message for p in problems))

    def test_programmatic_orchestration_must_exclude_free_external_actions(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(
                root,
                "docs/PROGRAMMATIC-TOOL-ORCHESTRATION.md",
                "READ_ONLY\nallowlisted tools\npublish;\nspend;\naccount/security change;\ndestructive delete;",
            )
            problems = []
            validator.check_programmatic_orchestration(root, problems)
            self.assertTrue(any(p.code == "AI012" and "Không cho free orchestration" in p.message for p in problems))


if __name__ == "__main__":
    unittest.main()
