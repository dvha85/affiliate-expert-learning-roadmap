# SYLLABUS v2026.09
## Affiliate Expert & Affiliate Bot Engineer

**Phiên bản:** 2026.09  
**Trạng thái:** Active canonical revision  
**Base structural source:** [`SYLLABUS-v2026.08.md`](SYLLABUS-v2026.08.md)  
**Định hướng:** Việt Nam + Global Affiliate  
**Thời lượng chuẩn:** 12–15 tháng  
**Khối lượng:** 8–10 giờ/tuần  
**Tỷ lệ:** ~30% lý thuyết — ~70% thực hành  
**Dự án xuyên suốt:** **Affiliate Intelligence Platform**

---

# 0. CÁCH ĐỌC REVISION NÀY

`v2026.09` là **active canonical manifest** cho curriculum sau quyết định Go-first.

Để tránh sao chép hơn 2.400 dòng syllabus và tạo hai bản structural source dễ drift, revision này dùng mô hình:

```text
ACTIVE CANONICAL v2026.09
=
v2026.08 structural baseline
+
explicit normative overrides in this file
```

Quy tắc:

1. Tất cả Part / Chapter / Lesson / Project / LAB / PASS Gate **không được override bên dưới** được kế thừa nguyên trạng từ `SYLLABUS-v2026.08.md`.
2. Các override trong file này **thắng** v2026.08 đối với technology direction, Bot Engineer capability model và các lesson kỹ thuật được liệt kê.
3. `SYLLABUS-v2026.08.md` được giữ nguyên làm provenance/history và không còn là active implementation direction.
4. Tổng cấu trúc vẫn là:

```text
23 Parts
89 Chapters
671 lessons
14 main projects
```

5. Current versions, SDK behavior, platform rules và software/library facts vẫn phải đi qua freshness policy; không hard-code current version thành chân lý vĩnh viễn của syllabus.

---

# I. MỤC TIÊU ĐÀO TẠO — OVERRIDE BOT ENGINEER

Bốn năng lực Affiliate Business Expert, Affiliate Marketer, Affiliate Data Analyst và Affiliate Intelligence Expert được kế thừa từ v2026.08.

## 4. Affiliate Bot Engineer — v2026.09

Affiliate Bot Engineer không chỉ có khả năng viết collector hoặc scheduler. Học viên phải có khả năng thiết kế và vận hành một hệ thống tự động đáng tin cậy có thể:

- collect dữ liệu từ APIs/exports/compliant sources;
- normalize, validate, store và theo dõi provenance;
- chạy worker/job/pipeline lâu dài;
- xử lý retry, timeout, idempotency, queue và failure recovery;
- phân tích, detect, rank và recommend;
- expose/consume tools bằng contract rõ ràng;
- dùng MCP khi interoperability có giá trị;
- dùng AI/LLM khi deterministic logic không đủ;
- giữ state, audit và trace cho agent/tool workflows;
- classify action risk;
- tự thực hiện low-risk actions theo policy;
- pause và chờ human approval cho consequential actions;
- resume/terminate workflow sau approval decision;
- bảo vệ secrets, permissions, data/privacy boundary;
- chống prompt injection/tool misuse ở agentic workflows;
- deploy, monitor và control cost của production bot.

Học viên vẫn phải có khả năng xây các hệ thống đã định nghĩa ở v2026.08:

- Product Collector
- Product Tracker
- Opportunity Engine
- Analytics Engine
- Alert Bot
- AI Content Assistant
- Experiment Engine
- Recommendation Engine

nhưng các hệ thống đó được triển khai theo Go-first, reliable-automation và governed-autonomy model.

---

# II. 4 TRACK HỌC SONG SONG — TRACK C OVERRIDE

Track A, B và D được kế thừa từ v2026.08.

## TRACK C — Engineering & AI — v2026.09

```text
Go
→ Services / Workers
→ Collector
→ Database
→ Queue / Durable Workflow
→ Bot
→ Tool Engineering / MCP
→ AI Agent
→ Human Approval / Governance
→ Production
```

### Primary implementation language

```text
Go = primary active implementation language
C#/.NET = optional/reference stack
```

Lý do chọn Go tập trung vào:

- concurrency cho collectors/watchers/workers;
- resource footprint hợp lý cho service chạy lâu dài;
- deployment simplicity;
- networking/service ecosystem;
- operational simplicity cho một hệ thống do ít người vận hành.

Không dùng lập luận đơn giản rằng “Go luôn nhanh hơn C#”. Affiliate Bot phần lớn là I/O-bound và external-service-bound.

### Engineering progression

```text
manual workflow
→ deterministic Go function/service
→ scheduled worker
→ reliable pipeline
→ AI-assisted bot
→ tool-using agent
→ governed autonomous system
```

Không dùng LLM/agent khi deterministic code/rule đã giải quyết vấn đề rõ hơn, rẻ hơn và kiểm soát tốt hơn.

---

# III. AUTONOMY MODEL — NEW CANONICAL PRINCIPLE

Bot không được hiểu là “tự động làm mọi thứ”.

Action phải đi qua policy/risk boundary:

```text
RISK 0
→ auto execute

RISK 1
→ auto execute
→ mandatory audit

RISK 2
→ persist workflow state
→ create approval request
→ pause
→ human approve/reject
→ resume or terminate
```

Risk classification không được giao hoàn toàn cho LLM. Deterministic policy/rule phải bảo vệ các hành động có tác động cao.

Ví dụ nhóm thường cần xem xét RISK 2:

- publish externally;
- spend money;
- thay đổi production/account configuration;
- xóa dữ liệu quan trọng;
- gửi communication có tác động bên ngoài;
- action có legal/platform/compliance impact đáng kể.

Chi tiết taxonomy được chuẩn hóa ở operating docs của curriculum.

---

# IV. ENGINEERING PRINCIPLES — NEW CANONICAL PRINCIPLES

## Rule E1 — Modular monolith first

Không bắt đầu bằng microservices chỉ vì hệ thống cuối lớn.

```text
single Go module
→ clear internal boundaries
→ workers/adapters
→ queues/workflows
→ split services only when justified
```

## Rule E2 — Context and cancellation are first-class

Network/API/worker operations phải có cancellation/timeout boundary rõ.

## Rule E3 — Side effects require idempotency

Action có thể retry phải có idempotency/dedup strategy.

## Rule E4 — Long waits require durable state

Workflow có thể chờ approval lâu không được phụ thuộc vào RAM/process lifetime.

Phải hiểu:

- checkpoint/resume;
- persisted state;
- retries/backoff;
- timeout/cancellation;
- compensation;
- crash recovery.

## Rule E5 — Tools before unrestricted agent action

Agent chỉ được hành động qua explicit tool contracts.

Tool contract phải xét:

- schema;
- validation;
- permission;
- side effect;
- timeout;
- retry;
- idempotency;
- policy decision;
- approval;
- audit.

## Rule E6 — Observability includes decisions

Production tracing không chỉ đo HTTP/DB latency.

Phải có khả năng truy ngược:

```text
request/workflow
→ decision
→ model call (nếu có)
→ tool call
→ policy decision
→ approval
→ action execution
→ result
```

## Rule E7 — Agent autonomy never removes accountability

Prompt injection, tool misuse, excessive permissions, data leakage và unsafe action paths phải được xem là production security concerns.

---

# V. PART / CHAPTER OVERRIDES

Các Part/Chapter không liệt kê bên dưới được kế thừa từ v2026.08.

## PHẦN 0 — ORIENTATION & AFFILIATE LAB

Lesson IDs và titles vẫn giữ nguyên trong revision này:

- `0.2 — Affiliate Bot Engineer là gì?`
- `0.4 — Affiliate Bot có thể và không thể làm gì?`
- `0.5 — Vì sao không nên bắt đầu bằng automation?`
- `0.6 — Learn → Do → Measure → Automate → Optimize`

Normative interpretation từ v2026.09:

- 0.2 phải dạy Go-first + reliable automation + agent/tool/governance model.
- 0.4 phải phân biệt auto action, approval-required action và prohibited action.
- 0.5–0.6 giữ nguyên nguyên tắc hiểu/làm/đo trước khi automate.

---

## PHẦN 15 — AFFILIATE BOT ENGINEERING

### Chương 50 — Bot Architecture

Scope hiện hành phải bao phủ:

```text
modular Go application
+ collectors/adapters
+ storage
+ analytics/decision
+ policy/risk boundary
+ approval boundary
+ action executor
+ audit/observability
```

Lesson IDs giữ nguyên. Detailed title migration được thực hiện ở roadmap migration PR.

### Chương 51 — Technology Stack

Technology direction của v2026.08:

```text
C# / .NET
ASP.NET Core
Worker Service
EF Core
Hangfire / Quartz
```

không còn là active primary path.

Active v2026.09 direction:

```text
Go current supported stable release
Go modules/project structure
HTTP/API + context
Goroutines / concurrency / worker patterns
PostgreSQL
Redis only when justified
configuration + interfaces + testing
Docker
observability
REST/Webhook/API adapters
MCP where useful
```

Không hard-code framework/library hiện hành vào canonical lesson title nếu concept có thể dạy framework-neutral.

### Chương 52 — Product Collector

Giữ 10 lesson IDs và scope business hiện tại.

Implementation interpretation:

- Go interface/adapter pattern;
- HTTP client + context timeout/cancellation;
- rate-limit/backoff;
- source provenance;
- validation;
- compliant collection.

### Chương 53 — Scheduler & Pipeline

Giữ 7 lesson IDs.

Scope phải bao phủ:

```text
job/workflow
scheduler/trigger
queue/worker pool
retry/backoff/timeout
idempotency/dedup
DLQ/compensation
checkpoint/resume/long-running wait
```

Durable workflow engine là implementation option khi reliability/approval wait yêu cầu; không phải dependency bắt buộc cho mọi bot.

---

## PHẦN 16 — DECISION & RECOMMENDATION ENGINE

Normative extension:

- Rule Engine phải hỗ trợ action policy/risk classification.
- Recommendation và execution là hai boundary khác nhau.
- High-risk recommendation không được tự động trở thành execution nếu policy yêu cầu approval.

---

## PHẦN 17 — AI AFFILIATE BOT

Normative extension:

- Tool Calling phải phát triển thành Tool Engineering: contracts, validation, permissions, side effects, policy và audit.
- MCP là interoperability concept bắt buộc phải hiểu; không bắt buộc dùng trong mọi bot.
- RAG/Knowledge Base phải phân biệt knowledge, session state và operational workflow state.
- AI Evaluation phải đánh giá cả task success/tool behavior, không chỉ text quality.
- Human-in-the-loop phải có pause/resume approval workflow, không chỉ checklist review.
- Single-agent/tool workflow là default; multi-agent chỉ dùng khi decomposition thật sự mang lại giá trị.

---

## PHẦN 19 — PRODUCTION, SECURITY & AUTOMATION

Normative extension:

### Chương 73 — Production Engineering

Observability phải bao phủ service + workflow + agent/tool spans.

### Chương 74 — Reliability

Bổ sung concept:

- durable execution;
- persisted workflow state;
- checkpoint/resume;
- cancellation;
- compensation.

### Chương 75 — Security

Bổ sung concept:

- tool permission/least privilege;
- prompt injection/tool misuse boundary;
- safe secret handling for agents/tools;
- sandbox/isolation when executing risky or generated operations.

### Chương 76 — Automation Governance

Governance baseline:

```text
RISK 0 / 1 / 2
+ policy checks
+ approval queue
+ audit trail
+ kill switch
```

---

## PHẦN 21 — CAPSTONE

Affiliate Intelligence Platform phải tiến tới architecture có các first-class capabilities:

```text
Data Sources
→ Collection
→ Historical Data
→ Analytics
→ Opportunity / Experiment / Recommendation
→ Tool Registry / Action Boundary
→ Policy & Risk Engine
→ Approval Queue
→ Action Executor
→ Audit / Trace Store
→ Result / Revenue
→ Feedback / Evaluation
↺
```

Không phải mọi capability đều phải là microservice riêng.

---

## PHẦN 22 — CONTINUOUS MASTERY

Technology Watch phải theo dõi ít nhất:

- supported Go releases;
- agent/tool protocols such as MCP;
- API/tracking integrations;
- durable workflow/runtime evolution;
- AI agent frameworks;
- observability/security practices;
- A2A/remote-agent interoperability khi có use case thật.

A2A hiện là SHOULD/WATCH, không phải Phase-1 requirement.

---

# VI. CURRENT TECHNICAL REFERENCE SNAPSHOT

> Phần này là snapshot để giải thích quyết định, không phải invariant của canonical structure.

**Verified:** 2026-08-28

- Go 1.27.0 released 2026-08-19.
- Official MCP SDK classification: Go = Tier 1.
- MCP Go SDK supports protocol `2026-07-28`.
- Temporal Go SDK is a reference for durable asynchronous long-running workflows.
- OpenTelemetry Go currently reports traces and metrics stable; logs beta.

References:

- https://go.dev/doc/devel/release
- https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/docs/2026-07-28/sdk.mdx
- https://github.com/modelcontextprotocol/go-sdk
- https://github.com/temporalio/sdk-go
- https://opentelemetry.io/docs/languages/go/

Before production implementation, re-verify current supported versions and protocol/library behavior.

---

# VII. STRUCTURAL INVARIANTS

The revision intentionally does not add or remove curriculum units.

```text
Parts: 23
Chapters: 89
Lessons: 671
Main projects: 14
```

Roadmap migration must preserve those counts.

---

# VIII. RELATION TO v2026.08

Use this rule when resolving curriculum source questions:

```text
If v2026.09 explicitly overrides a topic
→ v2026.09 wins.

If v2026.09 is silent
→ inherit v2026.08 unchanged.

If the fact is time-sensitive
→ current external verification/freshness layer wins for operating truth,
   without silently rewriting historical provenance.
```

This model preserves auditability while allowing the engineering direction to evolve without duplicating the entire historical syllabus.