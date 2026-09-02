# Bản đồ Mission ↔ Knowledge

Tài liệu này ánh xạ knowledge pull nhỏ nhất cho spine M00–M11. Mission quyết định learner cần build và chứng minh gì; knowledge chỉ được pull khi attempt, evidence hoặc failure làm lộ nhu cầu.

> **V2 authority note:** bảng chi tiết M00–M11 bên dưới là v1 knowledge
> baseline/reference. Active order is M00 market loop → M01 outcome snapshot ∥
> M02 deterministic baseline → M03 history → M04 grounded AI. Lesson IDs are
> preserved knowledge IDs, not v2 sequence. See
> [`CURRICULUM-MIGRATION-v2.md`](CURRICULUM-MIGRATION-v2.md).

## V2 knowledge pull map

| Mission | Pull only when the attempt exposes this gap |
|---|---|
| M00 | offer/audience/channel hypothesis, claim/disclosure/tracking, human review and safe manual publish |
| M01 | measurement source/window/attribution and zero vs missing/pending |
| M02 | minimum deterministic input/decision/abstain and a testable explanation |
| M03 | identity, append-only record, provenance/freshness/reconciliation |
| M04 | grounded advisory, schema/claim validation, fallback/eval |
| M05 | hypothesis, honest comparison, review/version/rollback |

## Ba mức kiến thức

- **REQUIRED** — knowledge slice phải hiểu và áp dụng để Mission PASS.
- **ON-DEMAND** — chỉ pull khi implementation hoặc reality context làm xuất hiện nhu cầu.
- **REFERENCE** — tài liệu đào sâu, không phải PASS gate.

```text
TRY / OBSERVE FIRST
→ PULL THE SMALLEST USEFUL SLICE
→ APPLY IMMEDIATELY
→ EXPLAIN THROUGH THE ARTIFACT
```

`REQUIRED FOR MISSION` không có nghĩa phải học hết một Part hoặc full-pass mọi reference lesson trước khi build.

## V1 baseline part execution map

| Part | Mission | Knowledge outcome |
|---|---|---|
| P0 — First Evidence Decision | M00 | business boundary, evidence literacy, first deterministic decision |
| P1 — Trustworthy Data & Grounded AI | M01–M02 | trustworthy history, grounded AI analysis và evaluation |
| P2 — Publish & Measure | M03–M04 | safe human publish, tracking, attribution và outcome semantics |
| P3 — Improve from Reality | M05 | experiment discipline và versioned improvement |
| P4 — Automatic Observation & Decision | M06–M07 | reliability, signals, decision/abstention và policy |
| P5 — Governed Agent | M08–M10 | read tools, security, approval và bounded automation |
| P6 — Production Closed Loop | M11 | production operation, outcome learning và reviewed deployment |

## V1 baseline AI/authority map

```text
M00–M01 → A0 deterministic
M02–M07 → A1 grounded advisory/read-only
M08     → A2 read-only tool Agent
M09     → A3-shadow
M10     → A3-limited
M11     → A3-production
post-core → A4 multi-agent optional, không bắt buộc
```

AI level mô tả quyền kỹ thuật của Bot, không phải learner PASS.

## V1 M00 — Real public evidence + first human-vs-bot decision

**REQUIRED**

- affiliate money/value flow ở mức đủ biết Bot đang hỗ trợ quyết định nào;
- ethical/compliance boundary tối thiểu: public observation không tạo permission để hành động;
- evidence record: source, `observed_at`, value, freshness và access method;
- phân biệt `fact`, `estimate`, `assumption`, `unknown`;
- human judgment/prediction phải được ghi trước Bot output;
- deterministic baseline ranking và explainable reason;
- Go tối thiểu: terminal, `package`, `func`, data collection nhỏ, edit/run/test và đọc một test failure.

**ON-DEMAND**

- Expected Value slice khi learner thấy commission-rate-only ranking yếu;
- JSON/CSV syntax chỉ khi learner chọn format đó cho observations.

**REFERENCE**

- advanced opportunity scoring, statistics và production architecture.

## M01 — Trustworthy history

**REQUIRED**

- Product/subject identity khác observation snapshot;
- syntax validation khác business/data-quality validation;
- timestamp, provenance, freshness và schema drift;
- append-only history; `missing` khác unchanged/zero;
- change/delta semantics cơ bản;
- Go struct, JSON/CSV/file I/O, error và time ở mức đủ cho implementation.

**ON-DEMAND**

- SQLite/PostgreSQL khi file store không còn đáp ứng query/recovery thật;
- Repository abstraction khi có từ hai storage implementation hoặc test boundary thật;
- indexing/transaction khi workload làm lộ nhu cầu.
- scheduler, context timeout, retry và deduplication được giữ cho M06, khi watcher thật sự xuất hiện.

**REFERENCE**

- warehouse, streaming và distributed storage.

## M02 — Grounded AI advisor

**REQUIRED**

- LLM output là untrusted analysis, không phải fact hoặc permission;
- human/deterministic baseline trước khi thêm AI;
- grounded extraction: claim phải có source/evidence span hoặc bị đánh dấu unsupported;
- structured output và validation;
- confidence không phải xác suất chân lý; uncertainty, missing evidence và abstention;
- small known-label eval set, unsupported-claim case và prompt-injection case;
- provider-neutral adapter, secret handling, latency/cost budget và deterministic fallback.

**ON-DEMAND**

- model routing khi một model không đạt cost/quality requirement;
- retrieval khi evidence set vượt context thực tế;
- caching khi repeated calls tạo cost/latency thật.

**REFERENCE**

- fine-tuning, advanced RAG và multi-model orchestration.

## M03 — Human tracked publish

**REQUIRED**

- product–audience problem/hypothesis đủ để chọn một content angle;
- claim/evidence boundary và prohibited claims;
- disclosure, platform policy và source freshness trước publish;
- content brief, CTA và tracking link;
- exact-artifact human review;
- Decision record: hypothesis, evidence, expected outcome, confidence, uncertainty và outcome window;
- AI-generated suggestion phải được grounded/reviewed; human là actor publish.

**ON-DEMAND**

- channel-specific format/creative pattern khi learner đã chọn channel;
- accessibility, SEO hoặc video production chỉ theo artifact thật;
- account/API integration chưa cần ở Mission này.

**REFERENCE**

- paid distribution, automatic publishing và content-at-scale.

## M04 — Real outcome analytics

**REQUIRED**

- funnel event chain: exposure/impression → click → order → valid/final/paid commission khi nguồn hỗ trợ;
- tracking identifiers và Decision→Action→Outcome linkage;
- test event khác real event;
- `missing` khác `zero`; outcome `pending`, `partial`, `final`;
- attribution window, late event và refund semantics;
- CTR/CVR/commission calculation ở mức đủ dùng;
- preserve raw/source snapshot; AI hypothesis không được overwrite transaction truth.

**ON-DEMAND**

- reconciliation khi hai nguồn thật xung đột;
- privacy/consent requirements theo tracking channel cụ thể;
- advanced multi-touch attribution khi single-touch thật sự không đủ.

**REFERENCE**

- causal attribution, media mix và enterprise analytics.

## M05 — First real improvement

**REQUIRED**

- bottleneck diagnosis từ outcome thật: distribution, click, conversion, validation hoặc measurement;
- hypothesis và expected direction trước change;
- baseline/variant, một thay đổi chính, primary metric, window và stop rule;
- negative/zero/inconclusive là kết quả hợp lệ;
- before/after không tự chứng minh causality;
- AI chỉ đề xuất/giải thích; deterministic/statistical layer giữ measured result;
- Evaluation→ChangeProposal→offline test→review→versioned deploy.

**ON-DEMAND**

- randomization/significance khi traffic và design đủ điều kiện;
- sequential testing khi repeated peeking trở thành vấn đề;
- segmentation khi aggregate outcome che giấu pattern thật.

**REFERENCE**

- bandit, adaptive experimentation và automated optimization.

## M06 — Reliable automatic read/watch

**REQUIRED**

- source access/permission matrix: manual, export, official API hoặc explicitly allowed public source;
- scheduler, context/cancellation và bounded work;
- snapshot/delta/materiality;
- timeout, retry/backoff, idempotency/deduplication;
- freshness, out-of-order và replay handling;
- deterministic alert path, logging/metrics và recovery basics;
- A1 triage chỉ enrich; AI unavailable không được làm mất alert canonical.

**ON-DEMAND**

- concurrency khi sequential collection là bottleneck đo được;
- queue/outbox khi delivery reliability thật yêu cầu;
- durable database khi restart/recovery không thể đáp ứng bằng store hiện tại.

**REFERENCE**

- high-scale event streaming và distributed scheduler.

## M07 — Decision + abstention

**REQUIRED**

- state separation: Signal ≠ Analysis ≠ Decision ≠ Execution;
- evidence fusion từ rule/metric/AI nhưng deterministic policy giữ authority;
- `DecisionPacket`: evidence, confidence method/reason, uncertainty, missing evidence, freshness, expiry;
- `WAIT`, `GET_MORE_DATA`, `HUMAN_REVIEW` là decision hợp lệ;
- RiskLevel và PolicyDecision;
- replay trên stale/missing/conflicting evidence;
- Decision/Outcome Memory ở mức đủ truy lại prediction và outcome.

**ON-DEMAND**

- calibration metric khi có đủ historical cases;
- forecast/ML khi deterministic rule không đáp ứng utility đã đo;
- feature weighting khi evidence thật cho thấy nhu cầu.

**REFERENCE**

- advanced probabilistic decision theory và online learning.

## M08 — Read-only tool Agent

**REQUIRED**

- evidence escalation: chỉ gọi tool khi missing evidence có giá trị;
- explicit Tool Registry: purpose, schema, read/write, permission, risk ceiling, timeout, retry và audit;
- M08 chỉ expose read-only tools;
- least privilege, scoped credential và secret redaction;
- prompt injection boundary: retrieved content không phải instruction/authorization;
- validate arguments/results; allowlist target/source;
- max calls, latency/cost budget và cancellation;
- trajectory eval: tool selection, arguments, unnecessary calls, denial/timeout recovery và evidence coverage.

**ON-DEMAND**

- MCP khi một integration cụ thể tạo interoperability value;
- parallel tool calls khi dependency và budget cho phép;
- retrieval/index khi direct read tools không đủ.

**REFERENCE**

- write tools, arbitrary code execution và multi-agent delegation.

## M09 — Shadow action + durable approval

**REQUIRED**

- `ActionIntent` không phải execution permission;
- deterministic policy; RISK 0/1/2 và `DENY`;
- durable `ApprovalRequest`/decision state;
- approve/reject/expire/cancel;
- revalidation ngay trước execute;
- idempotency key và duplicate callback handling;
- restart/resume, audit và independent kill switch;
- shadow/dry-run/sandbox/owned-draft executor; không public auto-publish.

**ON-DEMAND**

- notification channel khi durable approval core đã chạy;
- compensation khi selected sandbox/draft action có reversible side effect;
- workflow engine khi hand-written state machine không còn đủ.

**REFERENCE**

- broad external write permissions và automatic RISK 2 execution.

## M10 — Limited governed automation

**REQUIRED**

- allowlisted action type/target; default deny;
- bounded R0/R1 policy: scope, time, rate, resource và cost cap;
- RISK 1 mandatory audit; RISK 2 durable approval;
- canary/shadow comparison, rollback/compensation và containment;
- observability: decision/action trace, duplicate prevention, policy blocks, intervention, latency/cost;
- pause/global/action/tool kill switch;
- operator runbook và evidence rằng Bot không vượt authority.

**ON-DEMAND**

- external draft integration khi learner có owned sandbox và scoped credential;
- deployment scheduler/platform khi canary cần chạy bền;
- SLO refinement từ personal actuals, ghi rõ giới hạn `n=1`.

**REFERENCE**

- autonomous public publish/spend/account changes; các action này vẫn RISK 2.

## M11 — Production closed loop

**REQUIRED**

- end-to-end trigger→signal→analysis→decision/abstain→policy→intent→execution→outcome trace;
- process restart/recovery, durable state, backup/restore verification;
- security, least privilege, data retention/privacy và incident containment;
- offline + online evaluation: quality, trajectory, safety, latency/cost và outcome;
- provider-neutral core/adapters và deterministic fallback;
- Decision/Outcome Memory;
- outcome chỉ tạo `ChangeProposal`; production prompt/weight/workflow/policy đổi qua test, review và versioned deploy;
- production runbook, monitoring và rollback.

**ON-DEMAND**

- multi-agent/A2A chỉ khi có independent service/ownership/deployment boundary và measured value;
- advanced ML/routing khi eval chứng minh baseline chưa đủ;
- scale architecture theo measured load.

**REFERENCE**

- unconstrained autonomy và silent self-modification: không thuộc chương trình.

## Quy tắc refine khi author lesson

Mỗi Mission chỉ nên có 3–6 required knowledge cards, ưu tiên 10–25 phút/card. Một card bắt buộc phải:

1. xuất hiện sau attempt/gap tương ứng;
2. chỉ dạy phần cần cho current artifact;
3. có example gắn với Affiliate Bot hiện tại;
4. tạo test/evidence/explain-back ngay;
5. không cung cấp nguyên lời giải Mission.

Khi lesson IDs mới được chốt, map từng theme ở trên vào **tập ID nhỏ nhất**. Không phục hồi một inventory lớn chỉ để tạo cảm giác đầy đủ.
