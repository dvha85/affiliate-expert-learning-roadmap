# ADR-001 — Go-first Bot Engineering Stack

- **Status:** Accepted
- **Decision date:** 2026-08-28
- **Applies from:** curriculum revision v2026.09
- **Supersedes:** C#/.NET-first implementation direction in `sources/SYLLABUS-v2026.08.md`
- **Does not erase:** v2026.08 remains historical provenance

> **Beginner reader guide / Hướng dẫn cho người mới:** ADR = **Architecture Decision Record (Bản ghi quyết định kiến trúc)**. Tài liệu này giữ English terminology làm chuẩn kỹ thuật. Tra [`GLOSSARY-VI.md`](GLOSSARY-VI.md) khi cần. Các từ trọng tâm: **Primary Implementation Language (Ngôn ngữ triển khai chính)**, **Modular Monolith (Khối đơn thể mô-đun)**, **Deterministic Logic (Logic xác định)**, **Durable Execution (Thực thi bền vững)**, **Tool Boundary (Ranh giới công cụ)**, **Human Approval (Phê duyệt của con người)**, **Least Privilege (Quyền tối thiểu cần thiết)**, **Observability (Khả năng quan sát hệ thống)**.

## 1. Context

The curriculum targets an **Affiliate Intelligence Platform** that should run continuously, collect and reconcile data, detect changes, rank opportunities, use AI when useful, execute low-risk actions automatically, and pause for human approval before consequential actions.

The desired operator model is not “human drives every bot step”. It is:

```text
BOT observes
→ BOT collects
→ BOT analyzes
→ BOT proposes/decides within policy
→ low-risk action: execute automatically
→ consequential action: pause for approval
→ execute or reject
→ audit result
→ measure
→ learn
```

Beginner translation:

```text
Bot quan sát
→ thu thập
→ phân tích
→ đề xuất/quyết định trong policy
→ low-risk: tự thực thi
→ consequential: dừng chờ người duyệt
→ thực thi hoặc từ chối
→ ghi vết kết quả
→ đo lường
→ học
```

The previous syllabus selected C#/.NET as the primary engineering path. That remains a valid implementation stack, but it is no longer the preferred primary path for this curriculum.

## 2. Decision

The active curriculum adopts:

```text
PRIMARY IMPLEMENTATION LANGUAGE = Go
```

C#/.NET becomes an **optional/reference stack**, not the active primary implementation path.

The preferred engineering spine is:

```text
Go
→ Services / Workers
→ Collectors & Adapters
→ PostgreSQL / optional Redis
→ Queue / Workflow
→ Durable Execution when required
→ Analytics / Decision Engine
→ Tool Boundary / MCP
→ AI Agent where justified
→ Policy & Risk Engine
→ Human Approval Queue
→ Action Executor
→ Audit / Tracing / Feedback
```

## 3. Why Go

The decision is based on system-operating characteristics, not a simplistic claim that “Go is always faster than C#”.

Affiliate bots are primarily constrained by network/API latency, platform rate limits, databases, queues, external services and LLM calls. Raw CPU throughput is therefore not the primary decision variable.

Go is preferred because it fits the target operating model well:

- simple deployment as a small service/binary;
- strong concurrency model for many collectors, watchers and background jobs;
- good resource efficiency for services intended to stay online continuously;
- strong standard library for HTTP/network/service work;
- low operational complexity for a small team or single operator;
- mature cloud-native ecosystem;
- first-class support for modern tool/agent interoperability.

## 4. Current technical baseline

These are **freshness-scoped reference facts**, not permanent syllabus constants.

Verified 2026-08-28:

- Go 1.27.0 was released on 2026-08-19. The curriculum should use a currently supported stable Go release rather than hard-code 1.27 forever.
- The official Model Context Protocol SDK list classifies **Go as Tier 1**.
- MCP specification `2026-07-28` is supported by the Tier-1 Go SDK.
- Temporal Go SDK is a mature reference for durable, asynchronous, long-running workflows.
- OpenTelemetry Go currently lists traces and metrics as stable; logs remain beta.

Primary references:

- https://go.dev/doc/devel/release
- https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/docs/2026-07-28/sdk.mdx
- https://github.com/modelcontextprotocol/go-sdk
- https://github.com/temporalio/sdk-go
- https://opentelemetry.io/docs/languages/go/

Any implementation lesson that depends on current versions, SDK behavior or protocol details must use the repo freshness policy.

## 5. Architecture principles

### 5.1. Modular Monolith (Khối đơn thể mô-đun) first

Do not make the curriculum microservices-first.

Default progression:

```text
single Go module
→ clear packages/modules
→ workers and adapters
→ internal queues/workflows
→ split services only when scaling or failure boundaries justify it
```

### 5.2. Deterministic Logic (Logic xác định) before agent autonomy

Preferred progression:

```text
manual workflow
→ deterministic function
→ service
→ worker
→ reliable pipeline
→ AI-assisted bot
→ tool-using agent
→ governed autonomous system
```

LLMs must not replace deterministic business logic when rules, formulas or policy checks can be expressed explicitly.

### 5.3. Human Approval (Phê duyệt của con người) is a first-class system boundary

The platform uses three risk levels:

```text
RISK 0
→ auto execute

RISK 1
→ auto execute + mandatory audit

RISK 2
→ pause workflow
→ human approve/reject
→ resume or terminate
```

Examples of RISK 2 may include publishing, spending money, changing production/account settings, deleting important data, or other externally consequential actions.

The exact classification is defined by policy, not by the LLM alone.

### 5.4. Durable Execution (Thực thi bền vững) when workflows can wait

A workflow that can pause for minutes, hours or days for approval must not depend only on in-memory process state.

The curriculum must teach concepts such as:

- persisted workflow state;
- checkpoint/resume;
- retries and backoff;
- idempotency;
- timeout/cancellation;
- compensation;
- approval wait;
- crash/restart recovery.

Temporal is a reference implementation, not a mandatory dependency for every project.

### 5.5. Tool Boundary (Ranh giới công cụ) before unrestricted action

Agent actions must pass through explicit tools/interfaces.

Tool engineering includes:

- schema/contracts;
- input/output validation;
- read vs write separation;
- side-effect classification;
- permissions;
- idempotency;
- timeout/retry;
- policy check;
- approval when required;
- audit evidence.

MCP is an important interoperability layer, but REST/webhooks/native APIs remain valid where simpler.

## 6. Agent engineering implications

The curriculum must expand Bot Engineer beyond collector/scheduler code to include:

- tool engineering and MCP;
- state/session/memory boundaries;
- durable execution;
- agent evaluation;
- tracing and observability;
- prompt-injection/tool-misuse defenses;
- least-privilege tool permissions;
- approval and kill switch;
- policy-aware autonomous actions.

Multi-agent and A2A are advanced patterns. They are **not** default architecture for Phase 1.

## 7. Consequences for curriculum

### Active primary stack

```text
Go
PostgreSQL
Redis only when justified
HTTP/API/Webhook adapters
queue/worker patterns
Docker
OpenTelemetry-style observability
MCP where useful
provider-neutral AI boundary
```

Reference implementations may include current libraries or workflow engines, but library choices remain freshness-scoped.

### C#/.NET

C#/.NET:

- remains valid comparison/reference material;
- remains present in historical v2026.08 provenance;
- may be mentioned when comparing runtime/framework tradeoffs;
- is no longer the active primary implementation path.

## 8. Non-goals

This ADR does **not** mean:

- Go must be used for every future analytical/ML component;
- Python can never be introduced for a justified ML/data workload;
- every bot must use MCP;
- every bot must use Temporal;
- every bot should use an LLM;
- every workflow should become multi-agent;
- microservices are the desired starting architecture.

## 9. Migration plan

The migration is deliberately staged:

1. **PR 1** — canonical revision + this ADR.
2. **PR 2** — migrate engineering roadmap/lesson titles without changing counts.
3. **PR 3** — add Go engineering/autonomy/security operating standards and CI drift guards.
4. **PR 4** — author lesson 0.2 as the Go-first Bot Engineer reference lesson.

## 10. Invariants

The migration must preserve:

```text
23 Parts
89 Chapters
671 lessons
14 main projects
```

Technology decisions may change implementation guidance, examples and selected lesson titles, but must not silently alter the curriculum’s structural counts.
