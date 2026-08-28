# ADR-001 — Quyết định Go-first cho Bot Engineering Stack

- **Status (Trạng thái):** Accepted (Đã chấp nhận)
- **Decision date (Ngày quyết định):** 2026-08-28
- **Applies from (Áp dụng từ):** curriculum revision v2026.09
- **Supersedes (Thay thế):** hướng C#/.NET-first trong `sources/SYLLABUS-v2026.08.md`
- **Does not erase (Không xóa):** v2026.08 vẫn là historical provenance (nguồn gốc lịch sử)

> ADR = **Architecture Decision Record (Bản ghi quyết định kiến trúc)**. Tiếng Việt là ngôn ngữ chính; English terminology và tên công nghệ được giữ khi cần đối chiếu kỹ thuật. Xem [`LANGUAGE-POLICY.md`](LANGUAGE-POLICY.md) và [`GLOSSARY-VI.md`](GLOSSARY-VI.md).

## 1. Context (Bối cảnh)

Curriculum hướng tới một **Affiliate Intelligence Platform (Nền tảng Affiliate Intelligence)** có thể chạy liên tục, thu thập/đối soát dữ liệu, phát hiện thay đổi, xếp hạng cơ hội, dùng AI khi hữu ích, tự thực hiện action rủi ro thấp và dừng chờ Human Approval (phê duyệt của con người) trước action có hậu quả đáng kể.

Operator model (mô hình vận hành) mong muốn **không phải** “con người điều khiển từng bước của Bot”. Mô hình là:

```text
Bot quan sát
→ Bot thu thập
→ Bot phân tích
→ Bot đề xuất/quyết định trong policy
→ low-risk action: tự thực thi
→ consequential action: dừng chờ phê duyệt
→ thực thi hoặc từ chối
→ audit kết quả
→ đo lường
→ học
```

Syllabus trước dùng C#/.NET làm primary engineering path. C#/.NET vẫn là stack hợp lệ, nhưng không còn là primary path của curriculum hiện hành.

## 2. Decision (Quyết định)

Active curriculum dùng:

```text
PRIMARY IMPLEMENTATION LANGUAGE = Go
(Ngôn ngữ triển khai chính = Go)
```

C#/.NET trở thành **optional/reference stack (stack tùy chọn/tham khảo)**.

Engineering spine (xương sống kỹ thuật) ưu tiên:

```text
Go
→ Services / Workers
→ Collectors & Adapters
→ PostgreSQL / Redis khi có lý do
→ Queue / Workflow
→ Durable Execution khi cần
→ Analytics / Decision Engine
→ Tool Boundary / MCP
→ AI Agent khi justified (có lý do)
→ Policy & Risk Engine
→ Human Approval Queue
→ Action Executor
→ Audit / Tracing / Feedback
```

## 3. Vì sao chọn Go

Quyết định dựa trên đặc tính vận hành hệ thống, **không** dựa trên kết luận đơn giản “Go luôn nhanh hơn C#”.

Affiliate Bot thường bị giới hạn bởi:

- network/API latency (độ trễ mạng/API);
- platform rate limit;
- database;
- queue/external services;
- LLM calls;
- retry/wait.

Vì vậy raw CPU throughput không phải biến quyết định chính.

Go được ưu tiên vì phù hợp target operating model:

- deployment đơn giản dưới dạng service/binary nhỏ;
- concurrency model mạnh cho collector, watcher và background job;
- resource efficiency tốt cho service chạy liên tục;
- standard library mạnh cho HTTP/network/service;
- operational complexity thấp cho team nhỏ/single operator;
- cloud-native ecosystem trưởng thành;
- hỗ trợ tốt cho modern tool/agent interoperability.

## 4. Current technical baseline (mốc kỹ thuật hiện hành)

Đây là **freshness-scoped reference facts (dữ kiện tham chiếu có thời hạn)**, không phải permanent syllabus constants.

Verified 2026-08-28:

- Go 1.27.0 phát hành 2026-08-19. Curriculum phải dùng một Go stable release đang còn support, không giữ 1.27 vĩnh viễn.
- Official Model Context Protocol SDK list xếp **Go là Tier 1**.
- MCP specification `2026-07-28` được Tier-1 Go SDK hỗ trợ.
- Temporal Go SDK là current reference trưởng thành cho durable, asynchronous, long-running workflow.
- OpenTelemetry Go hiện liệt kê traces/metrics stable; logs beta.

Primary references (nguồn chính):

- https://go.dev/doc/devel/release
- https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/docs/2026-07-28/sdk.mdx
- https://github.com/modelcontextprotocol/go-sdk
- https://github.com/temporalio/sdk-go
- https://opentelemetry.io/docs/languages/go/

Implementation lesson phụ thuộc current version/SDK/protocol phải theo repo freshness policy.

Tại thời điểm hardening Issue #37, learner/reference bootstrap dùng `go 1.27` để khớp current supported stable line đã verified.

## 5. Architecture principles (Nguyên tắc kiến trúc)

### 5.1. Modular Monolith (Khối đơn thể mô-đun) trước

Không thiết kế curriculum theo microservices-first.

Progression mặc định:

```text
single Go module
→ packages/modules rõ ràng
→ workers + adapters
→ internal queues/workflows
→ chỉ split services khi scaling/failure boundary thật sự yêu cầu
```

### 5.2. Deterministic Logic (Logic xác định) trước Agent autonomy (Tự chủ Agent)

Progression ưu tiên:

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

LLM không được thay deterministic business logic khi rule, formula hoặc policy check có thể biểu diễn rõ ràng.

### 5.3. Human Approval là first-class system boundary (ranh giới hệ thống cấp một)

Platform dùng ba risk level:

```text
RISK 0
→ auto execute

RISK 1
→ auto execute + mandatory audit

RISK 2
→ pause workflow
→ human approve/reject
→ resume hoặc terminate
```

RISK 2 có thể bao gồm publish, spend money, thay production/account settings, xóa dữ liệu quan trọng hoặc external action có hậu quả tương tự.

Classification (phân loại) cuối cùng do deterministic policy quyết định, không giao cho LLM tự định đoạt.

### 5.4. Durable Execution (Thực thi bền vững) khi workflow có thể chờ

Workflow có thể pause nhiều phút/giờ/ngày để chờ approval không được chỉ phụ thuộc in-memory process state.

Curriculum phải dạy:

- persisted workflow state (state workflow lưu bền vững);
- checkpoint/resume;
- retry/backoff;
- idempotency;
- timeout/cancellation;
- compensation (hành động bù);
- approval wait;
- crash/restart recovery.

Temporal là reference implementation, **không** phải dependency bắt buộc mọi Project.

### 5.5. Tool Boundary (Ranh giới công cụ) trước unrestricted action (hành động không giới hạn)

Agent action phải đi qua explicit tool/interface.

Tool engineering bao gồm:

- schema/contract;
- input/output validation;
- tách read và write;
- side-effect classification;
- permission;
- idempotency;
- timeout/retry;
- policy check;
- approval khi cần;
- audit evidence.

MCP là interoperability layer quan trọng, nhưng REST/webhook/native API vẫn đúng khi đơn giản hơn.

## 6. Hệ quả cho Agent Engineering

Curriculum phải mở rộng Bot Engineer vượt khỏi collector/scheduler code để bao gồm:

- tool engineering và MCP;
- state/session/memory boundaries;
- durable execution;
- agent evaluation (đánh giá agent);
- tracing và observability;
- prompt-injection/tool-misuse defenses;
- least-privilege tool permissions;
- approval và kill switch;
- policy-aware autonomous actions.

Multi-agent và A2A là advanced patterns (mẫu nâng cao), **không** là default architecture Phase 1.

## 7. Hệ quả cho curriculum

### Active primary stack

```text
Go
PostgreSQL
Redis chỉ khi justified
HTTP/API/Webhook adapters
queue/worker patterns
Docker
OpenTelemetry-style observability
MCP khi hữu ích
provider-neutral AI boundary
```

Reference implementation có thể dùng library/workflow engine hiện hành, nhưng library choice vẫn freshness-scoped.

### C#/.NET

C#/.NET:

- vẫn là comparison/reference material;
- vẫn tồn tại trong historical v2026.08 provenance;
- có thể dùng khi so sánh runtime/framework trade-off;
- không còn là active primary implementation path.

## 8. Non-goals (Những điều ADR không có nghĩa)

ADR này **không** có nghĩa:

- Go bắt buộc cho mọi analytical/ML component tương lai;
- Python không bao giờ được dùng cho ML/data workload có lý do;
- mọi Bot phải dùng MCP;
- mọi Bot phải dùng Temporal;
- mọi Bot phải dùng LLM;
- mọi workflow phải thành multi-agent;
- microservices là kiến trúc khởi đầu mong muốn.

## 9. Migration plan (Kế hoạch migration) lịch sử

Migration Go-first đã được thực hiện theo các stage:

1. canonical revision + ADR;
2. migrate engineering roadmap/lesson titles mà không đổi counts;
3. thêm Go engineering/autonomy/security standards + CI drift guards;
4. author lesson 0.2 thành Go-first Bot Engineer reference lesson;
5. Build-First migration sau đó đưa Go vào learner Mission từ M00.

Phần này là migration history, không phải danh sách việc “sẽ làm” trong tương lai.

## 10. Invariants (Bất biến phải giữ)

Migration phải bảo toàn:

```text
23 Parts
89 Chapters
671 lessons
14 main Projects
```

Technology decision có thể thay implementation guidance, example và selected lesson title, nhưng không được âm thầm thay curriculum structural counts.