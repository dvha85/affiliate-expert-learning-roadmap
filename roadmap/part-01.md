# Phần 1 — TRUSTWORTHY DATA & GROUNDED AI

- Timeline: **Evidence-gated; recalibrate after learner pilot**.
- **Chapters:** C3–C5
- **Core:** 9 micro-lessons
- **Missions:** M01–M02
- **Outcome:** Bot giữ lịch sử/provenance đáng tin cậy và AI chỉ enrich một deterministic baseline có fallback.

## Attempt trước knowledge pull

1. M01: nhập dữ liệu xấu và ghi đè snapshot để quan sát data loss/failure trước khi harden.
2. M02: chạy cùng một research case với deterministic baseline, AI hợp lệ, AI unsupported và AI unavailable.

## Core checklist

### Chương 3 — Minimal trustworthy ingest

- [ ] **3.1** — Product struct, JSON/file import và schema vừa đủ
- [ ] **3.2** — Validation, clear errors và failure-path tests
- [ ] **3.3** — Source adapter boundary, normalization và provenance

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
- [ ] Snapshot cũ không bị overwrite và query history được
- [ ] Invalid/stale input fail rõ ràng
- [ ] Core product decision vẫn chạy khi AI unavailable
- [ ] Unsupported AI claim không trở thành scoring fact

[← Part trước](part-00.md) · [Roadmap tổng](../ROADMAP.md) · [Part tiếp theo →](part-02.md)
