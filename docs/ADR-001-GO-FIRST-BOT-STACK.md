# ADR-001 — Quyết định Go-first cho Domain/Governance Core

- **Status (Trạng thái):** Accepted for Go domain/governance core; runtime ownership superseded by ADR-003
- **Decision date (Ngày quyết định):** 2026-08-28
- **Applies from (Áp dụng từ):** curriculum revision v2026.09
- **Supersedes (Thay thế):** hướng C#/.NET-first trong `sources/SYLLABUS-v2026.08.md`
- **Does not erase (Không xóa):** v2026.08 vẫn là historical provenance

> [`ADR-002`](ADR-002-OUTCOME-DRIVEN-CURRICULUM.md) thay thế structural invariant/mission sequence cũ.
>
> [`ADR-003`](ADR-003-HYBRID-GO-N8N-AGENT-RUNTIME.md) thay thế các giả định runtime trước đây có thể bị hiểu thành `Go-everything`. ADR này hiện chỉ còn authority cho quyết định **Go là primary implementation language của domain/governance core**.

## 1. Context — Bối cảnh

Curriculum hướng tới một **Affiliate Intelligence Bot** có thể quan sát evidence, lưu lịch sử, tạo quyết định có giải thích, dùng AI/Agent khi hữu ích, tự động hóa workflow dần dần và chỉ tăng authority sau safety/evidence gates.

Syllabus trước dùng C#/.NET làm primary engineering path. C#/.NET vẫn là stack hợp lệ, nhưng không còn là primary path của curriculum hiện hành.

## 2. Decision — Quyết định

Active curriculum dùng:

```text
PRIMARY DOMAIN / GOVERNANCE IMPLEMENTATION LANGUAGE = Go
```

Go là primary language cho:

- evidence validation;
- canonical history/state contracts;
- deterministic decision logic;
- risk/policy classification;
- DecisionPacket / ActionIntent contracts;
- audit/correlation contracts;
- service/API boundary của domain core khi cần.

C#/.NET trở thành optional/reference stack.

Runtime architecture đầy đủ không còn được định nghĩa bởi ADR-001. Xem ADR-003:

```text
Go Domain / Governance Core
+ n8n Orchestration Reference
+ Agent Runtime Intelligence Layer
```

## 3. Vì sao chọn Go cho core

Quyết định dựa trên đặc tính vận hành hệ thống, không dựa trên kết luận đơn giản “Go luôn nhanh hơn C#”.

Affiliate Bot thường bị giới hạn bởi network/API latency, rate limit, database, external services, LLM calls và retry/wait. Go được ưu tiên cho core vì:

- deployment đơn giản dưới dạng service/binary nhỏ;
- concurrency model mạnh khi cần collector/watcher/service;
- resource efficiency tốt cho process chạy liên tục;
- standard library mạnh cho HTTP/network/service;
- operational complexity thấp cho team nhỏ/single operator;
- ecosystem cloud-native và interoperability trưởng thành;
- code/test/versioning phù hợp với deterministic domain/policy logic.

## 4. Current technical baseline — mốc kỹ thuật hiện hành

Đây là freshness-scoped reference facts, không phải permanent syllabus constants.

Verified 2026-08-28:

- Go 1.27.0 phát hành 2026-08-19; curriculum phải dùng stable release còn support tại thời điểm học.
- Official Model Context Protocol SDK list xếp Go là Tier 1.
- MCP specification `2026-07-28` được Tier-1 Go SDK hỗ trợ.
- OpenTelemetry Go là reference observability phù hợp.

Primary references:

- https://go.dev/doc/devel/release
- https://github.com/modelcontextprotocol/go-sdk
- https://opentelemetry.io/docs/languages/go/

Version/SDK facts phải theo freshness policy của repo.

## 5. Architecture principles còn hiệu lực

### 5.1. Modular core trước microservices

```text
single Go module
→ packages/modules rõ
→ service/API boundary khi có bottleneck thật
→ split service chỉ khi failure/scaling boundary justify
```

ADR-003 cho phép orchestration/Agent runtime ở lớp ngoài mà không yêu cầu biến Go core thành microservices sớm.

### 5.2. Deterministic logic trước Agent autonomy

```text
manual evidence
→ deterministic function
→ trustworthy service/core
→ grounded AI advisory
→ read-only tools
→ governed action
```

LLM/Agent không thay deterministic business logic khi rule/formula/policy có thể biểu diễn và kiểm thử rõ.

### 5.3. Human approval và deterministic policy là first-class boundary

Risk classification cuối cùng thuộc deterministic policy, không giao cho LLM/Agent hoặc workflow canvas tự quyết.

```text
RISK0
→ bounded auto execute khi Mission cho phép

RISK1
→ bounded execute + mandatory audit khi Mission cho phép

RISK2
→ durable human approval + context revalidation
```

### 5.4. Tool boundary trước unrestricted action

Agent/tool action phải đi qua explicit contract:

- schema;
- validation;
- read/write separation;
- permission;
- side-effect classification;
- idempotency;
- timeout/retry;
- policy;
- approval;
- audit.

MCP, REST, webhook hay native API là implementation choices; contract mới là authority.

## 6. Hệ quả cho curriculum

Primary domain stack:

```text
Go
HTTP/API boundary khi cần
canonical evidence/history/decision/policy contracts
provider-neutral AI/Agent boundary
```

Orchestration/runtime stack được ADR-003 định nghĩa riêng:

```text
n8n = primary orchestration reference
AgentRuntime = intelligence role
Hermes Agent = primary Agent reference/candidate ở Mission phù hợp
```

Không được suy ra từ ADR này rằng mọi scheduler, webhook, approval workflow, notification hoặc Agent runtime phải viết bằng Go.

## 7. Non-goals — Những điều ADR không có nghĩa

ADR này không có nghĩa:

- Go bắt buộc cho mọi runtime/integration;
- Go phải tự viết mọi orchestration plumbing;
- Python không bao giờ được dùng cho justified ML/data workload;
- mọi Bot phải dùng MCP;
- mọi Bot phải dùng n8n;
- mọi Bot phải dùng Hermes;
- mọi Bot phải dùng LLM;
- microservices là default architecture.

## 8. Historical migration note

Go-first migration ban đầu đã thay C#/.NET-first bằng Go trong learner/reference engineering path. Sau learner-oriented hardening, ADR-003 tiếp tục rebaseline runtime ownership để giữ lợi ích của Go core mà không biến chương trình thành `Go-everything`.

## 9. Final rule

```text
Go-first
=
Go domain/governance core first

Go-first
≠
Go owns every runtime concern
```
