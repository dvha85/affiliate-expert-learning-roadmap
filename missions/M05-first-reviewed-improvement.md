---
mission_id: "M05"
title: "First Reviewed Improvement"
status: draft
curriculum_version: 2
release_kind: "bot"
requires_missions: ["M04"]
bot_version_from: "v0.3"
bot_version_to: "v0.4"
estimated_hours: 10
delivery:
  starter_paths:
    - "starter-kits/M05-reviewed-improvement/"
  eval_pack: "evals/M05-reviewed-improvement/"
  verification_commands:
    - "python scripts/validate_m05_reviewed_improvement_pack.py"
  pilot_status: untested
  pilot_evidence_refs: []
knowledge:
  required: []
  on_demand: ["9.1", "10.1", "11.1"]
  reference: []
milestones:
  contributes_to: ["G3"]
evidence:
  minimum_level: "E4"
  reality_required: true
safety_gate: "S1"
risk_scope:
  external_side_effects: false
  execution_actor: "advisory_only"
---

# Mission M05 — First Reviewed Improvement

## Ship Target — Mục tiêu bàn giao

Tạo một experiment nhỏ có one main variable và trace liên kết:

```text
Decision → ActionRecord → Outcome → Evaluation
→ ChangeProposal(PENDING_REVIEW)
→ human release | reject | rollback
```

Outcome chỉ tạo ChangeProposal. Bot/AI không tự sửa prompt, rule, policy,
workflow, weight, publish hay execution.

## Starting Bot State — Trạng thái Bot ban đầu

M04 v0.3 đã có grounded advisory/fallback và M03 có history/measurement. Bắt
đầu bằng `starter-kits/M05-reviewed-improvement/`; evaluator fixture là E0 và
không có market action, account access hay paid tool requirement.

## Try First — Thử trước

Từ one bottleneck có evidence, viết hypothesis, one main variable, primary
metric, MeasurementContext, window và stop rule **trước** khi xem outcome.
Nếu traffic không đủ, dự đoán `INCONCLUSIVE`, không kéo thêm biến để làm result
trông tích cực.

## Run — Chạy

```bash
python scripts/validate_m05_reviewed_improvement_pack.py
```

Dùng `starter-kits/M05-reviewed-improvement/EXPERIMENT-PLAN.md` và
`CHANGE-REVIEW.md` ở local/private workspace cho record thật. Fixture chỉ dùng
để test linkage/review/rollback behavior.

## Observe — Quan sát

Ghi frozen time, outcome time, action/measurement IDs, observed value state,
attribution limitation, content-production time, model/tool cost và net value
limitation. `0`, missing, pending và `INCONCLUSIVE` vẫn tách biệt.

## Knowledge Pull — Lấy kiến thức đúng lúc

- `9.1` khi hypothesis chưa nối với bottleneck/outcome.
- `10.1` khi window, primary metric hoặc honest inference không rõ.
- `11.1` khi ChangeProposal/review/version/rollback thiếu boundary.

Không thêm agent autonomy để né một measurement/review gap.

## Improve — Cải tiến

Chạy offline replay/champion–challenger trước; tạo ChangeProposal có evidence
refs và limitation. Human review quyết định release/reject và rollback plan.
Không mutate production từ Outcome, evaluation, model output hay scheduler.

## Tests — Kiểm thử

- experiment thiếu main variable/freeze/window/stop rule fail;
- trace phải link Decision → ActionRecord → Outcome → Evaluation;
- inconclusive traffic được giữ honest;
- production mutation hoặc missing human review/rollback fail;
- costs/limitations được ghi, ChangeProposal luôn PENDING_REVIEW trước review.

## Reality Check — Kiểm chứng thực tế

E4 cần trace thật có action/outcome/evaluation/review liên kết. Negative hoặc
inconclusive result vẫn hợp lệ nếu measurement honest. Synthetic replay không
thay E4; access/channel block phải ghi `BLOCKED_EXTERNAL`.

## Operate — Vận hành

Lưu version/champion/challenger, reviewer, release/reject decision, rollback
target và next measurement. M05 không deploy silent improvement.

## Failure Case — Tình huống lỗi

Nhiều biến đổi cùng lúc, window sau outcome, outcome không link action/context,
low traffic được gọi lift, AI yêu cầu self-modify hoặc không có rollback đều
phải block/review.

## Safety Gate — Cổng an toàn

S1 advisory/propose-only: không tool/write/publish/execution, không paid spend,
không change account/policy và không tự release. External change chỉ do human
thực hiện trong scope/approval tương ứng.

## Evidence — Bằng chứng

Dùng [M05 contract](../docs/M05-REVIEWED-IMPROVEMENT-CONTRACT.md), Experiment
Plan, Change Review, `templates/MISSION-EVIDENCE.md` và redacted summaries.
Raw data/cost receipts/private context giữ local ignored.

## Explain-back — Giải thích lại

Learner phải giải thích được one-variable boundary, vì sao outcome không tự
cho phép change, `INCONCLUSIVE` có ý nghĩa gì và release/rollback được review
ra sao.

## Mission PASS — Tiêu chí PASS

### Capability

- [ ] Tạo được linked experiment/evaluation/proposal/review/rollback record và
  failure tests.

### Reality

- [ ] Có E4 trace thật với human review, hoặc `BLOCKED_EXTERNAL` được ghi
  trung thực; fixture không được claim E4.

### Operated

- [ ] Có versioned release/reject decision, rollback target và next measurement.

## Bot Version Result — Kết quả phiên bản Bot

`v0.4`: reviewed improvement proposal only. M06+ authoring chỉ mở sau H1 trust
repair; live activation vẫn cần personal Reality/evidence gate tương ứng.

## Next Mission — Mission tiếp theo

PR9 trust repair + personal validation loop. Xem
[ADR-006](../docs/ADR-006-PERSONAL-ONLY-VALIDATION.md):
`AUTHORING_OPEN` không đồng nghĩa `LIVE_ACTIVATION`.
