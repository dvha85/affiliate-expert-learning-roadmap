---
mission_id: "M05"
title: "First Reviewed Improvement"
status: draft
curriculum_version: 2
release_kind: "bot"
requires_missions: ["M04"]
bot_version_from: "v0.4"
bot_version_to: "v0.5"
estimated_hours: 10
delivery:
  starter_paths:
    - "starter-kits/M05-reviewed-improvement/"
  eval_pack: "evals/M05-reviewed-improvement/"
  verification_commands:
    - "python scripts/validate_m05_reviewed_improvement_pack.py"
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

Nâng v0.4 thành v0.5 bằng một improvement loop có review/rollback, không self-modification:

```text
Decision → ActionRecord → Outcome → Evaluation
→ ChangeProposal(PENDING_REVIEW)
→ human release | reject
→ rollback target retained
```

Outcome/AI chỉ được tạo proposal. Không tự sửa prompt, rule, policy, workflow, weight hoặc production behavior.

## Starting Bot State — Trạng thái Bot ban đầu

M04 v0.4 có grounded advisory/fallback. M03 đã cung cấp real ActionRecord/outcome context và M02 giữ replayable history.

## Try First — Thử trước

Trước outcome, freeze:

- bottleneck/evidence;
- hypothesis;
- one main variable;
- primary metric;
- measurement window;
- stop rule;
- rollback target.

Traffic không đủ phải có khả năng kết luận `INCONCLUSIVE`.

## Run — Chạy

```bash
python scripts/validate_m05_reviewed_improvement_pack.py
```

Fixture chỉ kiểm linkage/review/rollback. E4 cần trace thật.

## Observe — Quan sát

Ghi Decision/Action/Outcome/Evaluation IDs, measurement context, observed value state, attribution limitation, production/content cost khi relevant và ChangeProposal status.

## Knowledge Pull — Lấy kiến thức đúng lúc

Pull `9.1`, `10.1`, `11.1` khi hypothesis, measurement/inference hoặc review/version/rollback là blocker thật.

## Improve — Cải tiến

Chạy offline replay/champion–challenger trước. Human review quyết định release/reject; ChangeProposal phải versioned và có rollback path.

## Tests — Kiểm thử

- thiếu one-variable/freeze/window/stop rule → fail;
- trace phải nối Decision → ActionRecord → Outcome → Evaluation;
- low traffic giữ `INCONCLUSIVE`;
- ChangeProposal ở `PENDING_REVIEW` trước human review;
- production mutation hoặc missing rollback/review → fail.

## Reality Check — Kiểm chứng thực tế

E4 cần linked real trace + human review. Negative/inconclusive outcome vẫn hợp lệ nếu measurement trung thực. Synthetic replay không thay E4.

## Operate — Vận hành

Lưu version/champion/challenger, reviewer, release/reject decision, rollback target và next measurement.

## Failure Case — Tình huống lỗi

Nhiều biến đổi đồng thời, chọn window sau outcome, missing linkage, AI self-modify hoặc gọi inconclusive là lift đều phải block/review.

## Safety Gate — Cổng an toàn

S1 propose-only: không tool/write/publish/execution và không tự release production change.

## Evidence — Bằng chứng

Dùng M05 contract, Experiment Plan, Change Review và redacted trace summary. Raw/private data giữ local ignored.

## Explain-back — Giải thích lại

Learner giải thích được vì sao outcome không tự authorize change, `INCONCLUSIVE` nghĩa gì, và review/rollback giữ hệ thống học nhưng không self-modify.

## Mission PASS — Tiêu chí PASS

### Capability
- [ ] Linked experiment/evaluation/proposal/review/rollback record + failure tests.

### Reality
- [ ] Có E4 trace thật với human review hoặc blocker được ghi trung thực.

### Operated
- [ ] Có versioned release/reject decision + rollback target + next measurement.

## Bot Version Result — Kết quả phiên bản Bot

`v0.5`: reviewed improvement proposal loop; still no autonomous external action.

## Next Mission — Mission tiếp theo

M06 — Reliable Automatic Watcher.
