# Phần 2 — Trustworthy intelligence trước Agent

Trong curriculum v2, Part 02 phục vụ **M03 — Trustworthy History & Measurement** và **M04 — Grounded AI Advisor**. Human market publish đã được đưa lên M00; các label M03/M04 kiểu v1 không còn là active sequence.

## Canonical lesson projection

Dùng [`lessons/V2-LESSON-MAP.json`](../lessons/V2-LESSON-MAP.json). Mission có thể pull lesson ngoài Part vật lý; lesson ID là knowledge inventory, không phải reading order.

## M03 — Trustworthy History & Measurement

Active on-demand knowledge:

- `3.1–3.3` — subject/observation identity, validation, normalization, provenance.
- `4.1–4.3` — append-only history, delta/freshness, restart/change report.
- `7.3` — MeasurementContext/reconciliation khi analytics source/scope/config cần nối vào history.

Implementation semantics thuộc Deterministic Core. Không cần n8n nếu manual/read-only path đã đủ; chỉ thêm orchestration khi repeated plumbing tạo bottleneck thật.

## M04 — Grounded AI Advisor

Active v2 knowledge:

- `8.1` — advisory contract và `CALL_AI | SKIP_AI`.
- `8.2` — evidence-ref validity, claim-support và uncertainty gate.
- `8.3` — eval/reject/fallback, prompt-injection-like content và privacy boundary.

Detailed v1 lessons `5.1–5.3` vẫn là reference, không phải prerequisite.

Flow bắt buộc:

```text
E3 evidence/history
→ deterministic baseline FIRST
→ CALL_AI | SKIP_AI
→ untrusted candidate
→ schema/ref/support validation
→ GROUNDED | REJECTED | UNAVAILABLE | SKIPPED
→ deterministic fallback preserved
→ no Action
```

Invariant:

```text
structured ≠ grounded
ref exists ≠ claim supported
AI confidence ≠ evidence
AI recommendation ≠ execution permission
```

## Knowledge lineage C6–C8

- `6.1–6.3` và `7.1` hiện là active on-demand knowledge cho M00.
- `7.2` active cho M01; `7.3` reusable cho M01/M03.
- `8.1–8.3` là active M04 grounded-advisory chapter.

Việc lesson nằm trong Part 02 vật lý không ép learner học nó tại Part 02; Mission-first projection quyết định lúc pull.

## Authority ceiling

M03: deterministic/local/read-only truth handling.
M04: A1 advisory only — không tool use, write, publish, account mutation hay autonomous loop.

n8n/Agent runtime không được dùng để che một deterministic history/grounding contract chưa đúng.

[← Part trước](part-01.md) · [Roadmap tổng](../ROADMAP.md) · [Part tiếp theo →](part-03.md)
