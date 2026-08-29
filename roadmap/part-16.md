# Phần 16 — DECISION & RECOMMENDATION ENGINE

- Timeline: **Standard M11 · Accelerated M8** — forecast; PASS evidence mới là gate.
- Quy mô: **4 chương / 23 bài**
- Chỉ tick bài khi đã đạt đủ [5 tiêu chí PASS](../docs/PASS-CRITERIA.md).

> Part 16 là deterministic Decision/Policy core. Từ Agentic Decision Intelligence v1, AI có thể cung cấp `AnalysisPacket`, nhưng Decision Engine phải hợp nhất evidence theo contract tại [`DECISION-CONTRACTS.md`](../docs/DECISION-CONTRACTS.md); LLM không được là authority duy nhất cho policy hoặc consequential execution.

## Checklist bài học

### Chương 57 — Rule Engine

- [ ] **57.1** — Rule
- [ ] **57.2** — Condition
- [ ] **57.3** — Threshold
- [ ] **57.4** — Priority và Risk Level
- [ ] **57.5** — Explainability và Policy Decision

> Rule Engine không chỉ chấm điểm cơ hội; nó còn là deterministic policy layer bảo vệ action boundary. LLM không được tự quyết một mình liệu hành động consequential có được phép chạy hay không.

### Chương 58 — Scoring Engine

- [ ] **58.1** — Feature
- [ ] **58.2** — Normalization
- [ ] **58.3** — Weight
- [ ] **58.4** — Composite Score
- [ ] **58.5** — Calibration
- [ ] **58.6** — Validation

### Chương 59 — Ranking Engine

- [ ] **59.1** — Từ Products đến Features
- [ ] **59.2** — Từ Features đến Scores
- [ ] **59.3** — Ranking và tie-breaking
- [ ] **59.4** — TOP opportunities và diversity
- [ ] **59.5** — Đánh giá chất lượng ranking

### Chương 60 — Recommendation Engine

- [ ] **60.1** — Promote product nào?
- [ ] **60.2** — Audience nào?
- [ ] **60.3** — Content angle nào?
- [ ] **60.4** — Hook nào?
- [ ] **60.5** — Channel nào?
- [ ] **60.6** — Thời điểm nào?
- [ ] **60.7** — Khi nào nên dừng, execute hay yêu cầu approval?

> **Decision ≠ Execution.** Recommendation/DecisionPacket phải có reason/evidence/confidence/risk. Từ M10, cần thêm uncertainty, freshness/expiry và missing evidence khi relevant. Action execution là boundary riêng và phải tuân theo policy + RISK 0/1/2.

> **Decision Fusion pattern:** `Rules + Scores + Ranking + Forecast/ML + Experiment evidence + AI AnalysisPacket → DecisionPacket`. AI không được âm thầm override policy/rule; conflict phải hiện ra dưới dạng evidence, uncertainty hoặc yêu cầu lấy thêm dữ liệu.

> **2026 freshness note:** recommendation quality ngày càng phụ thuộc product truth, availability/price, policy eligibility và multi-surface discovery hiện hành. Emerging agentic-commerce protocol là input cần theo dõi, không phải lý do bỏ Human Approval.

## Cổng thực hành

- [ ] **PROJECT 11 — Opportunity Engine**
- [ ] Có artifact/evidence được lưu trong repo hoặc liên kết từ Issue
- [ ] Viết retrospective: kết quả, sai lệch, điều học được, bước tiếp theo

## Hoàn thành phần

- [ ] Tất cả bài học đã PASS
- [ ] Project/Lab/Pass Gate (nếu có) đã hoàn tất
- [ ] Knowledge Base đã cập nhật
- [ ] Đã chọn bài đầu tiên của phần tiếp theo

[← Roadmap tổng](../ROADMAP.md)
