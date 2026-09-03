from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_hybrid_runtime",
    ROOT / "scripts" / "validate_hybrid_runtime.py",
)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)


def write(root: Path, rel: str, text: str) -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class HybridRuntimeValidatorTests(unittest.TestCase):
    def test_current_repo_passes(self):
        problems = validator.validate(ROOT)
        self.assertEqual([], problems, "\n".join(str(p) for p in problems))

    def test_early_n8n_agent_adoption_is_rejected_in_v2_m04(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "missions/M04-grounded-ai-advisor.md", "Use n8n AI Agent to run M04")
            problems = []
            validator.check_no_early_runtime_adoption(root, problems)
            self.assertTrue(any(p.code == "HYB005" for p in problems))

    def test_early_decisionrules_adoption_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "missions/M00-first-safe-market-loop.md", "DecisionRules is mandatory")
            problems = []
            validator.check_no_early_runtime_adoption(root, problems)
            self.assertTrue(any(p.code == "HYB005" and "DecisionRules" in p.message for p in problems))

    def test_part02_rejects_legacy_m04_orchestration_slice(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(
                root,
                "roadmap/part-02.md",
                "M03 Trustworthy History & Measurement + M04 Grounded AI Advisor\n"
                "Manual/read-only path là baseline\n"
                "M04: A1 advisory only — không tool use, write, publish, account mutation hay autonomous loop.\n"
                "structured ≠ grounded\nAI recommendation ≠ execution permission\n"
                "First orchestration learning slice — M04\n",
            )
            problems = []
            validator.check_part02_boundary(root, problems)
            self.assertTrue(any(p.code == "HYB006" and "forbidden" in p.message for p in problems))

    def test_part02_requires_a1_no_tool_boundary(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(
                root,
                "roadmap/part-02.md",
                "M03 Trustworthy History & Measurement + M04 Grounded AI Advisor\n"
                "Manual/read-only path là baseline\n"
                "structured ≠ grounded\nAI recommendation ≠ execution permission\n",
            )
            problems = []
            validator.check_part02_boundary(root, problems)
            self.assertTrue(any(p.code == "HYB006" and "A1 advisory only" in p.message for p in problems))

    def test_part04_must_keep_deterministic_policy_owner(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(
                root,
                "roadmap/part-04.md",
                "n8n\n= primary watcher/orchestration reference\n"
                "Deterministic Core creates/validates DecisionPacket\n"
                "n8n routes DecisionPacket\n"
                "first meaningful visual-rule comparison\n"
                "Deterministic Policy Authority unavailable / invalid / unverified\n"
                "→ no consequential downstream execution\n",
            )
            problems = []
            validator.check_part04_ownership(root, problems)
            self.assertTrue(any(p.code == "HYB007" and "owns final state" in p.message for p in problems))

    def test_part05_must_keep_risk2_out_of_n8n_authority(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(
                root,
                "roadmap/part-05.md",
                "AgentRuntime\n= investigate + read-only tool use + propose\n"
                "n8n AI Agent là visual-first candidate ở M08\n"
                "Deterministic Core\n= Tool Registry contract + validation + ActionIntent + deterministic risk/policy + authorization\n"
                "CandidateEvidence\n→ Deterministic Core validate / ground\n"
                "Hermes/OpenAI Agents SDK comparison\n"
                "kill switch ON\n→ execution blocked even with prior approval\n",
            )
            problems = []
            validator.check_part05_governance(root, problems)
            self.assertTrue(any(p.code == "HYB008" and "RISK2" in p.message for p in problems))

    def test_part06_requires_policy_fail_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(
                root,
                "roadmap/part-06.md",
                "Agent unavailable\n≠ core deterministic decision unavailable\n"
                "n8n unavailable\n≠ canonical evidence/history corrupted\n"
                "rule runtime error / stale rule / unknown active version\n→ fail closed\n"
                "Correlation ID phải survive cross-runtime boundaries\n"
                "kill switch ON\n→ NO EXECUTION\n",
            )
            problems = []
            validator.check_part06_fail_safe(root, problems)
            self.assertTrue(any(p.code == "HYB009" and "Deterministic Policy Authority" in p.message for p in problems))

    def test_agent_safe_profile_requires_deterministic_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "docs/AGENT-RUNTIME-STANDARD.md", "Agent runtime is useful but unrestricted")
            problems = []
            validator.check_runtime_hardening(root, problems)
            self.assertTrue(any(p.code == "HYB011" for p in problems))

    def test_n8n_final_policy_claim_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "roadmap/part-05.md", "n8n owns final policy for convenience.\n")
            problems = []
            validator.check_negative_authority_drift(root, problems)
            self.assertTrue(any(p.code == "HYB013" for p in problems))

    def test_agent_direct_execution_claim_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "docs/AGENT-RUNTIME-STANDARD.md", "Agent proposal → direct execution")
            problems = []
            validator.check_negative_authority_drift(root, problems)
            self.assertTrue(any(p.code == "HYB013" for p in problems))

    def test_go_language_authority_regression_is_rejected_in_active_roadmap(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "roadmap/part-04.md", "Go decides what is true / allowed.\n")
            problems = []
            validator.check_negative_authority_drift(root, problems)
            self.assertTrue(any(p.code == "HYB014" for p in problems))

    def test_readme_stale_learner_claim_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(
                root,
                "README.md",
                "README không phải nguồn chuẩn của tiến độ người học\n"
                "canonical learner-state source\ncanonical authoring-state source\n"
                "DETERMINISTIC CORE FIRST\nDecisionRules\nDevelopment Agent\n"
                "Người học chưa bắt đầu\n",
            )
            problems = []
            validator.check_readme_status_source(root, problems)
            self.assertTrue(any(p.code == "HYB015" and "forbidden" in p.message for p in problems))


if __name__ == "__main__":
    unittest.main()
