# AI Capability Levels — Năng lực và quyền A0–A4

Tài liệu này chuẩn hóa progression của AI/Agent theo spine M00–M11. Capability level mô tả **Bot được phép làm gì**, không mô tả learner giỏi tới đâu và không tự tạo execution permission.

```text
INTELLIGENCE
≠ MODEL FLUENCY
≠ TOOL ACCESS
≠ EXECUTION AUTHORITY
```

Bot chỉ được nâng level khi evidence, evaluation, failure controls và business value của level trước đã đạt.

## A0 — Deterministic Baseline

**Core Mission:** M00–M03; M00/M01 are human/manual and M02/M03 are the
first deterministic baseline/history stages. Deterministic core tiếp tục tồn
tại ở mọi Mission sau.

Cho phép:

- validation và data-quality checks;
- append-only snapshots/history;
- deterministic score/rank/metric;
- rule, delta, materiality và scheduler;
- explicit `UNKNOWN`/error state.

Không cần model call. A0 là baseline để đánh giá AI, không phải giai đoạn “kém thông minh”. Một baseline explainable dùng evidence đúng tốt hơn một AI output không grounded.

**Upgrade gate sang A1:**

- learner hiểu evidence/schema đang phân tích;
- có human hoặc deterministic expected output;
- đã có invalid/missing evidence cases;
- model adapter có scope và cost boundary.

## A1 — Grounded Advisory / Read-Only

**Core Mission:** M04–M07.

Cho phép:

- extract structured facts từ evidence được cung cấp;
- summarize/classify/correlate;
- nêu hypothesis và missing evidence;
- explain ranking/anomaly/outcome;
- recommend investigation/decision candidate;
- abstain hoặc yêu cầu human review.

Bắt buộc:

- structured output validation;
- source/evidence refs cho material claim;
- confidence method/reason và uncertainty;
- known-label/failure evaluation;
- latency/cost trace;
- deterministic fallback khi capability chính không cần AI.

A1 không có external execution authority. M00 public publish là **human action** sau exact-artifact review, compliance và tracking gate; không phải AI publish.

```text
AI AnalysisPacket
→ deterministic/human Decision boundary
→ no AI external execute
```

**Upgrade gate sang A2-RO:**

- A1 grounded/eval evidence đạt;
- missing evidence use case rõ;
- read tool contract và permissions được thiết kế;
- malicious/unsupported content cases tồn tại;
- call/cost/time budget chấp nhận được.

## A2-RO — Read-Only Tool Agent

**Core Mission:** M08.

Agent được phép chọn và gọi **chỉ read-only tools** để lấy missing evidence. Mỗi tool phải khai báo:

- purpose và input/output schema;
- read-only category;
- allowed source/target;
- required permission và scoped credential;
- risk ceiling;
- timeout/retry/cancellation;
- call/cost budget;
- audit fields.

Bắt buộc đánh giá trajectory:

- tool selection và argument accuracy;
- unnecessary calls;
- permission denial behavior;
- timeout/tool failure recovery;
- evidence coverage;
- prompt injection resistance;
- final claim truy được về tool result/source.

Tool description, retrieved content và result vẫn là untrusted input. M08 không expose write tool; model không được tự mở rộng registry hoặc permission.

**Upgrade gate sang A3-shadow:**

- read-tool trajectory đạt;
- external/internal write use case có business value rõ;
- exact side effect và rollback/compensation được mô tả;
- deterministic policy/risk model tồn tại;
- durable approval/idempotency/kill-switch design sẵn sàng.

## A3 — Governed Action Agent

A3 có ba phase. Không được bỏ qua shadow để đi thẳng vào production.

### A3-shadow — M09

Agent tạo `ActionIntent`; executor chỉ dry-run, sandbox hoặc owned draft scope.

```text
ActionIntent
→ deterministic PolicyDecision
→ RiskLevel
→ durable ApprovalRequest khi cần
→ pause / approve / reject / expire / cancel
→ revalidate
→ shadow/sandbox execute hoặc terminate
→ audit
```

Bắt buộc:

- persistent workflow state;
- restart/resume;
- approval expiry và changed-context revalidation;
- idempotency/duplicate callback prevention;
- independent kill switch;
- model không tự assign permission hoặc approve action của mình.

### A3-limited — M10

Cho phép automatic execution chỉ với action đã allowlist và bound rõ:

```text
RISK 0 → internal/read-only auto
RISK 1 → bounded/reversible auto + mandatory audit
RISK 2 → durable Human Approval + revalidation
DENY   → prohibited regardless of approval
```

Mỗi canary phải có action/target allowlist, time/rate/resource/cost cap, monitoring, rollback/containment và operator stop path.

Public publish, spend, account/platform settings, destructive data change và consequential external communication mặc định là RISK 2.

### A3-production — M11

Giữ nguyên policy boundary của M10 và bổ sung:

- production recovery và durable state;
- decision/tool/action/outcome trace;
- offline + online evaluation;
- least privilege, retention/privacy và incident response;
- SLO/cost/quality/safety metrics;
- Decision/Outcome Memory;
- versioned improvement qua test/review/deploy.

Outcome không cho Agent quyền tự rewrite production prompt, weights, workflow hoặc policy.

## A4 — Multi-Agent Optional Advanced

A4 không phải core Mission và không phải thước đo “Bot trưởng thành”. Chỉ cân nhắc sau M11 khi có independent service/ownership/deployment boundary thật, ví dụ Product Intelligence và Revenue Intelligence được vận hành như hai service độc lập.

Không dùng multi-agent chỉ để workflow trông nâng cao hơn. Interface/function/workflow trong một application thường đơn giản, rẻ và dễ audit hơn.

A2A/MCP hoặc protocol tương đương là implementation choice, không phải curriculum dependency mặc định. Mọi agent vẫn chịu cùng Tool Registry, Policy/Risk, approval, audit và kill switch.

## Policy `DENY`

Một số action không được chuyển thành RISK 2 rồi cho phép chỉ vì human approve:

- fake/artificial clicks, orders hoặc engagement;
- spam hoặc consequential communication trái permission;
- né disclosure hoặc tạo unsupported/deceptive claims;
- bypass platform policy/control;
- restricted/private scraping;
- credential sharing hoặc quyền rộng không cần thiết;
- unbounded spend;
- để Agent sửa control đang giới hạn chính nó.

Policy Engine phải trả `DENY` cho các case này.

## Ma trận quyền

| Capability | A0 | A1 | A2-RO | A3-shadow | A3-limited | A3-production | A4 optional |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| deterministic compute | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| grounded AI analysis | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| read tools | — | giới hạn/context được cấp | allowlisted | allowlisted | allowlisted | allowlisted | allowlisted |
| internal write | — | — | — | shadow/draft | bounded policy | governed | governed |
| external side effect | — | — | — | sandbox/owned draft only | R0/R1 bounds; R2 approval | governed | governed |
| durable approval | — | — | — | bắt buộc theo policy | R2 | R2 | R2 |
| auto public publish/spend/settings | — | — | — | — | —, R2 approval | —, R2 approval | —, R2 approval |
| multi-agent | — | — | — | — | — | không mặc định | optional |

## Quy tắc nâng cấp chung

Không nâng level chỉ vì model/framework/tool mới tồn tại. Phải có:

1. business value và use case cụ thể;
2. human/deterministic baseline;
3. real evidence phù hợp scope;
4. known failure/threat cases;
5. offline evaluation đạt;
6. permission/risk/approval boundary;
7. fallback và acceptable operational cost;
8. operated evidence trước khi tăng authority.

## Invariants

```text
MODEL OUTPUT = UNTRUSTED INPUT
DECISION ≠ EXECUTION
ACTIONINTENT ≠ PERMISSION
CAPABILITY LEVEL ≠ LEARNER PASS
REALITY EVIDENCE ≠ SYNTHETIC FIXTURE
OUTCOME ≠ AUTHORITY TO SELF-MODIFY
```
