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

    def test_early_n8n_adoption_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "missions/M02-grounded-ai-advisor.md", "Use n8n to run the workflow")
            problems = []
            validator.check_no_early_runtime_adoption(root, problems)
            self.assertTrue(any(p.code == "HYB004" and "n8n" in p.message for p in problems))

    def test_early_hermes_adoption_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "missions/M03-first-tracked-manual-publish.md", "Hermes Agent publishes the content")
            problems = []
            validator.check_no_early_runtime_adoption(root, problems)
            self.assertTrue(any(p.code == "HYB004" and "Hermes Agent" in p.message for p in problems))

    def test_part04_must_keep_go_policy_owner(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "roadmap/part-04.md",
                "n8n\n= primary watcher/orchestration reference\n"
                "Go creates/validates DecisionPacket\n"
                "n8n routes DecisionPacket\n"
                "Go validation/policy unavailable\n→ no consequential downstream execution\n")
            problems = []
            validator.check_part04_ownership(root, problems)
            self.assertTrue(any(p.code == "HYB006" and "Go Policy owns final state" in p.message for p in problems))

    def test_part05_must_keep_risk2_out_of_n8n_authority(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "roadmap/part-05.md",
                "AgentRuntime\n= investigate + read-only tool use + propose\n"
                "Go\n= Tool Registry contract + validation + ActionIntent + deterministic risk/policy + authorization\n"
                "n8n\n= invoke/route Agent + shadow workflow + durable approval routing + bounded execution\n"
                "Hermes Agent là **primary Agent runtime reference/candidate**\n"
                "CandidateEvidence\n→ Go validate / ground\n"
                "kill switch ON\n→ execution blocked even with prior approval\n")
            problems = []
            validator.check_part05_governance(root, problems)
            self.assertTrue(any(p.code == "HYB007" and "RISK2" in p.message for p in problems))

    def test_part06_requires_policy_fail_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "roadmap/part-06.md",
                "Agent unavailable\n≠ core deterministic decision unavailable\n"
                "n8n unavailable\n≠ canonical evidence/history corrupted\n"
                "Correlation ID phải survive cross-runtime boundaries\n"
                "kill switch ON\n→ NO EXECUTION\n")
            problems = []
            validator.check_part06_fail_safe(root, problems)
            self.assertTrue(any(p.code == "HYB008" and "Go Policy unavailable" in p.message for p in problems))

    def test_agent_safe_profile_is_required(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "docs/AGENT-RUNTIME-STANDARD.md", "Agent runtime is useful but unrestricted")
            problems = []
            validator.check_runtime_hardening(root, problems)
            self.assertTrue(any(p.code == "HYB010" for p in problems))

    def test_n8n_canonical_state_claim_is_rejected_even_with_good_marker(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "docs/AGENT-HITL-RUNTIME.md",
                  "n8n execution state/history\n≠ canonical Action / Approval / Execution state\n"
                  "For convenience, n8n execution state = canonical business state\n")
            problems = []
            validator.check_negative_authority_drift(root, problems)
            self.assertTrue(any(p.code == "HYB013" for p in problems))

    def test_n8n_final_policy_claim_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "roadmap/part-05.md", "Go Policy owns final state.\nn8n owns final policy for convenience.\n")
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

    def test_readme_stale_learner_claim_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "README.md",
                  "README không phải nguồn chuẩn của tiến độ người học\n"
                  "canonical learner-state source\ncanonical authoring-state source\n"
                  "Người học chưa bắt đầu\n")
            problems = []
            validator.check_readme_status_source(root, problems)
            self.assertTrue(any(p.code == "HYB014" and "forbidden" in p.message for p in problems))


if __name__ == "__main__":
    unittest.main()
