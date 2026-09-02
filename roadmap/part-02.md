# Phần 2 — Vòng thị trường có tracking đầu tiên và orchestration an toàn đầu tiên

- Timeline: **Evidence-gated; includes a real observation window**.
- **Chapters:** C6–C8
- **Core:** 9 micro-lessons
- **Missions:** M03–M04
- **Outcome:** Learner thực hiện một publication thủ công có disclosure/tracking, đọc outcome thật, so human baseline với AI-assisted variant và lần đầu dùng orchestration read-only để import/reconcile analytics mà không tăng authority của Bot.

## Hybrid ownership trong Part 02

```text
Go
= tracking/event identity + validation + reconciliation + decision truth

n8n
= chỉ bắt đầu ở M04 dưới dạng read-only orchestration learning slice

Agent/AI
= advisory only, no tools/write authority

Human
= actor duy nhất được publish trong M03–M04
```

Part 02 không cho n8n hoặc Agent publish, send, spend hoặc thay platform/account state.

## Attempt trước knowledge pull

1. M03: chọn một product/audience problem và tự viết micro-content trước khi dùng framework hoặc AI.
2. Human review và manual publish; Bot/n8n/Agent không có publish authority.
3. M04: chờ declared observation window, import analytics thật rồi mới giải thích outcome.
4. Khi import outcome, learner ghi cả **measurement context (ngữ cảnh đo lường)**: source/scope, tracking identity, attribution/window nếu known, timezone/config timestamp khi relevant và import/data-quality status.
5. Trước khi automation sâu hơn, learner thử một **read-only orchestration path** nhỏ nhất cho analytics import: manual trigger → map/import → gọi Go validation/reconciliation → report. Failure của orchestration không được làm hỏng canonical evidence/history.

## Core checklist

### Chương 6 — Compliant micro-pilot

- [ ] **6.1** — Audience problem, product fit và một testable content angle
- [ ] **6.2** — Proof, claims, disclosure và current platform boundary
- [ ] **6.3** — Human review, manual publish và Decision ≠ Execution

### Chương 7 — Track real market signals

- [ ] **7.1** — Tracking ID, UTM/link, impression, click và outcome event
- [ ] **7.2** — Observation window, zero, missing và not-yet-observable
- [ ] **7.3** — Import analytics/export, provenance và reconciliation

M04 implementation reference cho Chương 7.3 có thể dùng n8n để học orchestration read-only, nhưng canonical validation/reconciliation semantics vẫn thuộc Go/domain contract.

Từ M04, analytics/outcome quan trọng phải reference một `MeasurementContext` hoặc equivalent canonical record. Minimum logical shape:

```yaml
measurement_context_id:
reporting_source:
reporting_scope:
tracking_id:
campaign_id:
attribution_model:
attribution_lookback_window:
reporting_timezone:
configuration_observed_at:
import_validation_status:
data_freshness:
limitations: []
```

Field mà source không expose phải là `unknown`/`not_available`, không invent.

Invariant:

```text
same metric name
+ different source/scope/attribution/window/config
≠ directly comparable truth
```

Nếu platform analytics và một analytics source khác cho số khác nhau, learner phải reconcile hoặc giữ `EXPLAINED_DIFFERENCE`/`CONFLICTING`/`INSUFFICIENT_CONTEXT`; không chọn số thuận lợi hơn.

### Chương 8 — Human-vs-AI content comparison

- [ ] **8.1** — Human baseline trước AI-assisted variant
- [ ] **8.2** — Publish manually, freeze variants và record performance
- [ ] **8.3** — Compare outcome, preserve uncertainty và chọn next measurement

Comparison chỉ hợp lệ khi hai variant có measurement context tương thích đủ để so hoặc limitation được ghi rõ. Không biến khác biệt attribution/reporting scope thành “AI lift”.

## First orchestration learning slice — M04

Mục tiêu không phải “học hết n8n”, mà chứng minh separation:

```text
manual trigger
→ n8n read-only/import workflow
→ analytics/export payload + measurement metadata
→ Go validate + reconcile
→ canonical outcome/report
```

Learner cần quan sát tối thiểu:

- workflow input/output mapping;
- execution failure rõ;
- duplicate import không tạo duplicate canonical outcome;
- secret không nằm trong workflow artifact/log;
- n8n unavailable không biến `missing` thành `0`;
- import/workflow success không biến payload thiếu context thành canonical comparable truth;
- Go validation reject invalid/incompatible payload dù workflow chạy thành công.

Nếu n8n không available hoặc không justified, equivalent manual/read-only orchestration fixture có thể dùng cho Capability; runtime choice không thay evidence gate của M04.

## Part PASS

- [ ] M03 đạt E2: có publication thật do human duyệt/thực hiện
- [ ] M04 đạt E3: có analytics/export thật sau observation window
- [ ] Disclosure và claim boundary được kiểm tra
- [ ] `0` không bị lẫn với missing data
- [ ] Outcome quan trọng ở M04 truy được về `MeasurementContext` hoặc equivalent source/scope/config evidence
- [ ] Khác source/attribution/window được reconcile hoặc giữ limitation/conflict; không chọn metric thuận lợi
- [ ] Có human-vs-AI comparison; outcome xấu hoặc inconclusive vẫn hợp lệ nếu measurement trung thực
- [ ] First orchestration slice không có external mutation và không bypass Go validation/reconciliation
- [ ] Orchestrator failure không làm mất/corrupt canonical evidence

[← Part trước](part-01.md) · [Roadmap tổng](../ROADMAP.md) · [Part tiếp theo →](part-03.md)
