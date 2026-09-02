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
2. Với tool có thể chạm personal/customer/account data, thử một query trả **nhiều dữ liệu hơn task cần** để quan sát data-minimisation gap trước khi harden contract.
3. M09: Agent có thể **propose** `ActionIntent`; Go risk policy phân loại; n8n chạy shadow/durable approval path. Thử duplicate/expired approval, changed context và process restart.
4. M10: chạy limited RISK0/RISK1 canary qua bounded executor; RISK2 vẫn phải qua durable approval + context revalidation + kill switch.

## Core checklist

### Chương 15 — Explicit tool contracts và read-only AgentRuntime

- [ ] **15.1** — Tool input/output schema, validation, permission và risk ceiling
- [ ] **15.2** — Read-only evidence escalation và Tool Registry
- [ ] **15.3** — Tool failure, timeout, retry, idempotency và audit

Canonical M08 path:

```text
GET_MORE_DATA
→ AgentRuntime receives task + allowed Tool Registry
→ read-only tool calls within permission + data scope
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

hoặc:

```text
Agent may read dataset
→ therefore Agent should collect/store every field
```

Permission phải explicit theo task/session/tool contract. Khi dữ liệu có privacy relevance, áp dụng `DataAccessContext` từ [`AGENT-SECURITY-AND-TOOL-GOVERNANCE.md`](../docs/AGENT-SECURITY-AND-TOOL-GOVERNANCE.md): purpose, minimum data, retention, downstream sharing và redaction.

Invariant:

```text
read-only
≠ privacy-safe by default
```

### Chương 16 — Policy, risk và approval

- [ ] **16.1** — ActionIntent và deterministic RISK0/RISK1/RISK2 policy
- [ ] **16.2** — Durable approval, expiry, reject reason và context revalidation
- [ ] **16.3** — Least privilege, secrets, prompt injection boundary và kill switch

C16.3 dùng `least privilege` theo hai lớp:

```text
PERMISSION LEAST PRIVILEGE
= tool/credential/action scope tối thiểu

DATA LEAST PRIVILEGE
= purpose + minimum necessary data + retention + downstream sharing + redaction
```

Ownership:

```text
Agent
→ may propose ActionIntent

Go Policy
→ classifies RISK / ALLOW / DENY / REQUIRE_APPROVAL

n8n
→ routes resulting workflow
```

n8n IF/Switch node không được tự reclassify `RISK2` thành auto-executable. Orchestrator cũng không được log/forward raw personal data ngoài `DataAccessContext` chỉ vì integration node hỗ trợ.

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

Audit trace phải giữ đủ metadata để biết data access/purpose khi relevant nhưng không mặc định copy raw sensitive payload vào trace.

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
- data-scope/minimisation compliance khi relevant;
- prompt-injection resistance;
- auditability không leak secret/full personal data;
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

Approval cho Action không tự cấp permission thu thêm data ngoài purpose/scope đã định.

## M10 — Limited governed automation

RISK0/RISK1 chỉ auto execute khi deterministic policy cho phép và canary scope đã khai báo.

RISK2:

```text
valid ActionIntent
+ Go Policy requires approval
+ durable human approval
+ current-context revalidation
+ data/action scope still valid
+ kill switch clear
→ execution may proceed
```

Thiếu bất kỳ gate nào → no execution.

## Cross-runtime failure cases

Bắt buộc test:

```text
Agent unavailable/bad output
→ reject/fallback

read-only tool returns excess personal data
→ minimise/redact/reject outside purpose

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
- [ ] Read-only tool có privacy relevance không được lấy/giữ/share dữ liệu vượt purpose/minimum scope
- [ ] CandidateEvidence phải qua Go validation/grounding trước khi thành canonical evidence
- [ ] Audit giữ traceability nhưng không mặc định lưu raw secret/full personal data
- [ ] Agent proposal không tự trở thành ActionIntent được authorize
- [ ] n8n không bypass deterministic Go risk/policy result
- [ ] RISK2 không execute nếu thiếu valid approval và revalidation
- [ ] Restart/duplicate approval/workflow không tạo side effect trùng
- [ ] Kill switch chặn execution kể cả khi approval đã tồn tại
- [ ] Agent/n8n framework có thể thay mà không đổi Mission outcome/contracts

[← Part trước](part-04.md) · [Roadmap tổng](../ROADMAP.md) · [Part tiếp theo →](part-06.md)
