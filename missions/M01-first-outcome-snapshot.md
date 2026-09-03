---
mission_id: "M01"
title: "Smallest Deterministic Bot"
status: draft
curriculum_version: 2
release_kind: "bot"
requires_missions: ["M00"]
bot_version_from: null
bot_version_to: "v0.1"
estimated_hours: 6
delivery:
  starter_paths:
    - "lab/learner/affiliate-bot/"
  eval_pack: null
  verification_commands:
    - "cd lab/learner/affiliate-bot && go test ./..."
knowledge:
  required: []
  on_demand: []
  reference: ["0.2", "2.1", "2.2", "2.3"]
evidence:
  minimum_level: "E1"
  reality_required: true
safety_gate: "S0"
risk_scope:
  external_side_effects: false
  execution_actor: "deterministic_only"
---

# Mission M01 — Smallest Deterministic Bot

## Ship Target — Mục tiêu bàn giao

Dùng E1/context từ M00 để xây baseline tất định nhỏ nhất có thể audit:

```text
known evidence fields
→ deterministic formula + stable tie-break
→ RANK_SCENARIO | GET_MORE_DATA | HUMAN_REVIEW
→ reason + missing evidence
→ action: null
```

M01 phát hành Bot `v0.1`. Real evidence làm input đáng tin hơn nhưng **không tự nâng** weak scenario thành `RECOMMEND`.

## Starting Bot State — Trạng thái Bot ban đầu

M00 đã có Human DecisionPacket và public observations E1. Learner runtime nằm ở `lab/learner/affiliate-bot/`.

Fixture synthetic là E0 để kiểm behavior. E0 không thay E1.

## Try First — Thử trước

Viết trước bằng lời của bạn:

- field nào source thật support;
- field nào missing/unknown;
- rule đơn giản nhất muốn thử;
- khi nào phải `GET_MORE_DATA`;
- khi nào conflict cần `HUMAN_REVIEW`.

Sau đó mới chạy baseline. Không nhìn output Bot rồi backfill assumption vào Human DecisionPacket.

## Run — Chạy

```bash
cd lab/learner/affiliate-bot
go run ./cmd/bot
go test ./...
```

Dùng fixture mặc định để kiểm plumbing; khi dùng E1 thật chỉ đưa summary/reference đã redact, không commit credential/raw account data.

## Observe — Quan sát

Ghi input/evidence refs, formula version, ranking, stable tie-break, state, reason và missing evidence. `0` là observed value; missing/null không được đổi thành 0.

## Knowledge Pull — Lấy kiến thức đúng lúc

Numeric lesson cũ chỉ là reference. Pull `0.2` hoặc `2.1–2.3` khi evidence taxonomy, uncertainty hoặc abstention thật sự là blocker.

## Improve — Cải tiến

Thêm một validation/rule/rationale vì một gap đã quan sát được, bằng test trước. Không tối ưu formula để khớp outcome chưa có; không thêm AI, Agent, scheduler hay external action.

## Tests — Kiểm thử

- rankable input → stable `RANK_SCENARIO`;
- missing/invalid evidence → `GET_MORE_DATA`;
- mixed/identity/currency conflict → `HUMAN_REVIEW`;
- real evidence vẫn không auto-promote thành `RECOMMEND`;
- no AI/tool/write/external execution.

## Reality Check — Kiểm chứng thực tế

Fixture chỉ chứng minh deterministic behavior E0. Reality của M01 dùng E1 public observations từ M00. Bot output không tự tạo market evidence.

## Operate — Vận hành

Lưu input reference, formula version, output state/reason, missing evidence và next measurement để M02 có thể replay/history.

## Failure Case — Tình huống lỗi

Malformed input, missing provenance, equal score, mixed currency, duplicate identity và unknown values phải dẫn đến stable result hoặc abstain/review, không default 0 để tiếp tục.

## Safety Gate — Cổng an toàn

S0 deterministic local calculation. Không AI/model/tool/network credential, publish, spend, send hoặc external execution.

## Evidence — Bằng chứng

Lưu command/test output, redacted input reference, formula version, DecisionPacket output và limitation. `price × commission_rate` chỉ là weak scenario, không phải Affiliate truth.

## Explain-back — Giải thích lại

Learner giải thích được formula dùng fact nào, assumption nào chưa được đo, vì sao output là scenario chứ không phải permission, và vì sao real provenance không đồng nghĩa recommendation.

## Mission PASS — Tiêu chí PASS

### Capability
- [ ] Deterministic baseline có stable tie-break, reason và abstention tests.

### Reality
- [ ] Chạy với E1 context thật hoặc ghi rõ chỉ có E0 engineering fixture; không claim E0 là market evidence.

### Operated
- [ ] Lưu input/output/formula version + next missing-evidence measurement.

## Bot Version Result — Kết quả phiên bản Bot

`v0.1`: deterministic advisory baseline, no AI/tool/action.

## Next Mission — Mission tiếp theo

M02 — Trustworthy History + Replay.
