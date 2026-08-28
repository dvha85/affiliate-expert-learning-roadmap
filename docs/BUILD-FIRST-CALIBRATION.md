# Hiệu chỉnh Build-First

> M00–M05 là calibration cohort (nhóm hiệu chỉnh) đầu tiên. Không giảm/tăng toàn bộ workload model (mô hình khối lượng học) chỉ từ cảm giác rằng Build-First nhanh hơn hay chậm hơn.

## Vì sao cần hiệu chỉnh bằng dữ liệu

Planning baseline (mốc kế hoạch) hiện tại của v2026.09 xấp xỉ:

```text
lesson/evidence midpoint      ≈ 489h
incremental integration       ≈ 30–31h
total planning envelope       ≈ 520h
```

Build-First có thể giảm double work (làm trùng) vì cùng một code có thể đồng thời là Mission evidence, Lesson practice evidence và đóng góp cho Project về sau. Nhưng Build-First cũng có thể tăng thời gian debug/vận hành thật.

Chỉ **actual learner data (dữ liệu thời gian thực tế của người học)** mới được dùng để quyết định net effect (tác động ròng).

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
| `result` | PASS / RETRY / BLOCKED / IN_PROGRESS |

Tổng actual time:

```text
build + debug + operate + knowledge + retry
```

Không double-count (tính hai lần) cùng một khoảng thời gian vào nhiều bucket.

## Quy tắc reforecast (dự báo lại)

Sau M00–M05:

1. tính median (trung vị) tỷ lệ actual/planned;
2. xác định overrun (vượt kế hoạch) đến từ learning, engineering setup, debugging hay operation;
3. so sánh evidence được reuse giữa Mission/Lesson/Project với phần duplicate work đã tránh được;
4. chỉ re-estimate phần scope còn lại có tính chất tương tự;
5. giữ nguyên PASS criteria và kéo dài timeline nếu evidence yêu cầu.

## Quyết định timeline

Standard vẫn khoảng 9h/tuần và Accelerated vẫn khoảng 11–12h/tuần cho tới khi dữ liệu thực tế đủ để thay đổi giả định.

```text
DATA > OPINION
(Dữ liệu > Ý kiến)
```

Calendar date (mốc lịch) chỉ là forecast; evidence mới là gate.