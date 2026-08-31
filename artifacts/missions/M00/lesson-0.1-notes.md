# Bài 0.1 — Ghi chú và giải thích thêm

## Trạng thái bài học

**PASS — 2026-08-31**

Bài học được chốt PASS sau khi người học tự explain-back đúng các ý cốt lõi về `go run`, `go test`, intentional FAIL, giới hạn của baseline và vai trò của state token `RANK_SCENARIO`.

## `main.go` và `main_test.go`

Cách hiểu đơn giản:

```text
main.go
= Bot thật

main_test.go
= người kiểm tra Bot
```

`main.go` định nghĩa behavior của Bot.

`main_test.go` kiểm tra Bot có thực hiện đúng behavior đó hay không.

## Vì sao viết test trước?

Vòng vừa thực hành:

```text
Requirement mới
→ viết test
→ test FAIL
→ sửa Bot
→ test PASS
```

Test FAIL có chủ ý chứng minh test thật sự phát hiện được behavior đang thiếu.

## Test PASS chứng minh gì?

```text
Test PASS
= code đang thực hiện behavior mà test yêu cầu
```

Nhưng:

```text
Test PASS
≠
quyết định Affiliate ngoài thị trường là đúng
```

Có thể nhớ:

```text
Software evidence
≠
Business evidence
```

## Baseline hiện tại

Bot hiện dùng:

```text
price × commission_rate
```

Vì vậy B đứng đầu chỉ có nghĩa:

```text
B đứng #1 theo baseline hiện tại
```

không có nghĩa:

```text
B là sản phẩm Affiliate tốt nhất
```

## Conversion potential

`Conversion potential` là khả năng người quan tâm/click thực sự mua.

Một sản phẩm có hoa hồng mỗi đơn cao nhưng rất khó chuyển đổi có thể tạo kết quả kém hơn sản phẩm có hoa hồng thấp hơn nhưng dễ chuyển đổi hơn.

## Audience fit

`Audience fit` là mức phù hợp giữa sản phẩm và nhu cầu của nhóm người mục tiêu.

Commission cao không đủ nếu sản phẩm không phù hợp với audience.

## Refund risk

`Refund risk` là rủi ro đơn bị hoàn/hủy hoặc không trở thành commission cuối cùng.

Vì vậy:

```text
Order
→ Valid Order
→ Final Commission
```

là các bước khác nhau.

## Vì sao Bot phải nói giới hạn?

Bot tốt không chỉ nói:

```text
Kết quả là gì?
```

mà còn phải giúp trả lời:

```text
Tôi dùng dữ liệu nào?
Tôi dùng công thức nào?
Tôi đang thiếu gì?
Tôi được phép kết luận tới đâu?
```

## VS Code + Go đã setup

```text
VS Code                 ✅
Go toolchain            ✅
gopls                    ✅
Autocomplete             ✅
Go to Definition / F12   ✅
Format on Save           ✅
Go Test Runner           ✅
go test ./...            ✅
```

## Các lệnh Git đã dùng

`git diff`:
- xem đã thay đổi gì.

`git diff --check`:
- kiểm lỗi whitespace cơ bản.

`git status --short`:
- xem file nào đã sửa.

Ví dụ:

```text
 M cmd/bot/main.go
 M cmd/bot/main_test.go
```

`M` = Modified.

## Explain-back của người học

### 1. `go run ./cmd/bot` và `go test ./...` khác nhau thế nào?

Người học trả lời đúng ý: `go run ./cmd/bot` dùng để chạy Bot, còn `go test ./...` dùng để chạy tất cả test case trong module.

### 2. Vì sao intentional FAIL là điều tốt?

Người học chốt đúng: test FAIL chứng minh test mới thực sự phát hiện được behavior/code đang thiếu trước khi implementation được thêm vào.

Diễn đạt chuẩn hơn:

```text
FAIL trước khi sửa implementation
= test có khả năng phát hiện behavior đang thiếu
```

### 3. Product B đứng #1 chứng minh gì?

Người học trả lời đúng: Product B đứng #1 theo công thức hiện tại, nhưng điều đó chưa chứng minh Product B là sản phẩm Affiliate tốt nhất.

### 4. Vì sao giữ nguyên `RANK_SCENARIO`?

Người học trả lời đúng: `RANK_SCENARIO` là mã mà code và test đang sử dụng nên phải giữ ổn định; phần giải thích ý nghĩa cho con người dùng tiếng Việt.

## Câu cần nhớ

```text
main.go
= behavior của Bot

main_test.go
= kiểm tra behavior đó
```

```text
Requirement
→ Test
→ FAIL
→ Fix
→ PASS
```

```text
Score
≠
Truth
```

Và:

```text
Product B đứng #1 theo baseline
≠
Product B là sản phẩm Affiliate tốt nhất
```

## Bước tiếp theo

Bài 0.2 — phân biệt sample/real evidence và fact/estimate/assumption/unknown.
