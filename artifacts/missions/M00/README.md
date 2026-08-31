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

Bài 0.1 — **Chạy, sửa và kiểm thử Bot đầu tiên**: ✅ PASS ngày 2026-08-31.

PASS được chốt sau khi người học tự explain-back đúng các ý cốt lõi:

- `go run ./cmd/bot` chạy Bot, còn `go test ./...` chạy các test để kiểm tra behavior đã định nghĩa;
- intentional FAIL chứng minh test mới thực sự phát hiện được behavior đang thiếu;
- Product B đứng #1 chỉ chứng minh vị trí theo baseline hiện tại, chưa chứng minh đó là sản phẩm Affiliate tốt nhất;
- `RANK_SCENARIO` được giữ nguyên vì là state token mà code/test có thể phụ thuộc vào, còn phần giải thích cho người học dùng tiếng Việt.

Mission M00 chưa PASS vì chưa có:
- 5 quan sát công khai thật;
- human ranking;
- Bot-vs-human comparison;
- abstention/reality evidence;
- các checkpoint tiếp theo.

## Learner change đầu tiên

Source code đã sửa:

- `lab/learner/affiliate-bot/cmd/bot/main.go`
- `lab/learner/affiliate-bot/cmd/bot/main_test.go`

Learner commit:

```text
a3f787a M00: expose baseline limitation in learner bot
```

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

## Bước tiếp theo

Tiếp tục knowledge pull của M00 Checkpoint 1 với Bài 0.2, sau đó Bài 0.3 trước khi chuyển sang Checkpoint 2.
