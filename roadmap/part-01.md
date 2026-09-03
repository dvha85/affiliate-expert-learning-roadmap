# Phần 1 — Outcome và deterministic baseline

Trong curriculum v2, Part 01 hỗ trợ **M01 — First Outcome Snapshot** và **M02 — Smallest Deterministic Bot**. Lịch sử/AI từ v1 không còn là Mission numbering của phần này.

## Quy tắc projection

Canonical v2 lesson mapping nằm tại [`lessons/V2-LESSON-MAP.json`](../lessons/V2-LESSON-MAP.json). Front matter cũ của `3.x–5.x` là historical v1 metadata, không phải active Mission order.

## M01 — First Outcome Snapshot

Pull knowledge nhỏ nhất khi cần:

- `7.2` — observation window, zero, missing, pending, not-yet-observable.
- `7.3` — provenance/reconciliation khi snapshot có source/scope/config ambiguity.

M01 không cần database, history engine, AI hoặc n8n để PASS. Manual/read-only snapshot đúng provenance tốt hơn automation chưa justified.

## M02 — Smallest Deterministic Bot

Active on-demand knowledge:

- `0.2` — evidence/claim distinction.
- `2.1` — human baseline trước Bot.
- `2.2` — naive score/Expected Value limitation.
- `2.3` — explainable decision, uncertainty và abstain.

`0.1` là reference cho learner dùng Go builder profile, không phải coding quota và không phải prerequisite của v2.

## Knowledge lineage C3–C5

Các lesson v1 vẫn có giá trị và được giữ nguyên:

- `3.1–3.3` identity/schema/validation/provenance → v2 M03 on-demand.
- `4.1–4.3` append-only history/delta/freshness/restart → v2 M03 on-demand.
- `5.1–5.3` deterministic-vs-AI/grounding/eval → detailed reference cho v2 M04.

Không cần học hết lineage này trước M01/M02. Mission pull knowledge theo blocker thực tế.

## PASS boundary

- M01 cần E3 outcome snapshot thật hoặc blocker trung thực; zero/inconclusive hợp lệ.
- M02 cần deterministic baseline audit được; implementation có thể visual/no-code hoặc Go reference theo ADR-004.
- M01 và M02 có thể chạy song song sau M00; M03 cần cả hai.

[← Part trước](part-00.md) · [Roadmap tổng](../ROADMAP.md) · [Part tiếp theo →](part-02.md)
