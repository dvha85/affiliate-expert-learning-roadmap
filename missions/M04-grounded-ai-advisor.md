---
mission_id: "M04"
title: "Grounded AI Advisor"
status: draft
curriculum_version: 2
release_kind: "bot"
requires_missions: ["M03"]
bot_version_from: "v0.2"
bot_version_to: "v0.3"
estimated_hours: 10
delivery:
  starter_paths:
    - "starter-kits/M04-grounded-advisory/"
  eval_pack: "evals/M04-grounded-advisory/"
  verification_commands:
    - "python scripts/validate_m04_grounded_advisory_pack.py"
knowledge:
  required: []
  on_demand: ["5.1", "5.2", "5.3"]
  reference: []
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

Nâng v0.2 thành v0.3 với grounded AI advisory có evidence refs và fallback:

```text
M03 evidence/history + deterministic baseline FIRST
→ untrusted candidate advisory
→ reference-validity + claim-support checks
→ grounded | rejected | unavailable | skipped
→ fallback baseline preserved, action null
```

AI có thể tóm tắt fact/hypothesis/missing evidence, nhưng không là source of
truth, không sửa scoring/history và không có tool/write/publish/execution.

## Starting Bot State — Trạng thái Bot ban đầu

M03 v0.2 có provenance/freshness/missing semantics. Bắt đầu bằng
`starter-kits/M04-grounded-advisory/` replay-only gate; Core không yêu cầu API
key, paid model hay live provider. Replay là evaluation fixture, không claim
provider live đã hoạt động.

## Try First — Thử trước

Trước khi gọi bất kỳ model nào, human freeze deterministic baseline và tự ghi:

- fact nào evidence thực sự support;
- fact nào chưa support;
- hypothesis/missing evidence nào có thể hỏi AI hỗ trợ diễn giải;
- fallback expected nếu AI malformed/unavailable/unsupported.

Chạy candidate unsupported claim để thấy parse JSON không đồng nghĩa grounded.

## Run — Chạy

```bash
python scripts/validate_m04_grounded_advisory_pack.py
```

Starter validates replay candidate against explicit evidence. Không đưa secret,
raw customer/account data hay instruction untrusted vào prompt/log/commit.

## Observe — Quan sát

Ghi `advisor_execution_kind: replay | live`, input evidence refs, baseline
version, candidate schema, support/rejection reason, fallback reason, model/
prompt version khi relevant và redaction limitation. Evidence refs tồn tại vẫn
chưa đủ: field/value phải support claim.

## Knowledge Pull — Lấy kiến thức đúng lúc

- `5.1` khi chưa biết CALL_AI hay SKIP_AI theo decision value.
- `5.2` khi schema, evidence refs, uncertainty/hypothesis cần rõ.
- `5.3` khi eval, rejected output, fallback, cost hoặc privacy lộ gap.

Không add agent runtime, tool registry hay write permission trong M04.

## Improve — Cải tiến

Thêm one explicit check/fixture sau failure: malformed schema, unknown ref,
unsupported field/value, unavailable provider, prompt-injection-like text hoặc
secret redaction. Giữ baseline immutable; accepted advisory không được mutate
observed fact, score/rank hay policy.

## Tests — Kiểm thử

- valid grounded replay có evidence refs và exact field/value support;
- unknown ref/unsupported claim bị rejected;
- unavailable/malformed/prompt injection fixture dùng fallback;
- no tool, write, publish hoặc execution; action luôn null;
- replay được gắn replay, không gọi là live evidence.

## Reality Check — Kiểm chứng thực tế

M04 sử dụng E3 source/history thật từ M01/M03 khi có access. Evaluator replay
chỉ chứng minh gate. Live provider là optional và nếu chưa chạy phải ghi
`live_provider_verified: pending`, không đổi replay thành real/live.

## Operate — Vận hành

Log redacted input/evidence/baseline/advisor versions, status/fallback và next
measurement. Monitor unsupported/rejection rate; khi evidence stale/missing,
SKIP_AI hoặc fallback/GET_MORE_DATA thay vì nới authority.

## Failure Case — Tình huống lỗi

Malformed candidate, invented CVR/revenue, valid ref nhưng sai field/value,
provider timeout, malicious public text hoặc prompt requesting tool access phải
reject/fallback. Không retry thành publish/execution.

## Safety Gate — Cổng an toàn

S1 advisory-only: không tool, write, publish, execution, network side effect,
credential/account access hoặc change policy/weights. Human quyết định mọi
external action sau scope/approval Mission sau.

## Evidence — Bằng chứng

Dùng `[M04 contract](../docs/M04-GROUNDED-ADVISORY-CONTRACT.md)`, evaluator
replay, `templates/MISSION-EVIDENCE.md` và redacted summary. Evidence refs phải
resolve được nhưng raw/private data không commit. Dùng
`starter-kits/M04-grounded-advisory/ADVISORY-EVALUATION-RECORD.md`; replay phải
ghi `live_provider_verified: pending`, không tự nhận là live.

## Explain-back — Giải thích lại

Learner giải thích được grounded khác plausible, evidence ref khác claim
support, fallback bảo toàn baseline ra sao và tại sao AI advisory không có
execution authority.

## Mission PASS — Tiêu chí PASS

### Capability

- [ ] Có grounded/rejected/unavailable/skipped behaviors, evidence refs và
  fallback tests; no tool/write/execute.

### Reality

- [ ] Nối replay/live status trung thực với E3 evidence references; không claim
  fixture/live provider thiếu access là verified.

### Operated

- [ ] Có redacted evaluation record, fallback/rejection review và next
  measurement before M05 proposes an improvement.

## Bot Version Result — Kết quả phiên bản Bot

`v0.3`: A1 grounded advisory only. M05 mới đề xuất improvement từ outcome qua
review/version/rollback, không tự sửa model/prompt/policy.

## Next Mission — Mission tiếp theo

M05 — First Reviewed Improvement, nối Outcome → Evaluation → proposal/review/
rollback.
