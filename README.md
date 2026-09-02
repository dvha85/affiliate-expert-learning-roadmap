# Lộ trình học Affiliate Intelligence Bot

**Curriculum v2 / Reality-First migration is active.** Đây là lộ trình cho
người mới xây một bot hỗ trợ quyết định Affiliate, nhưng điểm bắt đầu không
phải là cài Go hay gọi AI: đó là một market loop nhỏ, an toàn và do con người
kiểm soát.

Nội dung learner-facing ưu tiên tiếng Việt; xem
[Quy chuẩn ngôn ngữ](docs/VIETNAMESE-LANGUAGE-STYLE.md).

## Bắt đầu đúng chỗ

1. Đọc [CURRICULUM.md](CURRICULUM.md), sequence authority hiện hành.
2. Xem [Mission index](missions/README.md) để biết v2 hiện chưa có Mission
   delivery bundle nào được tuyên bố ready/delivered.
3. Dùng [ADR-005](docs/ADR-005-REALITY-FIRST-CURRICULUM.md) và
   [migration guide](docs/CURRICULUM-MIGRATION-v2.md) khi muốn hiểu/đóng góp
   vào rebaseline.

M00 v2 sẽ là human-only safe market loop: public observation → human-created
micro-artifact → disclosure/tracking → human review/manual publish. Bot/AI sẽ
không publish. O00 (sắp author) chỉ là demo synthetic an toàn và không phải
PASS.

```text
REAL CONTEXT
→ human action and evidence
→ outcome snapshot
→ smallest deterministic Bot
→ trustworthy history
→ grounded AI advisory
→ reviewed improvement
→ governed automation
```

## What “smart” and “automatic” mean

```text
DETERMINISTIC CORE FIRST
≠ CODE FIRST

NO-CODE WHEN IT IS AUDITABLE
AGENT-WRITTEN CODE WHEN CODE IS NECESSARY
```

A useful bot carries source/time, separates fact/estimate/assumption/unknown,
can abstain, and keeps Decision → Action → Outcome → Evaluation traceable.
AI advice is untrusted input, not evidence or execution permission. Policy,
risk, approval, audit and kill switch remain mandatory for consequential action.

Go, DecisionRules, n8n and a Development Agent are implementation/reference
options, not prerequisites for the first learner action. The Go workspace in
this repository is a v1 reference to preserve and test, pending remapping to
v2 M02; do not treat it as a v2 M00 quickstart.

## Current readiness and learner state

README không phải nguồn chuẩn của tiến độ người học. The canonical learner-state source is [PROGRESS.md](PROGRESS.md), currently a v1 pilot snapshot. The canonical authoring-state source is [missions/README.md](missions/README.md).
Delivery/pilot visibility comes from:

```bash
python scripts/validate_readiness.py
python scripts/report_readiness.py
```

`ready` means authored; it does not mean a beginner starter, eval pack or pilot
has been delivered. Use `--strict` only as a promotion gate for a new v2 Mission.

## Legacy v1 reference

The local tag `curriculum-v1-pre-reality-first` preserves the exact baseline.
Existing missions, lessons and Go fixtures remain available for provenance and
regression tests. Learners already on v1 should follow
[migration rules](docs/CURRICULUM-MIGRATION-v2.md), not have progress silently
renumbered.

## Repository checks

```bash
python scripts/validate_curriculum.py
python scripts/validate_mission_status.py
python scripts/validate_readiness.py
python scripts/validate_evidence_taxonomy.py
python scripts/validate_authority.py
python scripts/validate_language_policy.py
python scripts/validate_vietnamese_headings.py
python scripts/validate_hardening.py
python scripts/validate_build_first.py
python scripts/validate_agentic_architecture.py
python scripts/validate_hybrid_runtime.py
python -m unittest discover -s tests -v
```

The Go checks continue to protect the retained v1 reference and learner
workspace; they do not make Go an all-Mission v2 dependency.
