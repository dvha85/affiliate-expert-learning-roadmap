# ADR-003 — Hybrid Go Core + n8n Orchestration + Agent Runtime

- **Status:** Accepted
- **Decision date:** 2026-09-02
- **Applies from:** architecture rebaseline v2026.09-hybrid
- **Supersedes:** runtime-ownership assumptions in ADR-001 that implied Go should own most orchestration/runtime concerns
- **Keeps:** Go remains the primary language for domain/governance core

## 1. Context — Bối cảnh

Đích cuối của chương trình là một **Affiliate Intelligence Bot thông minh, tự động cao nhưng vẫn kiểm soát được**.

Roadmap trước đã đúng ở các nguyên tắc nền tảng:

- evidence-first;
- deterministic baseline trước AI;
- authority tăng dần theo Mission;
- read-only trước write;
- approval/policy trước consequential execution;
- audit/recovery/kill switch trước production autonomy.

Điểm cần rebaseline là **runtime ownership**. Nếu hiểu `Go-first` thành `Go-everything`, learner sẽ phải tự viết nhiều orchestration/integration plumbing không tạo lợi thế trực tiếp cho Affiliate intelligence. Ngược lại, nếu giao domain truth/policy cho workflow canvas hoặc Agent runtime, hệ thống khó audit và dễ tăng authority ngoài ý muốn.

## 2. Decision — Quyết định

Kiến trúc canonical từ nay là:

```text
Go Domain / Governance Core
+ n8n Orchestration Reference
+ Agent Runtime Intelligence Layer
```

Mental model bắt buộc:

```text
Go decides what is true / allowed.
Agent investigates / reasons / proposes.
n8n coordinates when / where / how workflows run.
```

Tương đương:

```text
GO CORE FIRST
≠
GO EVERYTHING
```

## 3. Ownership contract — Hợp đồng ownership

### 3.1. Go core owns

Go là canonical owner của:

- evidence schema/validation;
- subject/observation identity;
- canonical history/state contracts;
- deterministic ranking/decision logic;
- confidence/uncertainty semantics khi machine-readable;
- DecisionPacket / ActionIntent contracts;
- deterministic risk/policy classification;
- authorization result như `ALLOW | DENY | WAIT | GET_MORE_DATA | HUMAN_REVIEW`;
- audit/correlation identifiers và trace contracts;
- invariants như `missing != 0`, `Decision != Execution`.

Go không cần tự sở hữu mọi scheduler, webhook, notification, approval UI hoặc external integration.

### 3.2. n8n owns when adopted

n8n là **primary orchestration reference**, không phải decision engine.

Phù hợp cho:

- manual/scheduled trigger;
- webhook/API integration glue;
- workflow routing;
- notification/alert delivery;
- analytics/import orchestration;
- approval routing;
- retry/backoff orchestration nếu semantics đã được kiểm;
- calling Go service/CLI/API;
- bounded execution sau Go policy gate.

n8n không được trở thành canonical owner của:

- Product ranking truth;
- evidence truth classification;
- deterministic risk policy;
- final authorization;
- canonical business state chỉ vì canvas dễ chỉnh.

### 3.3. Agent runtime owns when adopted

Agent runtime là **intelligence layer**, không phải authority layer.

Phù hợp cho:

- unstructured reasoning;
- research;
- missing-evidence acquisition;
- read-only tool use;
- decomposition/delegation;
- candidate hypotheses/proposals;
- explanation/advisory.

Agent không được tự:

- upgrade inference thành measured fact;
- mutate canonical scoring/history input;
- classify final execution authority;
- bypass Go policy;
- publish/send/spend/change account trước Mission authority cho phép.

Hermes Agent là **primary reference/candidate implementation** cho Agent runtime ở các Mission tool-use sau, không phải mandatory dependency.

## 4. Capability lanes — Ba lane trưởng thành

Roadmap từ nay theo ba lane song song:

```text
DOMAIN / GOVERNANCE
AUTOMATION / ORCHESTRATION
INTELLIGENCE / AGENT
```

Maturity dự kiến:

| Mission | Domain / Governance | Automation / Orchestration | Intelligence / Agent |
|---|---|---|---|
| M00 | deterministic evidence decision | manual/local only | none |
| M01 | trustworthy ingest/history | manual/local only | none |
| M02 | grounded advisory contract/fallback | no external orchestration requirement | AI advisory, no tools |
| M03 | tracked Decision/Action boundary | human-only publish | optional advisory |
| M04 | analytics validation/reconciliation | first read-only n8n learning slice | optional advisory |
| M05 | experiment/evaluation/release decision | optional reporting/orchestration | advisory |
| M06 | signal/reliability contracts | n8n becomes primary watcher/orchestration reference | optional triage |
| M07 | DecisionPacket + deterministic policy | route decisions | advisory |
| M08 | Tool Registry/policy/audit | invoke/route read-only tools | read-only Agent runtime |
| M09 | ActionIntent + risk | shadow + durable approval routing | propose only |
| M10 | deterministic authorization | bounded governed execution | governed reasoning within permission |
| M11 | canonical state/policy/audit | production orchestration | production intelligence within authority ceiling |

## 5. Adoption timing — Khi nào dùng n8n/Agent

### n8n

- M00–M03: không cần cho Core.
- M04: **first read-only learning slice**; manual trigger/import/mapping/call-Go/failure handling, không external mutation.
- M06: **primary orchestration reference** cho watcher/trigger/integration/retry/alert.
- M09–M10: **primary reference** cho shadow workflow, approval routing và bounded execution.

### Agent runtime

- M02: AI advisory, **no tools**.
- M03–M07: advisory/analysis only; Agent runtime chưa phải Core dependency.
- M08: **first read-only tool-use Mission**; Hermes/reference runtime được spike qua explicit Tool Registry/permission/audit.
- M09: Agent có thể propose ActionIntent, không execute.
- M10–M11: Agent chỉ tham gia trong authority do deterministic policy/approval/kill switch giới hạn.

## 6. Authority progression — Capability không tự cấp quyền

Framework capability không bao giờ tự tăng Bot authority.

```text
n8n has a node
≠ workflow is authorized

Agent has a tool
≠ tool call is permitted

Agent confidence is high
≠ execution is allowed
```

Authority chỉ tăng qua Mission gate và evidence:

```text
A0 deterministic/manual
→ A1 advisory
→ A2-RO read-only tools
→ A3-shadow proposed/dry-run actions
→ A3-limited governed bounded execution
→ production closed loop
```

## 7. Runtime failure rules — Failure phải fail-safe

Các invariants production tương lai:

```text
Agent unavailable
≠ core deterministic decision unavailable

n8n unavailable
≠ canonical evidence/history corrupted

Go Policy unavailable
→ no consequential execution
```

Ngoài ra:

- duplicate workflow không được tạo duplicate side effect;
- stale/expired approval không được dùng;
- Agent bad output phải reject/fallback;
- external integration failure phải có retry/recovery/audit rõ;
- kill switch phải chặn execution bất kể approval/Agent confidence.

## 8. Replaceability — Không vendor-lock curriculum

Canonical curriculum khóa **contracts và ownership**, không khóa vendor.

```text
Orchestrator
= interface/role
n8n
= primary reference implementation

AgentRuntime
= interface/role
Hermes Agent
= primary reference/candidate implementation
```

Nếu về sau một công nghệ khác đáp ứng tốt hơn:

- permission;
- audit;
- retry/recovery;
- cost;
- security;
- operational simplicity;

thì có thể thay reference implementation mà không thay Mission outcome.

## 9. Consequences — Hệ quả cho roadmap

- Part 00–01 giữ outcome và learner sequence hiện tại.
- Part 02 giới thiệu orchestration **nhẹ/read-only** ở M04 thay vì đợi tới M06 mới học từ số 0.
- Part 03 giữ trọng tâm outcome/experiment; orchestration chỉ hỗ trợ.
- Part 04 trưởng thành n8n thành reliable orchestration reference.
- Part 05 trưởng thành Agent tool-use + approval + governed action.
- Part 06 trở thành cross-runtime production operation/recovery.
- Lesson future phải dạy ownership boundary, không chỉ feature của framework.

## 10. Consequences — Hệ quả cho learner

Learner không cần cài n8n/Hermes ở M00–M02.

Learner tiếp tục học:

```text
M00 evidence discipline
→ M01 trustworthy history
→ M02 grounded advisory
```

trước khi thêm runtime complexity.

Điều này giữ Build-First nhưng tránh overengineering sớm.

## 11. Non-goals — Không có nghĩa là

ADR này không có nghĩa:

- n8n mandatory cho mọi deployment;
- Hermes mandatory cho mọi Agent;
- Go không được dùng scheduler/integration khi cách đơn giản hơn;
- workflow canvas được phép chứa business truth/policy tùy ý;
- Agent được phép self-modify production logic;
- M00–M03 phải cài thêm infrastructure;
- microservices-first;
- multi-agent-first.

## 12. Migration plan — Rebaseline có kiểm soát

1. ADR-003 canonicalize ownership.
2. Update ADR-001 để chỉ còn authority cho Go domain-core language choice.
3. Update `CURRICULUM.md` + `ROADMAP.md` với ba capability lanes.
4. Rebaseline Part 02–06 và M03–M11 ship targets theo ownership mới.
5. Update technology candidate/reference note.
6. Add CI semantic guards cho authority drift.
7. Compatibility review Part 00–01.
8. Dừng authoring mới và quay lại learner progress hiện tại.

## 13. Final architectural rule

```text
Go = domain truth + governance authority
n8n = orchestration reference
Agent = intelligence worker

contracts first
authority gated
framework replaceable
```
