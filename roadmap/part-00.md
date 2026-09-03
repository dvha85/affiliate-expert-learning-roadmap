# Phần 0 — Reality trước, code sau

Phần 0 của curriculum v2 phục vụ **M00 — First Safe Market Loop**. Learner mới không bắt đầu bằng Go hay Bot; bắt đầu bằng một context Affiliate thật, human-owned và an toàn.

## Quy tắc đọc lesson

Lesson ID là **knowledge inventory**, không phải reading order. Front matter cũ trong các lesson `0.x–5.x` được giữ để bảo toàn lịch sử v1; projection chuẩn của v2 nằm ở [`lessons/V2-LESSON-MAP.json`](../lessons/V2-LESSON-MAP.json).

```text
TRY REAL CONTEXT
→ OBSERVE GAP
→ PULL SMALLEST KNOWLEDGE SLICE
→ APPLY
→ SAVE EVIDENCE
```

Không dùng `status: ready` hoặc `mission_refs` còn sót trong lesson v1 để suy ra Mission v2 đã ready/PASS.

## M00 active knowledge pull

- `6.1` — Audience/problem/product-fit hypothesis có thể kiểm.
- `6.2` — Proof, claim, disclosure và platform boundary hiện hành.
- `6.3` — Human review, manual publish và `Decision ≠ Approval ≠ Execution`.
- `7.1` — Tracking reference và event chain tối thiểu.

Các lesson `0.2`, `1.1`, `1.2` có thể được pull như reference nếu learner gặp evidence/affiliate-flow gap; không phải prerequisite.

## Knowledge lineage C0–C2

Các lesson sau được giữ nguyên để bảo toàn learner credit và M02 reference path:

- `0.1` Chạy, sửa và kiểm thử Bot đầu tiên — reference cho M02/Go builder profile.
- `0.2` Evidence kind và claim kind — reusable knowledge.
- `0.3` Failure evidence và explain-back — reference.
- `1.1–1.3` Observation/provenance/freshness — reusable cho M00/M02/M03 khi cần.
- `2.1–2.3` Human ranking, baseline score, uncertainty/abstain — active on-demand chủ yếu ở M02.

Hoàn thành các lesson này trước đây vẫn giữ knowledge credit; **không tạo M00 v2 PASS**.

## M00 PASS boundary

M00 chỉ PASS khi Mission contract chứng minh:

```text
E1 public observation
+ exact artifact review
+ disclosure/tracking
+ human manual execution E2
+ ActionRecord
+ next measurement
```

Bot/AI/n8n không publish. `BLOCKED_EXTERNAL` là trạng thái trung thực khi account/policy không cho action; không thay bằng synthetic evidence.

[← Roadmap tổng](../ROADMAP.md) · [Mission M00](../missions/M00-first-safe-market-loop.md) · [Part tiếp theo →](part-01.md)
