# M00 — Bằng chứng học tập

## Trạng thái hiện tại

Checkpoint 1 đã hoàn thành vòng kỹ thuật đầu tiên:

```text
chạy baseline
→ thêm requirement vào test
→ quan sát test FAIL
→ sửa Bot
→ test PASS
→ chạy toàn bộ test
→ kiểm tra diff
```

Mission M00 chưa PASS vì chưa có:
- 5 quan sát công khai thật;
- human ranking;
- các checkpoint tiếp theo.

## Learner change đầu tiên

Source code đã sửa:

- `lab/learner/affiliate-bot/cmd/bot/main.go`
- `lab/learner/affiliate-bot/cmd/bot/main_test.go`

Behavior mới:

```text
Giới hạn đường cơ sở (Baseline limitation):
chưa xét khả năng chuyển đổi (Conversion potential),
mức phù hợp với nhóm mục tiêu (Audience fit)
và rủi ro hoàn/hủy (Refund risk).
```

## Kết luận hiện tại

Bot đang dùng dữ liệu `synthetic` và công thức:

```text
price × commission_rate
```

Vì vậy:

```text
Synthetic Product B đứng #1 theo baseline hiện tại
```

không đồng nghĩa với:

```text
Synthetic Product B là sản phẩm Affiliate tốt nhất.
```

Đây mới là software/test evidence, chưa phải market evidence.
