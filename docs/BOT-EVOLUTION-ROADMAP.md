# Lộ trình tiến hóa Bot — M00 đến M15

Tài liệu này định nghĩa **product/evidence spine (xương sống sản phẩm/bằng chứng)** của Build-First Learning Architecture v1. Nó không thay thế canonical knowledge inventory (kho kiến thức chuẩn) 23/89/671 hay 14 main Projects.

| Mission | Bot Version | Ship target (Mục tiêu bàn giao) | Knowledge theme (chủ đề kiến thức) chính |
|---|---:|---|---|
| M00 | v0.0 | Bot khởi động và tạo output quan sát được | định hướng Affiliate/Bot, Go tối thiểu |
| M01 | v0.1 | Product ingest + validation (đọc + kiểm tra dữ liệu sản phẩm) | product cơ bản, struct, JSON, error |
| M02 | v0.2 | Product persistence + snapshots/history (lưu trữ + lịch sử) | data model, SQL, repository, history |
| M03 | v0.3 | Product ranking (xếp hạng) đầu tiên + before/after scoring | economics, Expected Value, Product Intelligence |
| M04 | v0.4 | Product watcher phát hiện thay đổi | scheduler, context, delta, concurrency |
| M05 | v0.5 | Reliable alerts (cảnh báo đáng tin cậy) | rule, timeout, retry, idempotency |
| M06 | v1.0 | Product Intelligence v1 | market, customer, product, economics, risk |
| M07 | v2.0 | Content Intelligence | content, CTR/CVR, psychology, funnel signals |
| M08 | v3.0 | Revenue & Attribution Intelligence | tracking, order, validation, commission, reconciliation |
| M09 | v4.0 | Experiment Engine | hypothesis, statistics, experiment logging |
| M10 | v5.0 | Decision & Policy Engine | score/rank/recommendation, confidence, RiskLevel, PolicyDecision |
| M11 | v6.0 | AI Analysis Assistant | grounded LLM, evaluation, state separation |
| M12 | v7.0 | Tool-Using Bot | tool contract rõ ràng, MCP khi hữu ích, tool validation |
| M13 | v8.0 | Governed Automation | ActionIntent, RISK 0/1/2, Human Approval, audit |
| M14 | v9.0 | Production Bot | recovery, observability, security, kill switch, cost |
| M15 | v10.0 | Affiliate Intelligence Platform | governed feedback loop (vòng phản hồi có kiểm soát) end-to-end |

## Quan hệ phụ thuộc giữa Mission

```text
M00 → M01 → M02 → M03 → M04 → M05 → M06 → M07 → M08
    → M09 → M10 → M11 → M12 → M13 → M14 → M15
```

Chuỗi chính cố ý giữ đơn giản cho một learner. Về sau có thể có side mission (nhiệm vụ nhánh) tùy chọn mà không thay M00–M15 main spine.

## Mẫu sư phạm Build-First

M03 là mẫu tham chiếu:

```text
Build naive ranking (xếp hạng đơn giản)
→ quan sát commission-rate-only ranking còn yếu
→ pull economics/product knowledge đúng lúc
→ cải tiến công thức
→ so sánh before/after
→ giải thích vì sao ranking thay đổi
```

Điểm quan trọng: learner workspace không được chứa sẵn lời giải M03 từ M00. Reference implementation có thể tồn tại riêng để đối chiếu, nhưng không phải starting state của learner.

## Đóng góp vào canonical Project

Mission evidence có thể đóng góp vào canonical Project mà không tạo Project ID mới:

- M02 + M08 → Project 7 — Affiliate Data Warehouse
- M03 + M06 → Project 4 — Product Intelligence
- M04 + M05 → Project 10 — Product Tracker Bot
- M07 → Project 5 — Real Content Portfolio
- M09 → Project 9 — Experiment System
- M10 → Project 11 — Opportunity Engine
- M11 + M12 → Project 12 — AI Content Assistant
- M14 → Project 13 — Production Affiliate Bot
- M15 → Project 14 — Affiliate Intelligence Platform

Mission contribution (đóng góp bằng chứng) không tự động nghĩa Project PASS.

## Tiến trình an toàn

```text
M00–M09: chủ yếu internal/read-only/sample side effects
M10: deterministic decision/policy boundary
M11–M12: AI/tool capability có validation
M13: governed external action model
M14–M15: production reliability/security/governance
```

```text
BUILD CODE EARLY (viết code sớm)
≠
AUTOMATE REAL BUSINESS EARLY (tự động hóa kinh doanh thật sớm)
```

Không đưa consequential auto-execution (tự thực thi có hậu quả đáng kể) lên Mission đầu chỉ để Bot trông nâng cao hơn.