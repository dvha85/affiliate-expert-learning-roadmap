# Phần 3 — Cải tiến dựa trên outcome

- Timeline: **Evidence-gated; experiment duration follows the declared observation window**.
- **Chapters:** C9–C11
- **Core:** 9 micro-lessons
- **Mission:** M05
- **Outcome:** Một thay đổi được đi từ observation đến hypothesis, outcome, reviewed decision và version/rollback rõ ràng.

## Hybrid ownership trong Part 03

```text
Go
= outcome truth + experiment/evaluation contract + release/reject decision

n8n
= optional reporting/orchestration; không quyết định experiment result

Agent/AI
= advisory/analysis; không tự sửa formula/prompt/production behavior
```

Part 03 không tăng execution authority. Orchestration chỉ hỗ trợ workflow; hypothesis, metric, outcome interpretation và reviewed improvement vẫn phải audit được độc lập khỏi runtime.

## Attempt trước knowledge pull

Chọn một bất đồng hoặc weak assumption từ M00–M04. Viết proposed change trước, không sửa formula/prompt chỉ để khớp intuition hoặc làm số đẹp hơn.

Nếu dùng orchestration để thu/report data, freeze hypothesis/metric trước outcome và giữ canonical event/outcome semantics trong Go/domain contract.

Trước khi gọi một khác biệt là experiment effect, so `MeasurementContext` của baseline và variant. Nếu source/scope/attribution/window/config không tương thích, result phải downgrade thành limitation/inconclusive hoặc được reconcile trước.

## Core checklist

### Chương 9 — Outcome truth và attribution limits

- [ ] **9.1** — Event identity và nối Decision → Action → Outcome
- [ ] **9.2** — Pending, valid, final, refunded commission và reconciliation state
- [ ] **9.3** — Delayed outcome, attribution uncertainty và data-quality boundary

Chương 9 phải giữ rõ:

```text
metric value
+ measurement context
→ interpretable outcome
```

và:

```text
same label
+ different attribution/source/window context
≠ automatically comparable result
```

Nếu nhiều source reporting cùng outcome nhưng khác nhau, preserve `MATCHED | EXPLAINED_DIFFERENCE | CONFLICTING | INSUFFICIENT_CONTEXT` thay vì overwrite.

### Chương 10 — Experiment nhỏ nhưng trung thực

- [ ] **10.1** — Observation, question, hypothesis và falsifiable expectation
- [ ] **10.2** — Baseline, primary metric, noise, sample nhỏ và stop rule
- [ ] **10.3** — Result, inconclusive, decision và next evidence

Experiment preregistration phải freeze không chỉ metric name mà còn measurement scope/window/context đủ để interpretation không đổi sau khi thấy outcome.

### Chương 11 — Controlled improvement

- [ ] **11.1** — Decision–Outcome Memory và calibration note
- [ ] **11.2** — Proposed change, offline test và versioned evaluation
- [ ] **11.3** — Human review, release/reject, rollback và retrospective

## Revenue reconciliation boundary

Khi source expose financial states, giữ tách:

```text
Order
→ Valid Order
→ Final Commission
→ Paid Commission
→ Net Payout nếu observable
```

Optional observed fields như `platform_adjustment` hoặc `tax_withheld` được giữ như financial evidence; không suy một mức thuế Affiliate phổ quát từ platform export.

## Runtime invariants

```text
workflow success
≠ experiment success

import success
≠ measurement completeness

Agent recommendation
≠ evidence that change works

report generation failure
≠ permission to invent/carry-forward outcome
```

Nếu n8n/Agent unavailable, learner vẫn phải đọc được canonical experiment evidence và đưa ra reviewed result từ dữ liệu đã lưu.

## Part PASS

- [ ] M05 có Capability PASS, Reality verified cấp E4 và Operated
- [ ] Experiment có hypothesis và declared metric trước outcome review
- [ ] Baseline/variant measurement context tương thích hoặc limitation/reconciliation được ghi rõ
- [ ] Decision liên kết được với action/outcome hoặc ghi rõ vì sao chưa thể
- [ ] Kết quả inconclusive không bị ép thành success/failure
- [ ] Source/attribution mismatch không bị trình bày như treatment effect
- [ ] Improvement qua test/review; không có silent self-modification
- [ ] Orchestration/Agent không thay outcome truth hoặc release authority

[← Part trước](part-02.md) · [Roadmap tổng](../ROADMAP.md) · [Part tiếp theo →](part-04.md)
