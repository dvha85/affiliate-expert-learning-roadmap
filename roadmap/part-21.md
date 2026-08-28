# Phần 21 — CAPSTONE

- Timeline: **Standard M14–15 · Accelerated M11–12** — forecast; PASS evidence mới là gate.
- Quy mô: **2 chương / 17 bài**
- Chỉ tick bài khi đã đạt đủ [5 tiêu chí PASS](../docs/PASS-CRITERIA.md).

## Checklist bài học

### Chương 83 — Affiliate Intelligence Platform

- [ ] **83.1** — Data Sources, Collection và Source Provenance
- [ ] **83.2** — Historical Data, Analytics và Observability
- [ ] **83.3** — Opportunity, Experiment và Workflow Engine
- [ ] **83.4** — AI, Tool Registry/MCP và Recommendation Engine
- [ ] **83.5** — Policy/Risk Engine, Approval Queue và Action Executor
- [ ] **83.6** — Revenue, Evaluation và data feedback loop

> Target capstone architecture:
>
> ```text
> Data Sources
> → Collection / Provenance
> → Historical Data
> → Analytics
> → Opportunity / Experiment / Recommendation
> → Tool Registry / Action Boundary
> → Policy & Risk Engine
> → RISK 0/1: controlled auto action
> → RISK 2: Approval Queue → Human approve/reject
> → Action Executor
> → Audit / Trace Store
> → Result / Revenue
> → Evaluation / Feedback
> ↺
> ```
>
> Các block trên là **logical capabilities**, không bắt buộc mỗi block là một microservice.

### Chương 84 — Capstone Versions

- [ ] **84.1** — V0 — Manual Affiliate Lab
- [ ] **84.2** — V1 — Product Database
- [ ] **84.3** — V2 — Product Tracker
- [ ] **84.4** — V3 — Product Finder
- [ ] **84.5** — V4 — Opportunity Engine
- [ ] **84.6** — V5 — Analytics Dashboard
- [ ] **84.7** — V6 — AI Content Assistant
- [ ] **84.8** — V7 — Experiment & Durable Workflow Engine
- [ ] **84.9** — V8 — Recommendation + Governed Action Engine
- [ ] **84.10** — V9 — Affiliate Intelligence Platform
- [ ] **84.11** — V10 — Affiliate SaaS

> **Go-first implementation note:** capstone bắt đầu như modular Go application; chỉ tách service khi có operational reason rõ như independent scaling, security boundary hoặc failure isolation.

> **2026 freshness note:** capstone should treat policy/platform/legal/search updates as first-class data inputs with provenance and effective dates. The target loop is not just `collect → rank → publish`; it is `collect → verify → analyze → recommend → approve/act → measure → learn`, with compliance and freshness gates throughout.

## Cổng thực hành

- [ ] **PROJECT 14 — Affiliate Intelligence Platform**
- [ ] Có artifact/evidence được lưu trong repo hoặc liên kết từ Issue
- [ ] Viết retrospective: kết quả, sai lệch, điều học được, bước tiếp theo

## Hoàn thành phần

- [ ] Tất cả bài học đã PASS
- [ ] Project/Lab/Pass Gate (nếu có) đã hoàn tất
- [ ] Knowledge Base đã cập nhật
- [ ] Đã chọn bài đầu tiên của phần tiếp theo

[← Roadmap tổng](../ROADMAP.md)
