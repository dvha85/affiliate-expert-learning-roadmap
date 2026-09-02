# Curriculum migration — v1 sang Reality-First v2

## Baseline và phạm vi

Tag local `curriculum-v1-pre-reality-first` trỏ tới commit
`e398e9a763cb181d7d087a77eb38363258ca1b6e`. Không xóa lesson, Mission hoặc
evidence v1 trong đợt migration này.

V2 là canonical sequence kể từ ADR-005. Các file Mission hiện tại khai báo
`curriculum_version: 1`; chúng là baseline/reference cho tới khi Mission v2
tương ứng được authored và delivered.

## Mapping Mission

| V1 | V2 | Ghi chú migration |
|---|---|---|
| M03 — First Tracked Manual Publish | M00 — First Safe Market Loop | Market action được đưa lên đầu; human-only và tracking/disclosure giữ nguyên. |
| M04 — Outcome analytics | M01 — First Outcome Snapshot | Chỉ chụp outcome/measurement nhỏ nhất trước history dài hạn. |
| M00 — First Evidence-Backed Decision | M02 — Smallest Deterministic Bot | Giữ lesson/Go starter như knowledge/reference, không bắt đầu v2 bằng code. |
| M01 — Trustworthy History | M03 — Trustworthy History & Measurement | History xuất hiện sau snapshot + baseline. |
| M02 — Grounded AI Advisor | M04 — Grounded AI Advisor | A1 advisory được lùi sau history/measurement. |
| M05–M11 | M05–M11 | Giữ intent, kiểm lại dependencies và authority khi author. |

## Quy tắc learner state

- Không đổi `PROGRESS.md` v1 thành progress v2 tự động.
- Credit lesson đã hoàn thành giữ nguyên là knowledge credit, không tự tạo
  Mission PASS ở v2. Ví dụ `0.1` có thể hỗ trợ M02 nhưng không thay E2 của M00.
- Evidence v1 có thể được reuse khi provenance, freshness và scope phù hợp;
  phải link lại trong evidence record v2, không copy rồi đổi nhãn `real`.
- Người đang ở v1 có thể finish v1 theo snapshot/tag hoặc chuyển có chủ đích
  bằng retrospective: state, evidence, blockers, authority và next measurement.

## Quy tắc link/file

Tên lesson ID giữ làm knowledge identifier; không hàm ý thứ tự v2. Khi có file
Mission v2, dùng title/path mới (ví dụ `M00-first-safe-market-loop.md`) và
front matter `curriculum_version: 2`. File v1 giữ filename cũ để link/history
không vỡ. `missions/README.md` là projection rõ hai thế hệ.

## Promotion checklist

Một Mission v2 chỉ đổi từ `planned`/`draft` sang `ready` khi:

1. có starter path cho beginner hoặc lý do explicit rằng Mission là manual-only;
2. có eval pack/fixture và verification commands tái lập được;
3. checkpoint attempt-first, safety/authority ceiling và evidence contract rõ;
4. personal execution đã ghi actual time, blocker và outcome hoặc
   `BLOCKED_EXTERNAL` trung thực; và
5. `python scripts/validate_readiness.py --strict` cùng validator/test liên quan qua.
