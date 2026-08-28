# Phần 15 — AFFILIATE BOT ENGINEERING

- Timeline: **Standard M9–10 · Accelerated M7–8** — forecast; PASS evidence mới là gate.
- Quy mô: **7 chương / 42 bài**
- Chỉ tick bài khi đã đạt đủ [5 tiêu chí PASS](../docs/PASS-CRITERIA.md).

## Checklist bài học

### Chương 50 — Bot Architecture

- [ ] **50.1** — AffiliateBot boundaries và module map
- [ ] **50.2** — Collectors, adapters và Storage
- [ ] **50.3** — Core Analytics và Decision boundary
- [ ] **50.4** — Policy, Risk, Approval và Action boundary
- [ ] **50.5** — Interface, dependency flow, audit và architecture review

> **Architecture direction:** modular monolith first. Tách service khi scaling/failure boundary thật sự yêu cầu; không bắt đầu bằng microservices chỉ vì capstone lớn.

### Chương 51 — Technology Stack

- [ ] **51.1** — Go runtime, modules và project structure
- [ ] **51.2** — HTTP/API, context, goroutines và concurrency
- [ ] **51.3** — PostgreSQL, Redis và data access
- [ ] **51.4** — Configuration, interfaces, testing và background workers
- [ ] **51.5** — Docker, observability và lựa chọn production stack

> **Primary stack:** Go là implementation language chính. Alternate stacks chỉ dùng cho comparison/reference. Không hard-code framework/library hiện hành vào lesson title nếu concept có thể dạy framework-neutral.

### Chương 52 — Product Collector

- [ ] **52.1** — ProductSource interface và adapter boundary
- [ ] **52.2** — API Adapter, HTTP client và context
- [ ] **52.3** — File Import
- [ ] **52.4** — Export Import
- [ ] **52.5** — Web Data Collection
- [ ] **52.6** — Normalization và source provenance
- [ ] **52.7** — Validation
- [ ] **52.8** — Rate Limit
- [ ] **52.9** — Retry, timeout và cancellation
- [ ] **52.10** — Compliance

### Chương 53 — Scheduler & Pipeline

- [ ] **53.1** — Job, Workflow và execution state
- [ ] **53.2** — Scheduler, Trigger và event-driven execution
- [ ] **53.3** — Queue, Worker Pool và concurrency control
- [ ] **53.4** — Retry, Backoff và Timeout
- [ ] **53.5** — Idempotency và Deduplication
- [ ] **53.6** — Dead Letter, failure handling và Compensation
- [ ] **53.7** — Checkpoint, Resume và long-running Human Wait

> **Durable execution:** khi workflow có thể chờ approval hàng phút/giờ/ngày hoặc phải sống qua process restart, state phải được persist. Temporal có thể dùng làm reference implementation nhưng không phải dependency bắt buộc của mọi bot.

### Chương 54 — Product Tracker

- [ ] **54.1** — Theo dõi Price và Commission
- [ ] **54.2** — Theo dõi Sales và Rating
- [ ] **54.3** — Theo dõi Availability
- [ ] **54.4** — Theo dõi SellerQuality và ProductQuality
- [ ] **54.5** — Snapshot, provenance, history và tracker validation

### Chương 55 — Change Detection

- [ ] **55.1** — Price drop và price spike
- [ ] **55.2** — Commission increase và commission drop
- [ ] **55.3** — Sales spike và sales acceleration
- [ ] **55.4** — Stock out và product return
- [ ] **55.5** — Policy risk và chống cảnh báo giả

### Chương 56 — Alert Bot

- [ ] **56.1** — Thiết kế alert payload
- [ ] **56.2** — Severity, priority, risk level và routing
- [ ] **56.3** — Recommended Action có thể giải thích
- [ ] **56.4** — Chống alert fatigue
- [ ] **56.5** — Delivery, acknowledgement, approval link và audit trail

> **Autonomy boundary:** alert/recommendation không tự động đồng nghĩa execution. Action phải qua policy/risk classification; high-risk action đi vào approval queue.

> **2026 freshness note:** collectors/trackers must capture source provenance and observed/effective timestamps for changing platform facts. Automation must prefer official APIs/exports and compliant collection paths; rate limits, terms and allowed data access are current facts that require verification before implementation.

## Cổng thực hành

- [ ] **PROJECT 10 — Product Tracker Bot**
- [ ] Có artifact/evidence được lưu trong repo hoặc liên kết từ Issue
- [ ] Viết retrospective: kết quả, sai lệch, điều học được, bước tiếp theo

## Hoàn thành phần

- [ ] Tất cả bài học đã PASS
- [ ] Project/Lab/Pass Gate (nếu có) đã hoàn tất
- [ ] Knowledge Base đã cập nhật
- [ ] Đã chọn bài đầu tiên của phần tiếp theo

[← Roadmap tổng](../ROADMAP.md)
