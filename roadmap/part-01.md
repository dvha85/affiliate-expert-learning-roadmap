# Phần 1 — Outcome và deterministic baseline

- Timeline: **Evidence-gated; M01 và M02 có thể chạy song song sau M00**.
- **Chapters:** C3–C5
- **Core:** 9 micro-lessons
- **Mission focus v2:** M01 First Outcome Snapshot + M02 Smallest Deterministic Bot; C3–C5 giữ knowledge lineage cho M03/M04.

## Cách đọc Part 01 trong v2

Canonical projection nằm tại [`lessons/V2-LESSON-MAP.json`](../lessons/V2-LESSON-MAP.json). Front matter cũ của `3.x–5.x` là historical v1 metadata, không phải active Mission order.

### Chương 3 — Minimal trustworthy ingest

- [ ] **3.1** — [Stable subject identity, observation identity và schema vừa đủ](../lessons/part-01/chapter-03/3.1-subject-observation-identity-schema.md)
- [ ] **3.2** — [Validation contract, clear errors và failure-path tests](../lessons/part-01/chapter-03/3.2-validation-clear-errors-failure-tests.md)
- [ ] **3.3** — [Normalization, provenance và source boundary nhỏ nhất](../lessons/part-01/chapter-03/3.3-normalization-provenance-source-boundary.md)

V2 projection: `3.1–3.3` là active on-demand knowledge cho M03, không phải prerequisite của M01/M02.

### Chương 4 — History và change observation

- [ ] **4.1** — [Append-only JSONL và immutable snapshots](../lessons/part-01/chapter-04/4.1-append-only-jsonl-immutable-snapshots.md)
- [ ] **4.2** — [Delta, timestamp, freshness và historical query](../lessons/part-01/chapter-04/4.2-delta-timestamp-freshness-historical-query.md)
- [ ] **4.3** — [Second observation cycle, restart và change report](../lessons/part-01/chapter-04/4.3-second-observation-restart-change-report.md)

V2 projection: `4.1–4.3` là active on-demand knowledge cho M03 Trustworthy History & Measurement.

### Chương 5 — Grounded AI advisory reference

- [ ] **5.1** — [Chọn quy tắc tất định hay AI theo giá trị quyết định](../lessons/part-01/chapter-05/5.1-deterministic-rule-hay-ai-theo-decision-value.md)
- [ ] **5.2** — [Trích xuất có cấu trúc với tham chiếu bằng chứng và độ bất định](../lessons/part-01/chapter-05/5.2-structured-extraction-evidence-refs-uncertainty.md)
- [ ] **5.3** — [Đánh giá case, từ chối output sai, fallback, chi phí và riêng tư](../lessons/part-01/chapter-05/5.3-eval-rejection-fallback-cost-privacy.md)

V2 projection: `5.1–5.3` là detailed reference cho M04. Active M04 sequence nằm ở `8.1–8.3` để tránh nhầm v1 Mission numbering với v2.

## M01 active knowledge pull

- `7.2` observation window, zero, missing, pending, not-yet-observable.
- `7.3` provenance/reconciliation khi source/scope/config ambiguity xuất hiện.

M01 không cần database, history engine, AI hay n8n để PASS.

## M02 active knowledge pull

- `0.2` evidence/claim distinction.
- `2.1` human baseline trước Bot.
- `2.2` naive score/Expected Value limitation.
- `2.3` explainable decision, uncertainty và abstain.

`0.1` là reference cho learner dùng Go builder profile, không phải coding quota.

## Part PASS theo v2

- M01 cần E3 outcome snapshot thật hoặc blocker trung thực; zero/inconclusive hợp lệ.
- M02 cần deterministic baseline audit được; implementation có thể visual/no-code hoặc Go reference theo ADR-004.
- M01 + M02 là dependency cho M03; hoàn thành C3–C5 trước không thay Mission evidence gate.

[← Part trước](part-00.md) · [Roadmap tổng](../ROADMAP.md) · [Part tiếp theo →](part-02.md)
