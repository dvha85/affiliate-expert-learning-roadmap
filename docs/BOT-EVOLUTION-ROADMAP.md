# Lộ trình tiến hóa Bot — M00 đến M15

Tài liệu này định nghĩa **product/evidence spine (xương sống sản phẩm/bằng chứng)** của Build-First Learning Architecture v1. Nó không thay thế canonical knowledge inventory 23/89/671 hay 14 main Projects.

| Mission | Bot Version | AI level | Ship target (Mục tiêu bàn giao) | Knowledge theme chính |
|---|---:|---|---|---|
| M00 | v0.0 | A0 | Bot khởi động và tạo output quan sát được | định hướng Affiliate/Bot, Go tối thiểu |
| M01 | v0.1 | A0 | Product ingest + validation | product cơ bản, struct, JSON, error |
| M02 | v0.2 | A0 | Product persistence + snapshots/history | data model, SQL, repository, history |
| M03 | v0.3 | A0 | Product ranking đầu tiên + before/after scoring | economics, Expected Value, Product Intelligence |
| M04 | v0.4 | A0 | Product watcher phát hiện thay đổi | scheduler, context, delta, concurrency |
| M05 | v0.5 | A1 | Reliable alerts + advisory triage | rule, timeout, retry, idempotency, alert triage |
| M06 | v1.0 | A1 | Product Intelligence + AI research | market, customer, product, economics, risk |
| M07 | v2.0 | A1 | Content Intelligence | content, CTR/CVR, psychology, funnel signals |
| M08 | v3.0 | A1 | Revenue & Attribution Intelligence + investigation | tracking, order, validation, commission, reconciliation |
| M09 | v4.0 | A1 | Experiment Engine + AI copilot | hypothesis, statistics, experiment logging |
| M10 | v5.0 | A1 | Decision Intelligence & Policy Engine | score/rank/recommendation, confidence, freshness, RiskLevel, PolicyDecision |
| M11 | v6.0 | A2 | AI Analysis Assistant | grounded LLM, model routing, evaluation, state separation |
| M12 | v7.0 | A2 | Tool-Using Agent | tool registry, MCP khi hữu ích, validation/permission |
| M13 | v8.0 | A3 | Governed Automation | ActionIntent, RISK 0/1/2, Human Approval, audit |
| M14 | v9.0 | A3 | Production Agentic Bot | recovery, observability, evaluation, security, kill switch, cost |
| M15 | v10.0 | A4 optional | Affiliate Intelligence Platform | governed closed-loop intelligence; multi-agent chỉ khi cần thật |

AI levels được định nghĩa tại [`AI-CAPABILITY-LEVELS.md`](AI-CAPABILITY-LEVELS.md).

## Quan hệ phụ thuộc giữa Mission

```text
M00 → M01 → M02 → M03 → M04 → M05 → M06 → M07 → M08
    → M09 → M10 → M11 → M12 → M13 → M14 → M15
```

Chuỗi chính cố ý giữ đơn giản cho một learner. Side Mission tùy chọn không được làm thay M00–M15 main spine.

## Mẫu sư phạm Build-First

M03 vẫn là mẫu tham chiếu:

```text
Build naive ranking
→ quan sát commission-rate-only ranking còn yếu
→ pull economics/product knowledge đúng lúc
→ cải tiến công thức
→ so sánh before/after
→ giải thích vì sao ranking thay đổi
```

M05+ mở thêm pattern:

```text
deterministic signal
→ AI advisory analysis khi có giá trị
→ evidence/confidence/uncertainty
→ deterministic Decision/Policy boundary
```

Điểm quan trọng: learner workspace không được chứa sẵn lời giải Mission sau. Reference implementation có thể tồn tại riêng để đối chiếu nhưng không phải learner starting state.

## Decision Intelligence progression

```text
M04  detect change
M05  prioritize/triage signals
M06  enrich Product Intelligence
M08  investigate revenue/attribution anomalies
M09  interpret experiments
M10  fuse evidence into DecisionPacket
M11  improve AI reasoning/routing/evaluation
M12  collect missing evidence through tools
M13  create governed ActionIntent
M14  operate safely/reliably in production
M15  close the outcome-learning loop
```

Bốn logical contract xuyên suốt:

```text
SignalPacket → AnalysisPacket → DecisionPacket → ActionIntent
```

Xem [`DECISION-CONTRACTS.md`](DECISION-CONTRACTS.md).

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

Mission contribution không tự động nghĩa Project PASS.

## Tiến trình an toàn

```text
M00–M04: A0 deterministic
M05–M10: A1 AI advisory/read-only; không external AI authority
M11–M12: A2 AI/tool capability có validation/permission
M13–M14: A3 governed external action model
M15: A4 optional multi-agent, vẫn giữ cùng policy/risk boundary
```

```text
BUILD CODE EARLY
≠
AUTOMATE REAL BUSINESS EARLY

AI APPEARS EARLY
≠
AI GETS AUTHORITY EARLY
```

Không đưa consequential auto-execution lên Mission đầu chỉ để Bot trông nâng cao hơn.