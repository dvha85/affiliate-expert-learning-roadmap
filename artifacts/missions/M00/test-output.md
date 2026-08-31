# M00 Checkpoint 1 — Test evidence

## Baseline trước khi thay đổi

Bot chạy thành công với:

```bash
go run ./cmd/bot
go test ./...
```

Starter Bot dùng:

```text
Evidence kind: synthetic
Formula version: commission-per-order/v1
Decision state: RANK_SCENARIO
```

Baseline ranking:

```text
1. Synthetic Product B | điểm (score)=9.60
2. Synthetic Product C | điểm (score)=8.10
3. Synthetic Product A | điểm (score)=6.00
```

## Requirement mới

Tôi muốn Bot nói rõ giới hạn của baseline thay vì chỉ đưa score.

Tôi thêm expectation vào `cmd/bot/main_test.go` trước:

```go
"Giới hạn đường cơ sở (Baseline limitation):",
```

Chưa sửa `main.go`.

## Intentional failure

Chạy:

```bash
go test ./cmd/bot
```

Kết quả:

```text
--- FAIL: TestRunShowsSafeStarterStateInVietnamese
output thiếu "Giới hạn đường cơ sở (Baseline limitation):"
FAIL
```

Ý nghĩa: test đã yêu cầu behavior mới nhưng implementation chưa có behavior đó.

## Implementation

Sau failure, tôi thêm vào `cmd/bot/main.go`:

```go
fmt.Fprintln(out, "Giới hạn đường cơ sở (Baseline limitation): chưa xét khả năng chuyển đổi (Conversion potential), mức phù hợp với nhóm mục tiêu (Audience fit) và rủi ro hoàn/hủy (Refund risk).")
```

## PASS sau thay đổi

```bash
go test ./cmd/bot
go test ./...
git diff --check
```

Các test đều PASS và `git diff --check` không báo lỗi.

## Điều test này chứng minh

Test PASS chứng minh Bot hiện có behavior đã được yêu cầu.

Test PASS không chứng minh ranking Affiliate là đúng ngoài thị trường.
