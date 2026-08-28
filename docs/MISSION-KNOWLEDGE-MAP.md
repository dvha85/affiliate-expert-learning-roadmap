# Bản đồ Mission ↔ Knowledge

Đây là lớp mapping (ánh xạ) just-in-time (đúng lúc cần) tập trung. Tài liệu cố ý tránh bulk-edit (sửa hàng loạt) front matter của 671 Lesson.

## Ý nghĩa ba mức kiến thức

- **REQUIRED (Bắt buộc cho Mission)** — phải hiểu đủ để Mission PASS.
- **ON-DEMAND (Lấy khi phát sinh nhu cầu)** — pull khi implementation/business context làm lộ nhu cầu cụ thể.
- **REFERENCE (Tham khảo)** — hữu ích để đào sâu nhưng không phải Mission PASS gate.

Các Lesson ID được ghi explicit phải resolve (tra được) trong canonical inventory 671 bài. Khi một Mission đã được author `ready`, ưu tiên dùng **Lesson ID cụ thể + knowledge slice (phần kiến thức cần ngay)** thay vì chỉ ghi theme mơ hồ.

Quan trọng:

```text
REQUIRED FOR MISSION
≠
FULL LESSON PASS
```

Mission có thể yêu cầu hiểu một phần của Lesson để build đúng; full Lesson PASS vẫn được đánh giá độc lập theo `docs/PASS-CRITERIA.md`.

## M00 — Khởi động Affiliate Bot

**REQUIRED**

- `0.1` — Affiliate Expert là gì?
  - slice cần ngay: affiliate là business system, vai trò của Affiliate Expert, hiểu trước khi automate thật.
- `0.2` — Affiliate Bot Engineer là gì?
  - slice cần ngay: Bot Engineer biến business logic thành hệ thống; deterministic trước AI; Decision ≠ Execution.

**ON-DEMAND**

- Go tối thiểu để đọc `package main`, `func`, slice và test của learner workspace.

**REFERENCE**

- Part 15 là formal Bot Engineering mastery; không cần học hết trước M00.

## M01 — Product Ingest (đọc dữ liệu sản phẩm)

**REQUIRED**

- `38.1` — Core marketplace entities: Platform, Merchant, Seller, Product.
  - slice: Product identity và các field cốt lõi.
- `51.1` — Go runtime, modules và project structure.
  - slice: struct/type/package ở mức đủ để tạo Product model.
- `52.3` — File Import.
  - slice: đọc file local làm data source đầu tiên.
- `52.7` — Validation.
  - slice: syntax validation khác business validation như thế nào.

**ON-DEMAND**

- Platform-specific product fields chỉ thêm khi có adapter thật.
- Error wrapping/JSON details chỉ học sâu khi lỗi thực tế yêu cầu.

## M02 — Product Store & History (lưu trữ và lịch sử sản phẩm)

**REQUIRED**

- `38.2` — ProductSnapshot và dữ liệu lịch sử.
  - slice: product identity khác snapshot state theo thời gian.
- `39.1` — Snapshot.
  - slice: vì sao cần snapshot để so sánh thay đổi.
- `51.3` — PostgreSQL, Redis và data access.
  - slice: repository boundary, migration/schema và persistence contract; chưa cần Redis.

**ON-DEMAND**

- PostgreSQL driver/integration wiring khi learner thực sự bật local database.
- Data lineage/provenance học sâu hơn khi có nguồn dữ liệu ngoài.

## M03 — Product Ranking đầu tiên

**REQUIRED**

- `5.11` — Expected Value (Giá trị kỳ vọng).
  - slice: vì sao commission rate đơn lẻ không đại diện expected outcome.
- `27.3` — Ranking (Xếp hạng).
  - slice: score cần deterministic, có thể so sánh và giải thích.

**ON-DEMAND**

- Demand (Nhu cầu), Product–Audience Fit (Mức phù hợp sản phẩm–đối tượng), price, CVR, valid-order/refund risk, seller/product quality khi tiến tới M06.

**REFERENCE**

- Advanced statistical ranking (xếp hạng thống kê nâng cao) và AI scoring cố ý để sau.

## M04 — Product Watcher (Bot theo dõi sản phẩm)

**REQUIRED themes (chủ đề bắt buộc, sẽ refine khi author Mission)**

- snapshot/delta semantics;
- scheduler;
- context/cancellation.

**ON-DEMAND**

- bounded concurrency (đồng thời có giới hạn) khi collection tuần tự trở thành bottleneck thật.

## M05 — Reliable Alerts (cảnh báo đáng tin cậy)

**REQUIRED themes**

- rule/threshold;
- timeout;
- retry/backoff;
- idempotency/deduplication.

## M06 — Product Intelligence v1

**REQUIRED themes**

- Parts 2, 6, 7 và 8: economics + market + customer + product intelligence.

## M07 — Content Intelligence

**REQUIRED themes**

- Parts 9–11: content/psychology + traffic context + funnel/conversion.

## M08 — Revenue & Attribution Intelligence

**REQUIRED themes**

- Parts 2, 3, 11–13: economics, tracking/attribution, funnel, data, analytics.

## M09 — Experiment Engine

**REQUIRED themes**

- Part 14: experimentation/statistics.

## M10 — Decision & Policy Engine

**REQUIRED themes**

- Parts 8, 13, 15 và 16: product/analytics/bot/recommendation;
- Decision (quyết định) ≠ Execution (thực thi);
- RiskLevel + PolicyDecision.

## M11 — AI Analysis Assistant

**REQUIRED themes**

- Part 17: grounding, LLM workflow, evaluation và state separation.

## M12 — Tool-Using Bot

**REQUIRED themes**

- explicit tool contract (hợp đồng tool rõ ràng);
- validation;
- permissions (quyền hạn);
- MCP khi hữu ích.

## M13 — Governed Automation

**REQUIRED themes**

- ActionIntent;
- RISK 0/1/2;
- Human Approval;
- revalidation;
- audit.

## M14 — Production Bot

**REQUIRED themes**

- Part 19: recovery, observability, security, least privilege, kill switch và cost.

## M15 — Affiliate Intelligence Platform

**REQUIRED themes**

- Part 21 capstone integration và toàn bộ evidence cần cho governed closed loop (vòng khép kín có kiểm soát).

## Quy tắc refine (làm rõ mapping)

Khi một Mission được author thành `ready`, thay theme-level pulls bằng **tập Lesson ID nhỏ nhất thực sự cần cho Mission PASS**, kèm knowledge slice cụ thể. Không thêm hàng trăm mapping dự đoán trước khi có Mission thực tế.