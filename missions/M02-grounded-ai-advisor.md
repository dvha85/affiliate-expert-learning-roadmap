---
mission_id: "M02"
title: "Grounded AI Advisor"
status: draft
requires_missions: ["M01"]
bot_version_from: "v0.2"
bot_version_to: "v0.3"
estimated_hours: 12
knowledge:
  required: ["5.1", "5.2", "5.3"]
  on_demand: []
  reference: []
milestones:
  contributes_to: ["G2"]
evidence:
  minimum_level: "E1"
  reality_required: true
safety_gate: "S1"
risk_scope:
  external_side_effects: false
---

# Mission M02 — Grounded AI Advisor

## Ship Target — Mục tiêu bàn giao

Thêm một A1 advisory layer trên Bot v0.2:

```text
validated E1 evidence + deterministic baseline
→ optional AI analysis
→ structured output validation
→ evidence-reference check
→ grounded advisory OR reject/fallback/abstain
```

Bot v0.3 phải tiếp tục tạo core decision khi AI unavailable. AI không có tool, write hoặc external execution authority.

## Starting Bot State — Trạng thái Bot ban đầu

Starting state là learner commit đã PASS M01:

- deterministic ranking/abstention tồn tại;
- E1 Observation history có provenance/freshness;
- invalid/stale/missing data đã có behavior rõ;
- chưa có model/provider adapter hoặc AI evaluation.

Reference không phải starting state.

## Try First — Thử trước

### Checkpoint 1 — Baseline trước AI

1. Chọn 5–10 historical/public evidence cases từ M00–M01.
2. Human label expected facts, unsupported fields và missing evidence.
3. Chạy deterministic Bot, lưu output/limitations.
4. Viết một câu: AI chỉ đáng gọi nếu expected information value nào cao hơn cost/risk?
5. Sau attempt, pull `5.1`.

### Checkpoint 2 — Chạy output AI chưa tin cậy

1. Đưa cùng evidence vào provider adapter hoặc reproducible provided AI fixture.
2. Thử bốn outputs: valid grounded, malformed schema, nonexistent evidence ref và unsupported claim.
3. Quan sát behavior trước validation.
4. Sau attempt, pull `5.2` và thêm structured/grounding gate.

### Checkpoint 3 — Evaluation + fallback

1. Chạy valid, unsupported, unavailable/timeout và malicious-content cases.
2. Đo schema validity, evidence coverage, unsupported claim, latency/cost khi có live provider.
3. Chứng minh invalid/unavailable AI không làm mất deterministic core output.
4. Sau attempt, pull `5.3`.

## Run — Chạy

Draft run contract:

```bash
cd lab/learner/affiliate-bot
go run ./cmd/bot
go test ./...
```

Expected inspectable output:

```text
Bot version: v0.3
Deterministic baseline: <decision + reasons>
AI invocation reason: <why called | skipped>
AI status: grounded | rejected | unavailable | skipped
AI advisory:
  facts: <claim + evidence refs>
  hypotheses:
  missing evidence:
  uncertainty:
Fallback used: true | false
Final authority: advisory only
```

Provider-specific response object không được trở thành domain contract.

## Observe — Quan sát

Ghi:

- baseline làm được gì trước AI;
- AI bổ sung evidence/analysis gì có giá trị;
- claim nào không truy được về source;
- malformed/unsupported output trước validation gây rủi ro gì;
- khi nào nên skip call vì evidence/cost/value;
- AI unavailable ảnh hưởng core behavior ra sao.

## Knowledge Pull — Lấy kiến thức đúng lúc

- `5.1` — chọn deterministic rule hay AI theo decision value;
- `5.2` — structured extraction với evidence refs và uncertainty;
- `5.3` — eval case, invalid-output rejection, fallback, cost và privacy.

Mission author phải cung cấp provider-neutral interface và reproducible offline tests. Core không được bắt learner mua paid service hoặc commit secret. Nếu live model access không có, capability có thể được kiểm bằng saved fixture/replay trên E1 inputs; mọi claim “live AI verified” phải giữ pending.

## Improve — Cải tiến

- thêm provider-neutral `Advisor` interface/adapter boundary;
- normalize output về schema riêng của Bot;
- reject unknown/malformed fields;
- require evidence refs cho material facts;
- tách observed facts, hypotheses và missing evidence;
- thêm confidence reason + uncertainty/abstention;
- fallback về deterministic baseline;
- log invocation reason, status, safe model metadata, latency/cost khi relevant;
- không log prompt secret hoặc raw sensitive data.

## Tests — Kiểm thử

Draft acceptance tests:

- deterministic baseline chạy không cần AI;
- valid grounded output được accept;
- malformed/unknown-field output bị reject;
- nonexistent/mismatched evidence ref bị reject;
- unsupported claim không trở thành Product/scoring fact;
- provider timeout/unavailable dùng fallback;
- malicious Product text không đổi instruction/authority;
- missing evidence dẫn tới abstain/request-more-data;
- same saved fixture tạo reproducible evaluation;
- secrets không xuất hiện trong output/log fixture.

## Reality Check — Kiểm chứng thực tế

**Minimum:** E1.

- AI/advisor input phải là public evidence thật từ M00–M01;
- mỗi accepted material claim trỏ tới source/evidence ref;
- human labels tạo trước AI output cho eval subset;
- `evidence_kind` của input và `ai_status` của output được lưu riêng;
- sample/synthetic malicious cases được dùng cho safety test, không thay E1 grounding cases.

Saved AI response có thể tạo reproducible Capability evidence nhưng không được trình bày như live provider call. Live provider là optional cho draft authoring trừ khi một no-cost/no-secret path được cung cấp.

M02 chưa có business outcome window hoặc external action.

## Operate — Vận hành

Chạy ít nhất:

1. baseline-only case;
2. valid grounded AI case;
3. invalid-schema case;
4. unsupported-evidence case;
5. provider unavailable/timeout case;
6. malicious retrieved-content case;
7. skip-call case khi expected value thấp.

Lưu model/fixture/workflow version để có thể replay.

## Failure Case — Tình huống lỗi

- malformed JSON/structured output;
- unknown field hoặc wrong type;
- evidence ref không tồn tại;
- AI trộn hypothesis thành fact;
- certainty cao nhưng evidence thiếu;
- prompt injection trong public Product text;
- timeout/rate-limit/unavailable;
- excessive cost/latency;
- secret/raw sensitive value lọt vào log.

Behavior đúng là reject, redact, fallback hoặc abstain; không cố “sửa hộ” một claim không grounded rồi silently accept.

## Safety Gate — Cổng an toàn

**S1 — AI Advisory. Authority ceiling: analyze/recommend only.**

Bắt buộc:

- baseline trước AI;
- model output là untrusted input;
- structured validation + grounding;
- budget và fallback;
- no tools;
- no internal/external write;
- Decision khác Execution.

Public content không thể cấp instruction/permission cho model. M02 không publish, send, spend, change account hoặc execute transaction.

## Evidence — Bằng chứng

Lưu dưới `artifacts/missions/M02/`:

- human-labeled eval subset;
- deterministic baseline output;
- accepted grounded output;
- malformed/unsupported outputs và rejection reason;
- fallback/unavailable output;
- prompt-injection case;
- schema + advisor interface/version;
- evaluation summary: validity, evidence coverage, unsupported claims, latency/cost khi relevant;
- learner commit và authority note.

Evidence chain:

```text
Observation/History(E1)
→ deterministic BotDecision baseline
→ grounded AI Analysis OR reject/fallback
→ human-visible advisory
→ no Action in scope
```

## Explain-back — Giải thích lại

Learner phải giải thích bằng case/evidence của mình:

1. Vì sao deterministic baseline phải tồn tại trước AI?
2. Grounded claim khác một câu trả lời hợp lý như thế nào?
3. Fact, hypothesis và missing evidence được tách ở đâu?
4. Vì sao confidence không thay evidence ref?
5. Khi AI unavailable/invalid, Bot làm gì và vì sao?
6. Prompt injection trong Product text bị chặn ở trust boundary nào?
7. AI output hiện được phép làm gì và không được phép làm gì?
8. Metric/evidence nào chứng minh AI thêm giá trị thay vì chỉ thêm cost?

## Mission PASS — Tiêu chí PASS

### Capability

- [ ] deterministic baseline chạy độc lập
- [ ] AI output có schema và evidence validation
- [ ] facts/hypotheses/missing evidence tách rõ
- [ ] invalid/unsupported/unavailable cases reject/fallback đúng
- [ ] safety/eval cases đạt
- [ ] no secret leakage
- [ ] required lessons được pull sau attempt và explain-back đạt

### Reality

- [ ] accepted advisor cases dùng E1 evidence
- [ ] human label tồn tại trước AI output trên eval subset
- [ ] material claim có evidence ref
- [ ] saved fixture/live call được phân loại trung thực

### Operated

- [ ] chạy đủ baseline, valid, invalid, fallback, injection và skip-call cases
- [ ] model/fixture/workflow version được lưu
- [ ] S1 đạt, không tool/write/external side effect

## Bot Version Result — Kết quả phiên bản Bot

```text
v0.2 trustworthy deterministic history
→ v0.3 grounded A1 advisor with validation/evaluation/fallback
```

Authority ceiling:

```text
analyze + recommend + abstain only
```

## Next Mission — Mission tiếp theo

M03 — First Tracked Manual Publish: learner tự chọn hypothesis, viết/review exact artifact, kiểm disclosure/tracking và tự publish; AI vẫn chỉ advisory.
