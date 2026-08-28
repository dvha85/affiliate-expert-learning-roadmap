# Phần 12 — DATA ENGINEERING FOR AFFILIATE

- Timeline: **Standard M8 · Accelerated M6** — forecast; PASS evidence mới là gate.
- Quy mô: **4 chương / 23 bài**
- Chỉ tick bài khi đã đạt đủ [5 tiêu chí PASS](../docs/PASS-CRITERIA.md).

## Checklist bài học

### Chương 38 — Affiliate Data Model

- [ ] **38.1** — Core marketplace entities: Platform, Merchant, Seller, Product
- [ ] **38.2** — ProductSnapshot và dữ liệu lịch sử
- [ ] **38.3** — Audience, Content và ContentMetric
- [ ] **38.4** — AffiliateLink, Click, Order và Commission
- [ ] **38.5** — Experiment, Variant, Event và quan hệ dữ liệu

### Chương 39 — Historical Data

- [ ] **39.1** — Snapshot
- [ ] **39.2** — Event
- [ ] **39.3** — Time-series
- [ ] **39.4** — Slowly Changing Data
- [ ] **39.5** — Data Versioning
- [ ] **39.6** — Data Lineage

### Chương 40 — Data Quality

- [ ] **40.1** — Missing Data
- [ ] **40.2** — Duplicate
- [ ] **40.3** — Outlier
- [ ] **40.4** — Invalid Data
- [ ] **40.5** — Data Freshness
- [ ] **40.6** — Data Consistency
- [ ] **40.7** — Reconciliation Error

### Chương 41 — Metrics Engine

- [ ] **41.1** — Thiết kế Metrics Engine
- [ ] **41.2** — Tính CTR và CVR
- [ ] **41.3** — Tính EPC, RPM và AOV
- [ ] **41.4** — Tính Revenue và Refund Rate
- [ ] **41.5** — Tính Sales Velocity và kiểm thử công thức

> **2026 freshness note:** current platform/policy/product signals cần lưu `source`, `observed_at/effective_at`, version và confidence khi có thể. Data model không nên biến commission, eligibility, policy state hoặc product-quality score thành thuộc tính bất biến.

> **Operational-data evolution:** Part 12 xây **affiliate domain data**. Parts 15–19 mở rộng cùng hệ thống bằng operational entities như `Workflow`, `ActionIntent`, `PolicyDecision`, `ApprovalRequest`, `ApprovalDecision`, `ExecutionRecord` và trace/correlation IDs. Không cần nhồi các entity này vào Ch38 trước khi học automation, nhưng schema/correlation phải cho phép nối `business event → decision → action → result` thay vì tạo một “bot database” tách rời không truy vết được.

## Cổng thực hành

- [ ] **PROJECT 7 — Affiliate Data Warehouse**
- [ ] Có artifact/evidence được lưu trong repo hoặc liên kết từ Issue
- [ ] Viết retrospective: kết quả, sai lệch, điều học được, bước tiếp theo

## Hoàn thành phần

- [ ] Tất cả bài học đã PASS
- [ ] Project/Lab/Pass Gate (nếu có) đã hoàn tất
- [ ] Knowledge Base đã cập nhật
- [ ] Đã chọn bài đầu tiên của phần tiếp theo

[← Roadmap tổng](../ROADMAP.md)
