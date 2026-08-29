# Affiliate Bot — learner workspace

Đây là Bot người học tự phát triển qua M00–M11. Reference ở `lab/affiliate-bot/` chỉ dùng sau attempt hoặc khi review.

## Preflight trước M00

Từ repo root, chạy:

~~~bash
git --version
go version
git rev-parse --show-toplevel
test -f lab/learner/affiliate-bot/go.mod
~~~

Nếu một lệnh fail vì thiếu Go, sai repo hoặc sai path, sửa environment trước. Đây là workstation preflight, **không phải kiến thức Affiliate và không phải PASS gate**.

Nếu public evidence chưa truy cập được, ghi `BLOCKED_EXTERNAL`/pending. Bạn vẫn có thể dùng sample để luyện engineering nhưng không được đổi sample thành real evidence.

## Starting state của M00

Scaffold đã chạy được để người mới không phải viết parser/ranking/evidence gate từ trang trắng:

~~~bash
cd lab/learner/affiliate-bot
go env GOMOD
go run ./cmd/bot
go test ./...
~~~

Nó đọc ba observations **synthetic** từ `data/m00-observations.json`, giữ `null` khác `0`, không trộn currency, chạy baseline `price × commission_rate` và trả `RANK_SCENARIO`.

Scaffold cố ý chưa đủ:

- chưa có public market evidence;
- mới có evidence eligibility guard tối thiểu, chưa có ingest validation/history đầy đủ;
- chưa lưu human ranking;
- chưa có history, AI hoặc external authority.

Đây là gap để M00 thực hành:

~~~text
RUN SYNTHETIC BASELINE
→ observe what it cannot claim
→ record 5 public observations
→ freeze human ranking
→ add one tested explanation/output improvement
→ test missing/conflicting input
→ save human-vs-Bot comparison
~~~

Không đổi `evidence_kind` thành `real` nếu record vẫn là sample. Tạo/copy input mới từ observation công khai và lưu `source_url` + `observed_at` + `access_method: public_manual`.

Bạn có thể chạy một file khác:

~~~bash
go run ./cmd/bot path/to/your-observations.json
~~~

Ba input có sẵn để quan sát state trước khi sửa code:

~~~bash
go run ./cmd/bot
go run ./cmd/bot data/m00-missing-input.json
go run ./cmd/bot data/m00-conflicting-input.json
~~~

## File map cho absolute beginner

Trong M00, ưu tiên tập trung vào bề mặt nhỏ này:

~~~text
cmd/bot/main.go                 # đọc flow/output hiện tại; chỉnh khi Mission yêu cầu
data/*.json                     # sample + public observations của bạn
cmd/bot/main_test.go            # nếu có/được Mission trỏ tới
README.md + HINTS-M00.md        # hướng dẫn và hint
~~~

Bạn **không cần hiểu toàn bộ repo** trước khi bắt đầu. Nếu thấy các package/file liên quan history, AI, database, tools, approval, deployment hoặc các capability của Mission sau, có thể bỏ qua cho đến khi Mission yêu cầu. Không refactor trước chỉ vì thấy code chưa “đẹp”.

Nguyên tắc:

> Chỉ mở file tiếp theo khi một failure, checkpoint hoặc lesson chỉ rõ lý do cần mở.

Nếu bị chặn, mở từng mức trong [Hint ladder M00](HINTS-M00.md). Không cần tự biết refactor output hay nullable JSON trước khi bắt đầu.

## Ranh giới

M00 chỉ dùng public/manual read và local compute. Không login scraping, publish, message, spend, order hoặc thay đổi tài khoản.

## Reference

Không copy reference rồi coi là PASS. Learner evidence phải chứng minh bạn đã:

1. tự attempt;
2. quan sát gap/failure;
3. kéo knowledge đúng lúc;
4. tự thay đổi/test;
5. giải thích được giới hạn.
