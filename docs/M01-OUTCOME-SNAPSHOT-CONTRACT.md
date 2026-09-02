# M01 Outcome Snapshot Contract

M01 ghi **một snapshot outcome/measurement thật nhỏ nhất** từ action M00.
Đây là read-only measurement, không phải một Bot release và không tự tạo action
mới. Mục tiêu là phân biệt trung thực điều gì đã quan sát được với điều gì còn
pending/missing.

## Trạng thái

```text
observed_value: 0 + outcome_status: zero
≠ observed_value: not_yet_observable + outcome_status: pending
≠ missing source/export
≠ outcome_status: inconclusive
```

- `zero`: source/export thật đã được đọc trong window và metric quan sát là 0;
- `pending`: outcome window chưa kết thúc hoặc platform chưa expose metric;
- `partial`: chỉ có một phần window/scope;
- `final`: window/scope đã đóng theo context đã ghi;
- `inconclusive`: có data nhưng không đủ để kết luận attribution/quality.

Không thay `pending` hoặc missing bằng `0`, và không gọi sale/revenue dương là
điều kiện PASS.

## Provenance và riêng tư

Snapshot phải nêu measurement source/reference, `observed_at`, window, metric,
scope và limitation attribution. Raw analytics/export/account data giữ local
private; chỉ redacted summary/reference mới được commit. Xem
[privacy boundary](PRIVACY-AND-LEARNER-EVIDENCE.md).

## Low-traffic protocol

Freeze `action_record_id`, `measurement_context_id`, source, metric scope và
window trước khi đọc outcome. Khi traffic không đủ, ghi `pending` hoặc
`inconclusive`, exact `next_read_at` và attribution limitation. `0` chỉ hợp lệ
khi source đã được đọc trong window, `value_state: observed`; missing hoặc
`not_yet_observable` không được convert thành zero.
