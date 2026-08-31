# Phần 1 — TRUSTWORTHY DATA & GROUNDED AI

- Timeline: **Evidence-gated; recalibrate after learner pilot**.
- **Chapters:** C3–C5
- **Core:** 9 micro-lessons
- **Missions:** M01–M02
- **Outcome:** Bot giữ lịch sử/provenance đáng tin cậy và AI chỉ enrich một deterministic baseline có fallback.

## Trạng thái authoring

- **Chương 3:** learner-ready sau review M01 ingest contract.
- **Chương 4:** chưa author; chỉ pull sau khi learner tự thử overwrite/data-loss ở M01 Checkpoint 2.
- **Chương 5:** chưa author; chỉ bắt đầu sau khi toàn M01 PASS.
- M01 vẫn `draft` cho tới khi Chương 4 hoàn tất Capability + Reality + Operated của trustworthy history.

## Attempt trước knowledge pull

1. M01 Checkpoint 1: đưa data xấu/ambiguous qua ingest M00 hiện có, quan sát identity/validation gap rồi mới pull Chương 3.
2. M01 Checkpoint 2: cố ý ghi đè snapshot để quan sát data loss trước khi pull Chương 4.
3. M01 Checkpoint 3: second E1 observation + restart + change report để hoàn tất history semantics.
4. M02: chạy cùng một research case với deterministic baseline, AI hợp lệ, AI unsupported và AI unavailable.

## Core checklist

### Chương 3 — Minimal trustworthy ingest

- [ ] **3.1** — [Stable subject identity, observation identity và schema vừa đủ](../lessons/part-01/chapter-03/3.1-subject-observation-identity-schema.md)
- [ ] **3.2** — [Validation contract, clear errors và failure-path tests](../lessons/part-01/chapter-03/3.2-validation-clear-errors-failure-tests.md)
- [ ] **3.3** — [Normalization, provenance và source boundary nhỏ nhất](../lessons/part-01/chapter-03/3.3-normalization-provenance-source-boundary.md)

Chương 3 kết thúc ở:

```text
M00 E1 observation
→ stable subject identity
→ strict validation
→ canonical normalization
→ provenance-preserving observation
```

Nó **chưa** chứng minh immutable history, persistence, delta hay freshness. Các capability đó thuộc Chương 4.

### Chương 4 — History và change observation

- [ ] **4.1** — Append-only file snapshots và immutable history tối thiểu
- [ ] **4.2** — Delta, timestamp, freshness và historical query
- [ ] **4.3** — Second observation cycle, restart và change report

### Chương 5 — Grounded AI advisory

- [ ] **5.1** — Chọn deterministic rule hay AI theo decision value
- [ ] **5.2** — Structured extraction với evidence refs và uncertainty
- [ ] **5.3** — Eval case, invalid-output rejection, fallback, cost và privacy

## Part PASS

- [ ] M01–M02 đều có Capability PASS, Reality verified và Operated
- [ ] Stable subject identity không bị trộn với observation identity
- [ ] Snapshot cũ không bị overwrite và query history được
- [ ] Invalid/stale input fail rõ ràng
- [ ] Core product decision vẫn chạy khi AI unavailable
- [ ] Unsupported AI claim không trở thành scoring fact

[← Part trước](part-00.md) · [Roadmap tổng](../ROADMAP.md) · [Part tiếp theo →](part-02.md)
