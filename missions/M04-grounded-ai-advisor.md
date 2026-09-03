---
mission_id: "M04"
title: "Grounded AI Advisor"
status: draft
curriculum_version: 2
release_kind: "bot"
requires_missions: ["M03"]
bot_version_from: "v0.3"
bot_version_to: "v0.4"
estimated_hours: 10
delivery:
  starter_paths:
    - "starter-kits/M04-grounded-advisory/"
  eval_pack: "evals/M04-grounded-advisory/"
  verification_commands:
    - "python scripts/validate_m04_grounded_advisory_pack.py"
knowledge:
  required: []
  on_demand: ["8.1", "8.2", "8.3"]
  reference: ["5.1", "5.2", "5.3"]
milestones:
  contributes_to: ["G3"]
evidence:
  minimum_level: "E3"
  reality_required: true
safety_gate: "S1"
risk_scope:
  external_side_effects: false
  execution_actor: "advisory_only"
---

# Mission M04 — Grounded AI Advisor

## Ship Target — Mục tiêu bàn giao

Nâng Bot v0.3 thành v0.4 bằng AI advisory có grounding và deterministic fallback:

```text
M03 evidence/history/outcome context
→ CALL_AI | SKIP_AI
→ untrusted candidate advisory
→ evidence-reference + claim-support validation
→ grounded | rejected | unavailable | skipped
→ deterministic fallback preserved
→ action: null
```

AI có thể hỗ trợ phân tích/tóm tắt/hypothesis nhưng không là source of truth, không sửa canonical evidence/history và không có tool/write/publish/execution.

## Starting Bot State — Trạng thái Bot ban đầu

M03 v0.3 đã có deterministic decision, replayable history và tracked human-action/outcome context. Starter/eval của M04 là replay-first; không cần API key để chứng minh grounding/fallback behavior.

## Try First — Thử trước

Human freeze deterministic baseline rồi ghi trước:

- fact nào evidence support;
- claim nào chưa support;
- câu hỏi nào AI có thể tạo thêm decision value;
- fallback mong đợi nếu output malformed/unsupported/unavailable;
- khi nào `SKIP_AI` tốt hơn `CALL_AI`.

## Run — Chạy

```bash
python scripts/validate_m04_grounded_advisory_pack.py
```

Replay fixture là E0 engineering evidence. Không đưa secret/raw customer/account data vào prompt/log/commit.

## Observe — Quan sát

Ghi routing decision, evidence refs, deterministic baseline version, candidate schema, support/rejection reason, fallback reason, execution kind (`replay | live`) và redaction limitation.

## Knowledge Pull — Lấy kiến thức đúng lúc

Pull `8.1–8.3` khi AI routing, schema/grounding hoặc eval/fallback thật sự là blocker. Numeric lesson cũ chỉ là reference, không phải reading order.

## Improve — Cải tiến

Thêm một explicit validation/fixture sau mỗi failure: malformed schema, unknown ref, unsupported claim, unavailable provider, injection-like source text hoặc secret leakage. Không nới authority để làm test xanh.

## Tests — Kiểm thử

- grounded output phải có evidence refs và exact field/value support;
- unknown ref/unsupported claim bị rejected;
- malformed/unavailable/injection case dùng fallback;
- `SKIP_AI` là behavior hợp lệ có reason;
- no tool, write, publish hoặc execution;
- replay không được gọi là live evidence.

## Reality Check — Kiểm chứng thực tế

M04 dùng E3 evidence/outcome context thật từ M03 khi có access. Replay chỉ chứng minh gate. Live provider chưa chạy phải ghi `pending`, không giả verified.

## Operate — Vận hành

Log redacted input/evidence/baseline/advisor versions, routing/status/fallback và next measurement. Evidence stale/missing phải fallback/abstain thay vì tăng confidence/permission.

## Failure Case — Tình huống lỗi

Invented CVR/revenue, valid ref nhưng sai field/value, provider timeout, prompt injection hoặc request đòi tool/write phải reject/fallback.

## Safety Gate — Cổng an toàn

S1 advisory-only: không tool, write, publish, execution, credential/account access hay policy mutation.

## Evidence — Bằng chứng

Dùng M04 contract/eval record và redacted summary. Evidence refs phải resolve; raw/private payload ở ignored local storage.

## Explain-back — Giải thích lại

Learner giải thích được grounded khác plausible, evidence ref khác claim support, fallback bảo toàn deterministic baseline ra sao và vì sao AI không có execution authority.

## Mission PASS — Tiêu chí PASS

### Capability
- [ ] Grounded/rejected/unavailable/skipped behaviors + fallback tests đều hoạt động.

### Reality
- [ ] Nối E3 evidence references trung thực; replay/live labeling đúng.

### Operated
- [ ] Có evaluation record + rejection/fallback review + next measurement.

## Bot Version Result — Kết quả phiên bản Bot

`v0.4`: grounded A1 advisory, no tools/write/action.

## Next Mission — Mission tiếp theo

M05 — First Reviewed Improvement.
