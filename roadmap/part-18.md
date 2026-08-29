# Phần 18 — ADVANCED AFFILIATE INTELLIGENCE

- Timeline: **Standard M12–13 · Accelerated M10** — forecast; PASS evidence mới là gate.
- Quy mô: **6 chương / 35 bài**
- Chỉ tick bài khi đã đạt đủ [5 tiêu chí PASS](../docs/PASS-CRITERIA.md).

> Part 18 tạo predictive/ML evidence cho Decision Intelligence; model output không trực tiếp trở thành execution authority. Các estimate phải mang evaluation, data window, uncertainty/freshness và đi vào Decision Fusion của Part 16.

## Checklist bài học

### Chương 67 — Time-Series Analysis

- [ ] **67.1** — Trend
- [ ] **67.2** — Moving Average
- [ ] **67.3** — Momentum
- [ ] **67.4** — Seasonality
- [ ] **67.5** — Sales Velocity
- [ ] **67.6** — Acceleration

> Time-series signal dùng trong DecisionPacket phải ghi data window và regime/effective-date context khi platform metric đổi nghĩa.

### Chương 68 — Anomaly Detection

- [ ] **68.1** — Price anomaly
- [ ] **68.2** — Sales anomaly
- [ ] **68.3** — Commission anomaly
- [ ] **68.4** — Conversion anomaly
- [ ] **68.5** — Traffic anomaly và anomaly validation

> Anomaly là trigger để điều tra, không tự động là cause. M08 AI Investigator có thể tạo hypotheses nhưng observed fact và hypothesis phải tách.

### Chương 69 — Forecasting

- [ ] **69.1** — Traffic
- [ ] **69.2** — Click
- [ ] **69.3** — CVR
- [ ] **69.4** — Orders
- [ ] **69.5** — Commission
- [ ] **69.6** — Revenue

> Forecast dùng cho quyết định cần prediction horizon, data freshness, error/evaluation và uncertainty. Forecast hết horizon/đổi regime phải được re-evaluate trước action.

### Chương 70 — Machine Learning Foundation

- [ ] **70.1** — Dataset
- [ ] **70.2** — Feature
- [ ] **70.3** — Label
- [ ] **70.4** — Train/Test
- [ ] **70.5** — Regression
- [ ] **70.6** — Classification
- [ ] **70.7** — Evaluation
- [ ] **70.8** — Overfitting

### Chương 71 — Learning to Rank

- [ ] **71.1** — Bài toán Learning to Rank
- [ ] **71.2** — Features, labels và training examples
- [ ] **71.3** — Ranking model baseline
- [ ] **71.4** — TOP-K opportunity evaluation
- [ ] **71.5** — Explainability, retraining và drift

> Ranking model output là một evidence channel. Opportunity Engine vẫn phải tạo DecisionPacket có reason/evidence/confidence/uncertainty/freshness và policy context.

### Chương 72 — Explore vs Exploit

- [ ] **72.1** — Exploration
- [ ] **72.2** — Exploitation
- [ ] **72.3** — Multi-Armed Bandit
- [ ] **72.4** — Thompson Sampling — concept
- [ ] **72.5** — Adaptive Experimentation

> **Decision Intelligence rule:** `Rules + Scores + Ranking + Forecast/ML + Experiment Evidence + AI Analysis → Decision Fusion → DecisionPacket`. Confidence không phải execution permission; RISK2 vẫn cần approval bất kể model confidence cao.

> **2026 freshness note:** concept/model drift bao gồm platform-policy, creator-score và AI-discovery changes. Forecast/ranking evaluation phải annotate regime changes và tránh coi metric đã rename/redefine là continuous unchanged series.

> **Adaptive-automation safety boundary:** explore/exploit model có thể recommend action/bounded allocation nhưng không bypass Part 16/19 controls. Trước model-driven side effect phải có action space, budget/risk ceiling, stop condition, freshness/revalidation rule và approval requirement. Preferred flow: `model recommendation → DecisionPacket → Policy/Risk → auto or approval → execution → outcome/evaluation`.

Tài liệu liên quan:

- [`DECISION-INTELLIGENCE-STANDARD.md`](../docs/DECISION-INTELLIGENCE-STANDARD.md)
- [`CONFIDENCE-AND-UNCERTAINTY.md`](../docs/CONFIDENCE-AND-UNCERTAINTY.md)
- [`DATA-FRESHNESS-FOR-DECISIONS.md`](../docs/DATA-FRESHNESS-FOR-DECISIONS.md)

## Hoàn thành phần

- [ ] Tất cả bài học đã PASS
- [ ] Project/Lab/Pass Gate (nếu có) đã hoàn tất
- [ ] Knowledge Base đã cập nhật
- [ ] Đã chọn bài đầu tiên của phần tiếp theo

[← Roadmap tổng](../ROADMAP.md)
