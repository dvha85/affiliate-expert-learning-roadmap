# Phần 4 — RELIABLE INTELLIGENCE & DECISIONS

- Timeline: **Evidence-gated; reliability and evaluation cases determine completion**.
- **Chapters:** C12–C14
- **Core:** 9 micro-lessons
- **Missions:** M06–M07
- **Outcome:** Signal-to-decision service chịu được duplicate, stale/conflicting evidence và có quality/cost evaluation.

## Attempt trước knowledge pull

1. M06: chạy watcher với duplicate event và transient failure; lưu before behavior rồi mới thêm reliability.
2. M07: replay stale/missing/conflicting evidence rồi mới thêm DecisionPacket và abstention policy.

## Core checklist

### Chương 12 — Reliable signals và alerts

- [ ] **12.1** — Material change, threshold, severity và alert noise
- [ ] **12.2** — Retry, backoff, idempotency và deduplication
- [ ] **12.3** — Queue/recovery boundary, logs, metrics và correlation

### Chương 13 — Decision contracts

- [ ] **13.1** — SignalPacket → AnalysisPacket → DecisionPacket → ActionIntent
- [ ] **13.2** — Evidence, confidence, uncertainty, freshness và expiry
- [ ] **13.3** — Risk/policy boundary: WAIT, GET_MORE_DATA và HUMAN_REVIEW

### Chương 14 — Decision evaluation

- [ ] **14.1** — Deterministic baseline, eval dataset và success rubric
- [ ] **14.2** — Unsupported, stale, missing và conflicting-evidence cases
- [ ] **14.3** — Decision utility, latency, cost và human intervention rate

## Part PASS

- [ ] M06–M07 đều có Capability PASS, Reality verified và Operated
- [ ] Duplicate/retry không tạo alert hoặc record trùng
- [ ] Stale/missing/conflicting evidence dẫn tới trạng thái an toàn
- [ ] DecisionPacket có evidence/confidence/freshness/expiry
- [ ] Có baseline và eval report, không chỉ demo happy path

[← Part trước](part-03.md) · [Roadmap tổng](../ROADMAP.md) · [Part tiếp theo →](part-05.md)
