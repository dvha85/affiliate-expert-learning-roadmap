# Phần 5 — Tool Agent và tự động hóa Hybrid có quản trị

- Timeline: **Evidence-gated; authority increases only after safety cases pass**.
- **Chapters:** C15–C17
- **Core:** 9 micro-lessons
- **Missions:** M08–M10
- **Outcome:** AgentRuntime dùng explicit read-only tools để lấy missing evidence; Go giữ Tool/Decision/Policy contracts; n8n orchestration xử lý shadow/approval/bounded execution mà không bypass deterministic authority.

## Hybrid ownership trong Part 05

```text
AgentRuntime
= investigate + read-only tool use + propose

Go
= Tool Registry contract + validation + ActionIntent + deterministic risk/policy + authorization

n8n
= invoke/route Agent + shadow workflow + durable approval routing + bounded execution

Human
= approve/reject RISK2 và consequential action theo Mission gate
```

Hermes Agent là **primary Agent runtime reference/candidate** để spike ở M08. Canonical curriculum khóa `AgentRuntime`/`Tool Registry` contract, không khóa vendor.

## Attempt trước knowledge pull

1. M08: để Agent xử lý một case thiếu evidence nhưng chỉ expose explicit read-only tools. So với manual/deterministic retrieval baseline.
2. M09: Agent có thể **propose** `ActionIntent`; Go risk policy phân loại; n8n chạy shadow/durable approval path. Thử duplicate/expired approval, changed context và process restart.
3. M10: chạy limited RISK0/RISK1 canary qua bounded executor; RISK2 vẫn phải qua durable approval + context revalidation + kill switch.

## Core checklist

### Chương 15 — Explicit tool contracts và read-only AgentRuntime

- [ ] **15.1** — Tool input/output schema, validation, permission và risk ceiling
- [ ] **15.2** — Read-only evidence escalation và Tool Registry
- [ ] **15.3** — Tool failure, timeout, retry, idempotency và audit

Canonical M08 path:

```text
GET_MORE_DATA
→ AgentRuntime receives task + allowed Tool Registry
→ read-only tool calls
→ CandidateEvidence
→ Go validate / ground
→ DecisionPacket
```

Không cho phép:

```text
Agent tool result
→ silently become measured fact
```

hoặc:

```text
Agent sees a tool
→ therefore Agent may call it
```

Permission phải explicit theo task/session/tool contract.

### Chương 16 — Policy, risk và approval

- [ ] **16.1** — ActionIntent và deterministic RISK0/RISK1/RISK2 policy
- [ ] **16.2** — Durable approval, expiry, reject reason và context revalidation
- [ ] **16.3** — Least privilege, secrets, prompt injection boundary và kill switch

Ownership:

```text
Agent
→ may propose ActionIntent

Go Policy
→ classifies RISK / ALLOW / DENY / REQUIRE_APPROVAL

n8n
→ routes resulting workflow
```

n8n IF/Switch node không được tự reclassify `RISK2` thành auto-executable.

### Chương 17 — Durable action workflow

- [ ] **17.1** — Persisted state, checkpoint, restart và resume/terminate
- [ ] **17.2** — Dry-run, controlled executor và duplicate-side-effect prevention
- [ ] **17.3** — Trace decision, tool, policy, approval, action và result

Primary orchestration reference:

```text
DecisionPacket
→ Go creates ActionIntent
→ Go PolicyDecision
→ n8n shadow/dry-run workflow
→ durable approval if required
→ context revalidation
→ controlled executor
→ ExecutionRecord
```

## M08 — Agent authority ceiling

```text
A2-RO
read-only tools only
no external write
```

Hermes/reference spike phải test:

- evidence correctness/grounding;
- unsupported claim rate;
- tool-call success/failure;
- permission compliance;
- prompt-injection resistance;
- auditability;
- latency/cost;
- fallback khi Agent unavailable.

Agent unavailable phải fallback về deterministic/manual evidence path thay vì làm core decision contract biến mất.

## M09 — Shadow authority ceiling

```text
Agent may propose
Go may classify
n8n may dry-run/route approval
no consequential execution from Agent proposal alone
```

Approval phải durable và gắn với:

- exact ActionIntent/version;
- context/evidence snapshot;
- expiry;
- approver/reject reason;
- revalidation result.

## M10 — Limited governed automation

RISK0/RISK1 chỉ auto execute khi deterministic policy cho phép và canary scope đã khai báo.

RISK2:

```text
valid ActionIntent
+ Go Policy requires approval
+ durable human approval
+ current-context revalidation
+ kill switch clear
→ execution may proceed
```

Thiếu bất kỳ gate nào → no execution.

## Cross-runtime failure cases

Bắt buộc test:

```text
Agent unavailable/bad output
→ reject/fallback

n8n duplicate/restart
→ no duplicate side effect

approval expired/context changed
→ revalidation fails / no execution

Go Policy unavailable
→ no consequential execution

kill switch ON
→ execution blocked even with prior approval
```

## Part PASS

- [ ] M08–M10 đều có Capability PASS, Reality verified và Operated
- [ ] Agent không thể gọi tool ngoài registry/permission
- [ ] CandidateEvidence phải qua Go validation/grounding trước khi thành canonical evidence
- [ ] Agent proposal không tự trở thành ActionIntent được authorize
- [ ] n8n không bypass deterministic Go risk/policy result
- [ ] RISK2 không execute nếu thiếu valid approval và revalidation
- [ ] Restart/duplicate approval/workflow không tạo side effect trùng
- [ ] Kill switch chặn execution kể cả khi approval đã tồn tại
- [ ] Agent/n8n framework có thể thay mà không đổi Mission outcome/contracts

[← Part trước](part-04.md) · [Roadmap tổng](../ROADMAP.md) · [Part tiếp theo →](part-06.md)
