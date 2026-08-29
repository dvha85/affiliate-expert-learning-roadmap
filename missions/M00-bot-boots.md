---
mission_id: "M00"
title: "Khởi động Affiliate Bot"
status: ready
requires_missions: []
bot_version_from: null
bot_version_to: "v0.0"
estimated_hours: 2
knowledge:
  required: ["0.1", "0.2"]
  on_demand: []
  reference: []
projects:
  contributes_to: []
risk_scope:
  external_side_effects: false
---

# Mission M00 — Khởi động Affiliate Bot

## Ship Target — Mục tiêu bàn giao

Chạy được learner Affiliate Bot bằng Go, hiểu Bot hiện **chỉ khởi động**, thực hiện ít nhất một thay đổi nhỏ do chính bạn làm và lưu evidence (bằng chứng) đầu tiên.

Expected capability (năng lực mong đợi) sau M00:

```text
start
→ print Bot version
→ print Bot status
→ exit cleanly
```

M00 **chưa** có Product, JSON ingest, database, ranking, AI hay external side effect.

## Starting Bot State — Trạng thái Bot ban đầu

Learner workspace:

```text
lab/learner/affiliate-bot/
```

Repo cung cấp scaffold (khung tối giản) có thể compile/run để bạn không mất buổi đầu vào boilerplate. Trạng thái learner vẫn là `pre-v0.0` cho tới khi bạn chạy, sửa, test, giải thích và lưu evidence.

Reference implementation (bản triển khai tham chiếu) nằm ở `lab/affiliate-bot/` và **không phải starting state** của M00.

## Environment Preflight — Kiểm tra môi trường trước khi build

M00 dùng Go ngay từ vòng học đầu tiên, vì vậy **không giả định máy đã có sẵn toolchain**. Trước khi `cd` vào learner workspace hoặc chạy Bot, hãy kiểm tra môi trường từ terminal hiện tại:

```bash
pwd
git --version
go version
```

Sau đó xác nhận bạn đang có repository và learner workspace đúng:

```bash
# chạy từ repo root sau khi đã clone/mở đúng repository
pwd
test -f go.mod || true
test -d lab/learner/affiliate-bot
ls lab/learner/affiliate-bot
```

> Repo root không bắt buộc phải có `go.mod`; learner Go module nằm trong `lab/learner/affiliate-bot/`. Mục tiêu của preflight là **xác nhận vị trí**, không đoán path trên máy người học.

Tiếp tục kiểm tra module thật:

```bash
cd lab/learner/affiliate-bot
pwd
test -f go.mod
go env GOMOD
go test ./...
```

### Nếu `git` không tồn tại

Dừng M00 tại đây và cài/enable Git bằng cách phù hợp với hệ điều hành. Không tiếp tục bằng cách copy source rời rạc vì learner evidence cần gắn với repository/commit.

### Nếu `go: command not found`

Dừng trước bước Build First và cài **Go stable release** từ nguồn chính thức phù hợp với hệ điều hành/kiến trúc máy. Sau khi cài, mở terminal mới nếu cần rồi xác nhận lại:

```bash
go version
go env GOMOD
```

Không hard-code một Go patch version vào Mission vì runtime version là current fact và được quản lý bởi freshness layer của curriculum.

### Nếu `cd lab/learner/affiliate-bot` thất bại

Không tạo ngẫu nhiên directory mới. Quay lại xác định repo root:

```bash
pwd
git rev-parse --show-toplevel
```

Sau đó `cd` tới path repo root mà Git trả về và kiểm tra lại `lab/learner/affiliate-bot/`.

### Preflight readiness

Chỉ chuyển sang Build First khi:

- `git --version` chạy được;
- `go version` chạy được;
- `git rev-parse --show-toplevel` xác định được repository;
- `lab/learner/affiliate-bot/go.mod` tồn tại;
- `go env GOMOD` trỏ tới learner module;
- baseline `go test ./...` chạy được hoặc ít nhất trả một failure thuộc code/test của repo mà bạn có thể quan sát, không phải lỗi thiếu tool/path.

Preflight là **readiness gate của execution**, không phải một Lesson/Mission mới và không tự tạo learner PASS.

## Build First — Xây trước

1. Mở `lab/learner/affiliate-bot/cmd/bot/main.go`.
2. Đọc vừa đủ để nhận ra `package`, `func` và chuỗi output.
3. Chạy Bot trước khi học sâu Go.
4. Tự thêm một dòng output có ý nghĩa, ví dụ `Learner mission: M00`, rồi cập nhật test tương ứng.

Không mở reference v0.3 trước khi đã có attempt (lần thử) trừ khi có blocker thật.

## Run — Chạy

Từ repo root:

```bash
cd lab/learner/affiliate-bot
go run ./cmd/bot
go test ./...
```

Expected baseline output:

```text
Affiliate Bot starting...
Bot version: v0.0
Bot status: OK
```

Sau thay đổi của learner, output phải có thêm/đổi phần bạn chủ động thực hiện và test vẫn PASS.

## Observe — Quan sát

Bot hiện chưa làm Affiliate business logic. Đây là chủ ý: bạn cần thấy ranh giới giữa **một process chạy được** và **một Affiliate Bot có business capability**.

Câu hỏi quan sát:

- Bot hiện biết gì về Product? → chưa biết.
- Bot đã ra Decision (quyết định) nào? → chưa.
- Bot có external side effect (tác động bên ngoài) không? → không.
- Vậy vì sao vẫn đáng build M00? → để có executable learning loop (vòng học bằng chương trình chạy thật) từ ngày đầu.

## Knowledge Pull — Lấy kiến thức đúng lúc

### Required — Bắt buộc cho Mission

`0.1 — Affiliate Expert là gì?`

Chỉ cần slice (phần) này cho M00:

- Affiliate là một business system, không chỉ là link;
- Affiliate Expert phải hiểu vì sao một quyết định tạo giá trị;
- không automate hoạt động kinh doanh thật khi chưa hiểu logic bên dưới.

`0.2 — Affiliate Bot Engineer là gì?`

Chỉ cần slice này cho M00:

- Bot Engineer biến business logic thành software có thể chạy/đo/kiểm soát;
- deterministic logic (logic xác định) trước AI autonomy;
- Decision (quyết định) ≠ Execution (thực thi).

> **Không yêu cầu full PASS 0.1 và 0.2 trước khi chạy M00.** Full Lesson PASS được đánh giá độc lập.

### On-demand — Khi phát sinh nhu cầu

- `package`, `func`, slice và test syntax ở mức đủ đọc/sửa code hiện tại.

### Reference — Tham khảo

- Part 15 là formal Go/Bot Engineering mastery; để sau.

## Improve — Cải tiến

Thực hiện một thay đổi nhỏ nhưng có chủ ý trong learner workspace, ví dụ:

```text
Learner mission: M00
```

Sau đó sửa test để behavior mới được kiểm soát.

Mục tiêu không phải code nhiều; mục tiêu là hoàn thành một vòng:

```text
edit → run → test → observe → explain
```

## Tests — Kiểm thử

```bash
go test ./...
```

Test phải bảo vệ ít nhất Bot Version và Bot Status.

## Operate — Vận hành

Chạy Bot nhiều lần. Với cùng code, output phải deterministic (xác định, lặp lại được).

## Failure Case — Tình huống lỗi

Tạm thời đổi một expected value trong `main_test.go` để test thất bại, chạy:

```bash
go test ./...
```

Quan sát failure message, sau đó khôi phục test đúng và chạy lại tới PASS.

Failure exercise này giúp bạn chứng minh test thật sự phát hiện sai lệch, thay vì chỉ tồn tại cho đẹp.

## Evidence — Bằng chứng

Lưu dưới `artifacts/missions/M00/` hoặc link tương đương:

- preflight output đủ để chứng minh Git/Go/repo/module đã sẵn sàng;
- command đã chạy;
- output trước/sau thay đổi;
- test PASS cuối cùng;
- một failure output đã quan sát;
- code path/learner commit;
- note ngắn: Bot hiện làm gì và chưa làm gì.

## Explain-back — Giải thích lại

1. Tại sao một chương trình chỉ in status vẫn hữu ích cho M00?
2. Affiliate Bot hiện tại đã tự động hóa business decision nào chưa?
3. Vì sao M00 chưa cần AI/Agent?
4. `USE GO EARLY` khác `CLAIM GO MASTERY EARLY` như thế nào?
5. Vì sao `BUILD CODE EARLY ≠ AUTOMATE REAL BUSINESS EARLY`?
6. Vì sao phải phân biệt lỗi môi trường/toolchain với lỗi code/test của Bot?

## Mission PASS — Tiêu chí PASS

- [ ] Environment Preflight xác nhận Git/Go/repo/module đủ để thực thi M00
- [ ] learner Bot chạy được
- [ ] bạn đã tự sửa ít nhất một behavior nhỏ
- [ ] tests PASS sau thay đổi
- [ ] output kiểm tra được
- [ ] đã quan sát ít nhất một test failure và khôi phục về PASS
- [ ] hiểu knowledge slice bắt buộc của 0.1 và 0.2
- [ ] explain-back đạt
- [ ] evidence đã lưu

## Bot Version Result — Kết quả phiên bản Bot

```text
pre-v0.0 learner state → v0.0 learner Bot có thể chạy/test/giải thích
```

## Next Mission — Mission tiếp theo

M01 — Product Ingest (Đọc và kiểm tra dữ liệu sản phẩm).