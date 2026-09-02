---
mission_id: "M02"
title: "Grounded AI Advisor"
status: ready
curriculum_version: 1
release_kind: "bot"
requires_missions: ["M01"]
bot_version_from: "v0.2"
bot_version_to: "v0.3"
estimated_hours: 12
delivery:
  starter_paths:
    - "lab/learner/affiliate-bot/"
  eval_pack: null
  verification_commands:
    - "cd lab/learner/affiliate-bot && go test ./..."
  pilot_status: untested
  pilot_evidence_refs: []
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

Nâng Bot v0.2 thành v0.3 bằng một A1 advisory layer có thể bị từ chối hoàn toàn mà **core deterministic decision vẫn sống**:

```text
validated E1 history
→ deterministic baseline FIRST
→ decide CALL_AI | SKIP_AI
→ untrusted AI output
→ strict schema validation
→ evidence-ref existence check
→ claim-support check
→ grounded advisory OR reject/fallback/abstain
→ no scoring mutation / no Action
```

AI ở M02 là **advisor**, không phải source of truth, scorer, tool user hay execution actor.

Hai rule không được phá:

```text
AI confidence ≠ evidence
AI recommendation ≠ execution permission
```

Và ở M02:

```text
AI advisory
≠ permission to mutate deterministic scoring facts/inputs
```

Nếu AI đề xuất `audience_fit = 0.9`, `CVR = 3%` hoặc bất kỳ số nào source không đo, Bot không được tự ghi số đó vào Product/history/scoring input như measured fact.

## Learner workspace

Tiếp tục trên cùng Bot của người học:

```text
lab/learner/affiliate-bot/
```

Reference implementation không phải starting state. Không copy reference rồi coi là PASS.

## Starting Bot State — Trạng thái Bot ban đầu

Chỉ bắt đầu M02 sau khi M01 PASS:

- Bot v0.2 có deterministic ranking/abstention;
- E1 history append-only có stable identity/provenance;
- delta/freshness behavior deterministic;
- invalid/missing/conflicting data có behavior rõ;
- history survive restart;
- chưa có trusted AI domain output, grounding gate hoặc AI evaluation.

Nếu M01 chưa Reality/Operated PASS, tiếp tục engineering bằng fixture được gắn nhãn nhưng **không tuyên bố M02 Reality verified**.

## Try First — Thử trước

### Checkpoint 1 — Chứng minh baseline trước AI

1. Chọn một eval subset 5–10 cases từ E1 history M00–M01.
2. **Trước khi xem AI output**, human label cho từng case:
   - facts source thực sự hỗ trợ;
   - field/claim source không hỗ trợ;
   - missing evidence;
   - deterministic baseline output/limitation mong đợi.
3. Chạy deterministic Bot và freeze output/version.
4. Với từng case, ghi một trong hai:

   ```text
   CALL_AI because <unstructured information question worth asking>
   SKIP_AI because <deterministic evidence already sufficient / value too low>
   ```

5. Ghi expected information value bằng ngôn ngữ định tính; M02 không bắt numeric ROI của model call.
6. **Sau attempt mới pull `5.1`.**

### Checkpoint 2 — Để output AI chưa tin cậy thất bại trước mắt

Dùng provider-neutral fixture/replay trước để không phụ thuộc billing/API key.

Chạy ít nhất:

1. valid structured + actually grounded claim;
2. malformed schema;
3. evidence ref không tồn tại;
4. evidence ref tồn tại nhưng **không support claim**;
5. hypothesis được trình bày như fact.

Quan sát điều gì sẽ xảy ra nếu code chỉ parse JSON rồi tin output.

**Sau attempt mới pull `5.2`** và xây schema + grounding gate.

### Checkpoint 3 — Evaluation + fallback + trust boundary

Chạy ít nhất:

1. valid grounded replay/live case;
2. invalid schema;
3. unsupported claim;
4. provider unavailable/timeout fixture;
5. malicious public Product text/prompt-injection fixture;
6. skip-call case;
7. secret/log redaction case.

Chứng minh invalid/unavailable AI **không xóa hoặc thay đổi deterministic baseline**.

**Sau attempt mới pull `5.3`.**

## Execution kind — replay khác live

M02 bắt buộc ghi rõ AI execution evidence:

```text
advisor_execution_kind: replay | live
```

### `replay`

Saved response/fixture dùng để chứng minh:

- parser/schema validation;
- grounding gate;
- unsupported-claim rejection;
- fallback;
- prompt-injection boundary;
- reproducible evaluation.

Replay **không chứng minh provider live đang hoạt động**.

### `live`

Live provider call có thể chứng minh integration thực tế nếu learner có access hợp lệ.

Live call là optional cho Core M02. Không yêu cầu learner mua paid API, commit secret hoặc gửi private data chỉ để PASS.

Nếu live chưa chạy:

```text
live_provider_verified: pending
```

không được relabel replay thành live.

## Provider-neutral advisory contract

Provider response object không được trở thành domain contract.

Một normalized advisory tối thiểu có thể có shape tương đương:

```yaml
advisor_execution_kind: replay
advisor_version:
input_evidence_refs: []
invocation_reason:
status: grounded | rejected | unavailable | skipped
facts:
  - claim:
    evidence_refs: []
    support: supported | unsupported | unknown
hypotheses:
  - claim:
    evidence_refs: []
missing_evidence: []
uncertainty: []
fallback_used: false
```

Exact Go struct có thể khác, nhưng semantics phải giữ.

## Grounding contract — hai tầng bắt buộc

Một evidence ref tồn tại chưa đủ để biến claim thành grounded.

### Gate 1 — Reference validity

```text
claim.evidence_ref
→ ref có tồn tại trong evidence set đang xét không?
```

Không tồn tại → `rejected`.

### Gate 2 — Claim support

```text
ref tồn tại
→ evidence content có thực sự support claim này không?
```

Ví dụ:

```text
AI claim: "Product X có CVR 12%"
Evidence OBS-X: chỉ có price + commission_rate
```

Dù `OBS-X` tồn tại, claim vẫn **unsupported**.

Với structured factual extraction, ưu tiên field-addressable support:

```yaml
claim_kind: fact
field: price
value: 299000
evidence_ref: OBS-X
evidence_field: price
```

Bot có thể deterministic-check value/ref/field tốt hơn.

Với interpretation không thể trực tiếp verify, giữ:

```text
hypothesis
```

không tự nâng thành `fact`.

## AI scoring authority ceiling

Ở M02 accepted AI output có thể:

- tóm tắt evidence;
- extract candidate structured facts để grounding gate kiểm;
- nêu hypothesis;
- nêu missing evidence;
- nêu uncertainty;
- đề xuất next measurement;
- hỗ trợ human analysis.

AI output **không được tự động**:

- sửa `price`, `commission_rate`, outcome hoặc provenance đã quan sát;
- tạo measured CVR/EV từ assumption;
- ghi candidate AI value vào canonical history như observed fact;
- thay deterministic score/rank chỉ vì model nói “nên chọn X”;
- cấp tool/write/action authority.

Nếu sau này muốn AI-derived signal đi vào scoring, cần Mission/Decision contract sau với evaluation và governance tương ứng; không kéo vào M02.

## Invocation decision — khi nào CALL_AI?

M02 không dạy “có AI thì gọi mọi lúc”.

Mental model:

```text
Deterministic rule đủ?
├─ yes → SKIP_AI
└─ no
   ↓
Có câu hỏi unstructured cụ thể?
├─ no → GET_MORE_DATA / deterministic path
└─ yes
   ↓
Expected information value > cost/risk?
├─ no → SKIP_AI
└─ yes → CALL_AI
```

Không cần một công thức monetary hoàn chỉnh. Learner phải nói được **AI sẽ giảm uncertainty nào** trước khi gọi.

## Run — Chạy

Từ learner workspace:

```bash
cd lab/learner/affiliate-bot
go test ./...
```

Executable path có thể khác implementation, nhưng output phải inspectable tương đương:

```text
Bot version: v0.3
Deterministic baseline: <decision + reasons>
AI invocation: CALL_AI | SKIP_AI
AI invocation reason: <reason>
AI execution kind: replay | live
AI status: grounded | rejected | unavailable | skipped
AI advisory:
  facts: <claim + evidence refs + support>
  hypotheses:
  missing evidence:
  uncertainty:
Fallback used: true | false
Final authority: advisory only
```

Khi `rejected` hoặc `unavailable`:

```text
Deterministic baseline vẫn giữ nguyên
Fallback used: true
```

## Observe — Quan sát

Lưu:

- deterministic baseline trước AI;
- human labels trước AI;
- vì sao call/skip;
- malformed/unsupported output trông thuyết phục như thế nào trước gate;
- ref tồn tại nhưng không support claim ở đâu;
- hypothesis nào dễ bị model trình bày quá chắc;
- fallback có thực sự giữ core output không;
- replay/live evidence khác nhau thế nào;
- latency/cost chỉ khi đo được;
- field nào không được phép trở thành scoring fact.

## Knowledge Pull — Lấy kiến thức đúng lúc

### Sau Checkpoint 1

- `5.1` — deterministic rule hay AI theo decision value/information value.

### Sau Checkpoint 2

- `5.2` — structured advisory, claim kind, evidence refs, claim-support grounding và uncertainty.

### Sau Checkpoint 3

- `5.3` — eval set, invalid-output rejection, fallback, injection boundary, cost/latency/privacy và replay-vs-live evidence.

Mỗi lần pull tối đa slice cần để sửa gap vừa quan sát. Không đọc provider SDK dài trước khi domain contract rõ.

## Improve — Cải tiến

- thêm provider-neutral `Advisor` boundary nhỏ;
- giữ provider response ở adapter edge;
- normalize output sang Bot advisory schema;
- strict reject malformed/unknown material fields;
- check evidence-ref existence;
- check claim support;
- tách facts / hypotheses / missing evidence;
- fallback deterministic;
- log invocation reason/status/execution kind/version;
- log latency/cost khi thật sự đo được;
- redact secret/sensitive values;
- giữ AI khỏi scoring mutation và write authority.

## Tests — Kiểm thử

Acceptance tests tối thiểu:

- deterministic baseline chạy khi không có Advisor;
- `SKIP_AI` không cần provider;
- valid grounded output được accept;
- malformed/wrong-type/unknown material field bị reject;
- nonexistent evidence ref bị reject;
- ref tồn tại nhưng không support claim bị reject/downgrade hypothesis;
- hypothesis không được serialize như observed fact;
- unsupported claim không mutate Product/history/scoring fact;
- timeout/unavailable dùng deterministic fallback;
- malicious Product text không đổi system/domain instruction hoặc authority;
- replay case reproducible;
- replay không bị report là live;
- secret không xuất hiện trong output/log fixture;
- M00/M01 deterministic behavior không regression.

## Evaluation contract

M02 mới có E1, chưa có business outcome analytics E3.

Do đó eval được phép đo:

```text
schema validity
reference validity
claim-support rate
unsupported-claim count/rate
human-labelled extraction correctness
fallback correctness
skip/call correctness theo rubric
latency (nếu live)
cost (nếu live/measured)
```

Không được tuyên bố từ M02 rằng:

```text
AI tăng conversion
AI tăng revenue
AI ranking business tốt hơn
```

vì chưa có outcome evidence.

Metric câu hỏi đúng là:

> AI có thêm **analysis/information utility** trên eval set hiện tại mà vẫn giữ grounding/fallback không?

Business lift chỉ được đánh giá khi Mission sau có Action/Outcome evidence phù hợp.

## Reality Check — Kiểm chứng thực tế

**Minimum:** E1.

- advisor input grounding cases phải dùng public E1 history thật từ M00–M01;
- human labels phải tồn tại trước AI output trên eval subset;
- accepted material fact phải có evidence refs **và support check**;
- `evidence_kind` của input tách khỏi `advisor_execution_kind`/`ai_status`;
- malicious/schema/failure fixtures có thể synthetic nhưng không thay E1 grounding cases;
- replay/live được ghi trung thực.

M02 không có business outcome window và không có external Action.

## Operate — Vận hành

Chạy tối thiểu:

1. baseline-only / Advisor absent;
2. `SKIP_AI` case;
3. valid grounded advisory;
4. invalid-schema case;
5. nonexistent-ref case;
6. existing-ref-but-unsupported-claim case;
7. unavailable/timeout fallback;
8. malicious-content/injection case;
9. replay reproducibility case;
10. optional live case nếu access hợp lệ.

Lưu evidence/model/fixture/workflow version đủ để replay.

## Failure Case — Tình huống lỗi

- malformed JSON/structured output;
- wrong type hoặc unknown material field;
- evidence ref không tồn tại;
- evidence ref tồn tại nhưng không support claim;
- AI nâng hypothesis thành fact;
- confidence cao nhưng evidence thiếu;
- AI candidate value cố chảy vào deterministic scoring facts;
- prompt injection trong public Product text;
- timeout/rate-limit/unavailable;
- excessive cost/latency;
- replay bị relabel live;
- secret/raw sensitive value lọt log.

Behavior đúng là reject, downgrade-to-hypothesis, redact, fallback, skip hoặc abstain. Không “sửa hộ” unsupported claim rồi silently accept.

## Safety Gate — Cổng an toàn

**S1 — AI Advisory. Authority ceiling: analyze/recommend/abstain only.**

Bắt buộc:

- deterministic baseline trước AI;
- model output là untrusted input;
- structured validation + two-stage grounding;
- call/skip reason;
- fallback;
- no tools;
- no internal/external write authority;
- no scoring mutation from unverified AI claim;
- Decision khác Execution.

Public Product text là **untrusted data**, không phải instruction, policy, permission hoặc tool command.

M02 không publish, send, spend, order, change account hay execute transaction.

## Evidence — Bằng chứng

Lưu dưới `artifacts/missions/M02/`:

- human-labeled eval subset frozen trước AI;
- deterministic baseline output/version;
- call/skip decisions + reasons;
- accepted grounded output;
- malformed/nonexistent-ref/unsupported-claim rejection outputs;
- fallback/unavailable output;
- prompt-injection case;
- advisory schema + adapter/interface version;
- replay/live classification evidence;
- evaluation summary trong scope E1;
- privacy/secret-log check;
- learner commit + authority note.

Evidence chain:

```text
Observation/History(E1)
→ deterministic BotDecision baseline
→ CALL_AI | SKIP_AI
→ untrusted AI output
→ schema + reference + claim-support gate
→ grounded Analysis OR reject/fallback
→ human-visible advisory
→ no scoring mutation / no Action
```

## Explain-back — Giải thích lại

Learner phải trỏ vào case/code/evidence của mình để giải thích:

1. Vì sao deterministic baseline phải tồn tại trước AI?
2. Khi nào `SKIP_AI` tốt hơn `CALL_AI`?
3. Grounded claim khác câu trả lời “nghe hợp lý” thế nào?
4. Vì sao evidence ref tồn tại vẫn chưa đủ?
5. Fact, hypothesis và missing evidence được tách ở đâu?
6. Vì sao confidence không thay evidence support?
7. Vì sao AI không được mutate scoring facts ở M02?
8. Khi AI invalid/unavailable, baseline sống thế nào?
9. Product text prompt injection bị chặn ở trust boundary nào?
10. Replay chứng minh gì và không chứng minh gì so với live?
11. Eval M02 chứng minh analysis utility gì nhưng chưa chứng minh business lift gì?
12. AI output hiện được phép làm gì và không được phép làm gì?

## Mission PASS — Tiêu chí PASS

### Capability

- [ ] deterministic baseline chạy độc lập
- [ ] explicit `CALL_AI | SKIP_AI` behavior + reason
- [ ] provider-neutral advisory contract
- [ ] strict schema validation
- [ ] evidence-ref existence check
- [ ] claim-support check
- [ ] facts/hypotheses/missing evidence tách rõ
- [ ] unsupported AI claim không mutate scoring facts/history
- [ ] invalid/unavailable cases reject/fallback đúng
- [ ] injection/privacy/eval cases đạt
- [ ] replay/live classification đúng
- [ ] required lessons được pull sau attempt và explain-back đạt

### Reality

- [ ] accepted grounding cases dùng E1 history thật
- [ ] human labels tồn tại trước AI output
- [ ] accepted material facts có refs + support
- [ ] sample/synthetic chỉ dùng failure/safety khi phù hợp
- [ ] replay không bị trình bày là live
- [ ] không claim business lift từ E1-only evaluation

### Operated

- [ ] chạy baseline, skip, valid, invalid, unsupported, fallback, injection và replay cases
- [ ] same replay fixture tạo reproducible result
- [ ] deterministic core vẫn chạy khi Advisor absent/unavailable
- [ ] S1 đạt, không tool/write/scoring-mutation/external side effect

## Bot Version Result — Kết quả phiên bản Bot

Chỉ bump sau khi Capability + Reality + Operated đều đạt:

```text
v0.2 trustworthy deterministic history
→ v0.3 grounded A1 advisor with validation/evaluation/fallback
```

Authority ceiling:

```text
analyze + recommend + abstain only
```

## Next Mission — Mission tiếp theo

M03 — First Tracked Manual Publish: human tạo/review exact artifact và tự publish; AI vẫn advisory, không có publish tool.
