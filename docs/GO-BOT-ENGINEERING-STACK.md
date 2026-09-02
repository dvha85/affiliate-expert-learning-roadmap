# Go Bot Engineering Stack — Go implementation profile/reference

> Go là implementation profile/reference cho deterministic Bot từ v2 M02 khi
> phù hợp, không phải prerequisite cho v2 M00. Sequence authority nằm tại
> [`CURRICULUM.md`](../CURRICULUM.md) và implementation flexibility ở
> [`ADR-004`](ADR-004-DETERMINISTIC-CORE-IMPLEMENTATION-FLEXIBILITY.md).

Tiếng Việt là ngôn ngữ chính. English terminology (thuật ngữ tiếng Anh) được giữ để đối chiếu kỹ thuật và có giải thích tiếng Việt ở lần xuất hiện quan trọng. Xem [`LANGUAGE-POLICY.md`](LANGUAGE-POLICY.md) và [`GLOSSARY-VI.md`](GLOSSARY-VI.md).

## 1. Quy tắc chính

```text
GO PROFILE = AUDITABLE DETERMINISTIC IMPLEMENTATION OPTION
(Go là lựa chọn triển khai deterministic có thể audit)
```

No-code/visual rule profile hoặc agent-maintained code đều có thể hợp lệ nếu
giữ parity, test, audit, fail-closed và ownership contract. C#/.NET vẫn là
comparison/reference material, không phải default implementation path.

## 2. Kiến trúc mặc định

Bắt đầu bằng **Modular Monolith (Khối đơn thể mô-đun)**:

```text
Go application
├── api/
├── collectors/
├── adapters/
├── storage/
├── analytics/
├── decision/
├── policy/
├── approval/
├── executor/
├── workflows/
└── observability/
```

Chỉ tách service khi independent scaling (mở rộng độc lập), security isolation (cách ly bảo mật), deployment ownership hoặc failure containment (khoanh vùng lỗi) thực sự yêu cầu.

## 3. Stack ưu tiên

### Language/runtime (Ngôn ngữ/môi trường chạy)

- dùng một Go stable release (bản ổn định) đang còn support;
- dùng Go modules;
- ưu tiên standard library (thư viện chuẩn) trước khi thêm framework.

### HTTP và external APIs

- học `net/http` mental model trước;
- dùng `context.Context` cho deadline/cancellation (hạn thời gian/hủy);
- retry/backoff policy (chính sách thử lại/tăng thời gian chờ) phải explicit;
- phân biệt transient failure (lỗi tạm thời) và permanent failure (lỗi lâu dài/cố định);
- validate dữ liệu bên ngoài trước khi đưa vào core model.

### Concurrency (Xử lý đồng thời)

Dùng goroutine/channel/worker pool có chủ ý.

Phải hiểu:

- bounded concurrency (đồng thời có giới hạn);
- cancellation propagation (lan truyền tín hiệu hủy);
- backpressure (hãm tải khi downstream quá tải);
- race avoidance (tránh race condition);
- worker lifecycle (vòng đời worker);
- graceful shutdown (tắt dịch vụ có kiểm soát).

Không đồng nhất “nhiều goroutine hơn” với throughput tốt hơn khi platform rate limit mới là bottleneck.

### Database (Cơ sở dữ liệu)

Primary relational store (kho quan hệ chính):

```text
PostgreSQL
```

Chỉ dùng Redis khi có requirement cụ thể như caching, ephemeral coordination (phối hợp tạm thời) hoặc rate-limit state.

### Workflow execution (Thực thi workflow)

Progression khuyến nghị:

```text
function
→ job
→ scheduled worker
→ queue-backed workflow
→ durable workflow khi state phải sống qua restart/chờ lâu
```

Durable engine như Temporal là reference implementation, không phải dependency bắt buộc của mọi Bot.

### Tool boundary (Ranh giới công cụ)

Các kiểu integration (tích hợp) được hỗ trợ:

```text
REST API
Webhook
native SDK
file/export import
MCP khi interoperability (khả năng liên thông) mang lại giá trị
```

Tool contract (hợp đồng công cụ) phải định nghĩa:

- input/output schema;
- side effect (tác động bên ngoài);
- permission (quyền hạn);
- timeout;
- retry;
- idempotency (tính lặp an toàn);
- policy;
- audit behavior (hành vi ghi vết).

### AI layer (Lớp AI)

Ưu tiên provider-neutral application interface (giao diện ứng dụng ít phụ thuộc nhà cung cấp) khi hợp lý.

Thứ tự ưu tiên:

```text
deterministic rule (quy tắc xác định)
→ deterministic algorithm (thuật toán xác định)
→ model call
→ tool-using agent (agent dùng công cụ)
```

Không dùng LLM thay thế business rule xác định chỉ vì LLM có sẵn.

### Observability (Khả năng quan sát hệ thống)

Baseline mental model:

```text
structured logs
+ metrics
+ traces
+ business events
+ workflow/action audit
```

OpenTelemetry là current reference standard. Chi tiết package/version thuộc freshness layer, không phải canonical constant.

### Packaging/deployment (Đóng gói/triển khai)

- Docker khi container deployment hữu ích;
- Go binary/service nhỏ, đơn giản;
- validate environment/config khi startup;
- graceful shutdown;
- health/readiness checks;
- database migration là deployment step có kiểm soát.

## 4. Freshness snapshot (ảnh chụp kiến thức hiện hành)

Verified 2026-08-28:

- Go 1.27.0 phát hành 2026-08-19;
- official MCP Go SDK được xếp Tier 1 và hỗ trợ protocol line 2026-07-28;
- Temporal Go SDK là reference cho durable long-running workflow;
- OpenTelemetry Go: traces/metrics stable, logs beta.

Không biến các version cụ thể này thành permanent lesson invariant.

Current learner/reference bootstrap trong repo dùng Go 1.27 tại thời điểm hardening này, nhưng future update phải tiếp tục theo freshness policy thay vì giữ 1.27 vĩnh viễn.

## 5. Development progression (tiến trình phát triển) mặc định

```text
manual workflow (quy trình thủ công)
→ Go function
→ tested package
→ API/worker
→ reliable pipeline (pipeline đáng tin cậy)
→ durable workflow
→ AI-assisted workflow (workflow có AI hỗ trợ)
→ tool-using agent
→ governed autonomous system (hệ thống tự chủ có kiểm soát)
```

## 6. Anti-patterns (cách làm cần tránh)

Tránh:

- microservices trước khi có operational need;
- unlimited goroutines (goroutine không giới hạn);
- retry mà không có idempotency;
- in-memory state cho approval wait dài;
- vendor SDK types lan khắp domain model;
- LLM truy cập trực tiếp high-impact side effect;
- tool call không validation/audit;
- thêm Redis/queue/workflow engine khi chưa có bài toán cụ thể;
- tối ưu CPU trước khi đo external I/O và rate-limit bottleneck.

## 7. Nguyên tắc sư phạm cho learner

```text
USE GO EARLY (dùng Go sớm)
≠
CLAIM GO MASTERY EARLY (tuyên bố làm chủ Go sớm)
```

Learner dùng Go scope hẹp từ M00; engineering mastery được chứng minh dần bằng Mission/Milestone evidence, không bằng việc hoàn thành một Part lý thuyết riêng.
