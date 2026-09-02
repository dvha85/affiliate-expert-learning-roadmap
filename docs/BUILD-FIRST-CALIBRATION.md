# Hiệu chỉnh Build-First

> M00–M05 là personal calibration loop đầu tiên. Không giảm/tăng toàn bộ workload model (mô hình khối lượng học) chỉ từ cảm giác rằng Build-First nhanh hơn hay chậm hơn.

## Vì sao cần hiệu chỉnh bằng dữ liệu

Planning envelope chưa được kiểm chứng của Core hiện tại:

```text
focused learner time          ≈ 240–360h
external outcome waiting      = ghi riêng
confidence                    = thấp trước personal actuals
```

Build-First có thể giảm double work vì cùng một code/evidence phục vụ micro-lesson, Mission và milestone. Nhưng real observation, review, debug và operation cũng có thể làm calendar dài hơn.

Chỉ **personal actuals (dữ liệu thời gian thực tế của owner, `n=1`)** mới được dùng để quyết định net effect (tác động ròng) trong repository này.

## Dữ liệu cần ghi cho từng Mission

Với M00–M05, ghi:

| Field (trường) | Ý nghĩa |
|---|---|
| `planned_hours` | số giờ ước tính trước khi làm Mission |
| `actual_build_hours` | thời gian coding/configuration/data work |
| `actual_debug_hours` | thời gian chẩn đoán/sửa lỗi |
| `actual_operate_hours` | thời gian chạy và quan sát Bot |
| `actual_knowledge_hours` | thời gian pull required knowledge + explain-back |
| `actual_retry_hours` | thời gian làm lại/review sau evidence chưa đạt |
| `waiting_for_outcome_hours` | thời gian lịch chờ outcome; ghi riêng, không cộng vào focused time |
| `capability_result` | PASS / RETRY / BLOCKED / IN_PROGRESS |
| `reality_result` | VERIFIED / PENDING / BLOCKED / NOT_REQUIRED |
| `result` | PASS / RETRY / BLOCKED / IN_PROGRESS |

Tổng actual time:

```text
build + debug + operate + knowledge + retry
```

Không double-count (tính hai lần) cùng một khoảng thời gian vào nhiều bucket.

## Quy tắc reforecast (dự báo lại)

Sau M00–M05:

1. tính tỷ lệ actual/planned của owner và ghi rõ `n=1`;
2. xác định overrun (vượt kế hoạch) đến từ learning, engineering setup, debugging hay operation;
3. so sánh evidence được reuse giữa Mission/Lesson/Milestone với phần duplicate work đã tránh được;
4. chỉ re-estimate phần scope còn lại có tính chất tương tự;
5. giữ nguyên PASS criteria và kéo dài timeline nếu evidence yêu cầu.

## Quyết định timeline

Các profile 12/15 tháng chỉ là forecast. Không giữ một số giờ/tuần cố định nếu personal actuals cho thấy khác; không suy rộng thành median hay benchmark learner.

```text
DATA > OPINION
(Dữ liệu > Ý kiến)
```

Calendar date (mốc lịch) chỉ là forecast; evidence mới là gate.
