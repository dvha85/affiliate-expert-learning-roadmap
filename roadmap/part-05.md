# Phần 5 — TOOL AGENT & GOVERNED AUTOMATION

- Timeline: **Evidence-gated; authority increases only after safety cases pass**.
- **Chapters:** C15–C17
- **Core:** 9 micro-lessons
- **Missions:** M08–M10
- **Outcome:** Agent dùng tool read-only để lấy missing evidence; action có hậu quả phải qua policy, durable approval và revalidation.

## Attempt trước knowledge pull

1. M08: để agent xử lý một case thiếu evidence nhưng chỉ cung cấp explicit read-only tools.
2. M09: tạo shadow ActionIntent + durable approval; thử duplicate/expired approval, changed context và process restart.
3. M10: chạy limited RISK0/RISK1 canary; RISK2 vẫn phải qua durable approval và revalidation.

## Core checklist

### Chương 15 — Explicit tool contracts

- [ ] **15.1** — Tool input/output schema, validation, permission và risk ceiling
- [ ] **15.2** — Read-only evidence escalation và Tool Registry
- [ ] **15.3** — Tool failure, timeout, retry, idempotency và audit

### Chương 16 — Policy, risk và approval

- [ ] **16.1** — ActionIntent và deterministic RISK0/RISK1/RISK2 policy
- [ ] **16.2** — Durable approval, expiry, reject reason và context revalidation
- [ ] **16.3** — Least privilege, secrets, prompt injection boundary và kill switch

### Chương 17 — Durable action workflow

- [ ] **17.1** — Persisted state, checkpoint, restart và resume/terminate
- [ ] **17.2** — Dry-run, controlled executor và duplicate-side-effect prevention
- [ ] **17.3** — Trace decision, tool, policy, approval, action và result

## Part PASS

- [ ] M08–M10 đều có Capability PASS, Reality verified và Operated
- [ ] Agent không thể gọi tool ngoài registry/permission
- [ ] RISK2 không execute nếu thiếu valid approval và revalidation
- [ ] Restart/duplicate approval không tạo side effect trùng
- [ ] Kill switch chặn execution kể cả khi approval đã tồn tại

[← Part trước](part-04.md) · [Roadmap tổng](../ROADMAP.md) · [Part tiếp theo →](part-06.md)
