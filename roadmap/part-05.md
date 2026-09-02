# Phần 5 — Tool Agent và tự động hóa Hybrid có quản trị

- Timeline: **Evidence-gated; authority increases only after safety cases pass**.
- **Chapters:** C15–C17
- **Core:** 9 micro-lessons
- **Missions:** M08–M10
- **Outcome:** AgentRuntime dùng explicit read-only tools để lấy missing evidence; Deterministic Core giữ Tool/Decision/Policy contracts; n8n orchestration xử lý shadow/approval/bounded execution mà không bypass deterministic authority.

## Hybrid ownership trong Part 05

```text
AgentRuntime
= investigate + read-only tool use + propose
= n8n AI Agent là visual-first candidate ở M08
= Hermes/OpenAI Agents SDK chỉ compare khi có measured bottleneck

Deterministic Core
= Tool Registry contract + validation + ActionIntent + deterministic risk/policy + authorization
= Go reference/fallback; reviewed visual rule engine có thể implement policy sau parity gate

n8n
= invoke/route Agent + shadow workflow + durable approval routing + bounded execution

Human
= approve/reject RISK2 và consequential action theo Mission gate
```

Canonical curriculum khóa `AgentRuntime`/`Tool Registry` contract, không khóa vendor. Ở M08, ưu tiên spike **n8n AI Agent** trước vì n8n đã là orchestration runtime; chỉ thêm Hermes/OpenAI Agents SDK nếu visual-first baseline lộ limitation đo được.

DecisionRules hoặc deterministic visual rule engine tương đương có thể được cân nhắc cho policy từ M09 **chỉ sau** khi M07 comparison đã có parity/reason/version/fail-closed evidence. Go vẫn là fallback nếu visual rule không đủ rõ hoặc an toàn.

## Attempt trước knowledge pull

1. M08: để n8n AI Agent hoặc AgentRuntime candidate đơn giản nhất xử lý một case thiếu evidence nhưng chỉ expose explicit read-only tools. So với manual/deterministic retrieval baseline.
2. Với tool có thể chạm personal/customer/account data, thử một query trả **nhiều dữ liệu hơn task cần** để quan sát data-minimisation gap trước khi harden contract.
3. Chỉ nếu n8n AI Agent baseline thật sự thiếu capability/isolated runtime/auditability, compare Hermes hoặc OpenAI Agents SDK trên cùng fixture/eval set.
4. M09: Agent có thể **propose** `ActionIntent`; Deterministic Policy Authority phân loại; n8n chạy shadow/durable approval path. Thử duplicate/expired approval, changed context và process restart.
5. M09: nếu visual rule candidate đã có parity baseline, thử policy table trên cùng canonical cases; AI có thể hỗ trợ draft rule nhưng **không được auto-publish rule**.
6. M10: chạy limited RISK0/RISK1 canary qua bounded executor; RISK2 vẫn phải qua durable approval + context revalidation + kill switch.

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
→ Deterministic Core validate / ground
→ DecisionPacket
```

Visual-first implementation reference:

```text
n8n AI Agent
→ approved read-only tools / MCP client
→ CandidateEvidence
→ Deterministic Core validation
```

Go có thể là implementation của validation path này, nhưng canonical requirement là deterministic validation/grounding behavior chứ không phải language name.

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

Deterministic Policy Authority
→ classifies RISK / ALLOW / DENY / REQUIRE_APPROVAL

n8n
→ routes resulting workflow
```

Policy implementation có thể là:

```text
Go reference/fallback
OR
reviewed visual rule engine with parity + fail-closed proof
```

n8n IF/Switch node không được tự reclassify `RISK2` thành auto-executable. Orchestrator cũng không được log/forward raw personal data ngoài `DataAccessContext` chỉ vì integration node hỗ trợ.

### Chương 17 — Durable action workflow

- [ ] **17.1** — Persisted state, checkpoint, restart và resume/terminate
- [ ] **17.2** — Dry-run, controlled executor và duplicate-side-effect prevention
- [ ] **17.3** — Trace decision, tool, policy, approval, action và result

Primary orchestration reference:

```text
DecisionPacket
→ Deterministic Core creates/validates ActionIntent
→ Deterministic PolicyDecision
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

n8n AI Agent visual-first spike phải test:

- evidence correctness/grounding;
- unsupported claim rate;
- tool-call success/failure;
- permission compliance;
- data-scope/minimisation compliance khi relevant;
- prompt-injection resistance;
- auditability không leak secret/full personal data;
- latency/cost;
- fallback khi Agent unavailable.

Hermes/OpenAI Agents SDK comparison chỉ có ý nghĩa khi chạy **cùng test set** và chứng minh measured benefit trên một bottleneck n8n Agent cụ thể.

Agent unavailable phải fallback về deterministic/manual evidence path thay vì làm core decision contract biến mất.

## M09 — Shadow authority ceiling

```text
Agent may propose
Deterministic Policy Authority may classify
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

Nếu visual rule engine được adopt ở M09, bắt buộc lưu rule version/decision reason và parity cases đủ để chứng minh nó đang implement canonical contract, không tạo contract mới ngoài review.

## M10 — Limited governed automation

RISK0/RISK1 chỉ auto execute khi deterministic policy cho phép và canary scope đã khai báo.

RISK2:

```text
valid ActionIntent
+ Deterministic Policy requires approval
+ durable human approval
+ current-context revalidation
+ data/action scope still valid
+ kill switch clear
→ execution may proceed
```

Thiếu bất kỳ gate nào → no execution.

## Development Agent — không phải runtime authority

Codex/Copilot/Claude coding agent có thể implement/refactor Go, workflow artifact, tests hoặc rule-adapter code qua PR. Nhưng:

```text
coding agent writes policy code/rule adapter
≠ production policy changed
```

Mọi policy/runtime PR vẫn cần CI + human review; không auto-merge chỉ vì coding agent hoặc AI reviewer đánh giá cao.

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

Deterministic Policy Authority unavailable / invalid / unverified
→ no consequential execution

visual policy runtime error/version mismatch
→ fail closed / no consequential execution

kill switch ON
→ execution blocked even with prior approval
```

## Part PASS

- [ ] M08–M10 đều có Capability PASS, Reality verified và Operated
- [ ] Agent không thể gọi tool ngoài registry/permission
- [ ] Read-only tool có privacy relevance không được lấy/giữ/share dữ liệu vượt purpose/minimum scope
- [ ] CandidateEvidence phải qua Deterministic Core validation/grounding trước khi thành canonical evidence
- [ ] Audit giữ traceability nhưng không mặc định lưu raw secret/full personal data
- [ ] Agent proposal không tự trở thành ActionIntent được authorize
- [ ] n8n không bypass deterministic risk/policy result
- [ ] RISK2 không execute nếu thiếu valid approval và revalidation
- [ ] Restart/duplicate approval/workflow không tạo side effect trùng
- [ ] Kill switch chặn execution kể cả khi approval đã tồn tại
- [ ] Nếu Hermes/OpenAI SDK được thêm: có measured benefit so với n8n AI Agent trên cùng eval set
- [ ] Nếu visual policy được adopt: parity/version/reason/fail-closed/rollback evidence PASS
- [ ] Go/n8n/Agent/rule-engine implementations có thể thay mà không đổi Mission outcome/contracts

[← Part trước](part-04.md) · [Roadmap tổng](../ROADMAP.md) · [Part tiếp theo →](part-06.md)
