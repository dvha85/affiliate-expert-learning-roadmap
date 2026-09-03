# Phần 2 — Trustworthy intelligence trước Agent

- Timeline: **Evidence-gated; M03 cần M01+M02, M04 cần M03**.
- **Chapters:** C6–C8
- **Core:** 9 micro-lessons
- **Mission focus v2:** M03 Trustworthy History & Measurement + M04 Grounded AI Advisor.

## Cách đọc Part 02 trong v2

Canonical projection nằm tại [`lessons/V2-LESSON-MAP.json`](../lessons/V2-LESSON-MAP.json). Mission có thể pull lesson ngoài Part vật lý; lesson ID là knowledge inventory, không phải reading order.

### Chương 6 — Compliant micro-experiment knowledge

- [ ] **6.1** — [Audience problem, product fit và content angle có thể kiểm](../lessons/part-02/chapter-06/6.1-audience-problem-product-fit-content-angle.md)
- [ ] **6.2** — [Proof, claims, disclosure và platform boundary hiện hành](../lessons/part-02/chapter-06/6.2-proof-claims-disclosure-platform-boundary.md)
- [ ] **6.3** — [Human review, manual publish và Decision khác Execution](../lessons/part-02/chapter-06/6.3-human-review-manual-publish-decision-execution.md)

V2 projection: `6.1–6.3` là active on-demand knowledge cho M00. `6.3` khóa invariant `Decision ≠ Approval ≠ Execution` và human-only external action.

### Chương 7 — Track real market signals

- [ ] **7.1** — [Tracking ID, link, impression, click và outcome event](../lessons/part-02/chapter-07/7.1-tracking-id-utm-link-impression-click-outcome.md)
- [ ] **7.2** — [Observation window, zero, missing và not-yet-observable](../lessons/part-02/chapter-07/7.2-observation-window-zero-missing-not-yet-observable.md)
- [ ] **7.3** — [Import analytics/export, provenance và reconciliation](../lessons/part-02/chapter-07/7.3-import-analytics-export-provenance-reconciliation.md)

V2 projection:
- `7.1` active cho M00.
- `7.2` active cho M01.
- `7.3` reusable cho M01/M03.

Manual/read-only path là baseline. n8n chỉ được thêm khi orchestration/plumbing tạo bottleneck thật; workflow success không được bypass canonical validation/reconciliation.

### Chương 8 — Grounded AI advisory

- [ ] **8.1** — [Grounded advisory contract và CALL_AI hay SKIP_AI](../lessons/part-02/chapter-08/8.1-grounded-advisory-contract-call-skip.md)
- [ ] **8.2** — [Evidence refs, claim support và uncertainty gate](../lessons/part-02/chapter-08/8.2-evidence-refs-claim-support-uncertainty.md)
- [ ] **8.3** — [Eval, reject, fallback, injection và privacy boundary](../lessons/part-02/chapter-08/8.3-eval-reject-fallback-injection-privacy.md)

Chương 8 là active M04 path:

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

Detailed v1 lessons `5.1–5.3` vẫn là reference sâu, không phải prerequisite.

## Authority ceiling

M03: deterministic/local/read-only truth handling.
M04: A1 advisory only — không tool use, write, publish, account mutation hay autonomous loop.

Invariant:

```text
structured ≠ grounded
ref exists ≠ claim supported
AI confidence ≠ evidence
AI recommendation ≠ execution permission
```

[← Part trước](part-01.md) · [Roadmap tổng](../ROADMAP.md) · [Part tiếp theo →](part-03.md)
