# Affiliate Bot — không gian làm việc của người học

> **V1 learner scaffold/reference.** Curriculum v2 does not require Go before
> M00. This workspace maps to v2 M02 Smallest Deterministic Bot after the
> human market loop and outcome snapshot; do not use this as a v2 M00 entrypoint.

Đây là Bot người học tự phát triển qua v1 M00–M11. Bản tham chiếu (`reference`) ở `lab/affiliate-bot/` chỉ dùng sau khi đã tự thử (`attempt`) hoặc khi review.

## Kiểm tra trước M00 (`preflight`)

Từ thư mục gốc của repo, chạy:

~~~bash
git --version
go version
git rev-parse --show-toplevel
test -f lab/learner/affiliate-bot/go.mod
~~~

Nếu một lệnh thất bại vì thiếu Go, sai repo hoặc sai đường dẫn, hãy sửa môi trường trước. Đây là bước kiểm tra máy làm việc (`workstation preflight`), **không phải kiến thức Affiliate và không phải cổng PASS**.

Nếu bằng chứng công khai thật chưa truy cập được, ghi `BLOCKED_EXTERNAL`/pending. Bạn vẫn có thể dùng dữ liệu mẫu để luyện kỹ thuật, nhưng không được đổi sample thành real evidence.

## Trạng thái khởi đầu của M00

Bộ khung (`scaffold`) đã chạy được để người mới không phải tự viết parser, ranking hay evidence gate từ trang trắng:

~~~bash
cd lab/learner/affiliate-bot
go env GOMOD
go run ./cmd/bot
go test ./...
~~~

Output mặc định dành cho người học dùng **tiếng Việt là ngôn ngữ chính**. Các token máy đọc như `RANK_SCENARIO`, `GET_MORE_DATA`, `HUMAN_REVIEW`, JSON key và code identifier vẫn giữ nguyên, nhưng có diễn giải tiếng Việt ở ngữ cảnh quan trọng.

Ví dụ starter output:

~~~text
Affiliate Bot đang khởi động...
Phiên bản Bot (Bot version): pre-v0.1
Loại bằng chứng (Evidence kind): synthetic (dữ liệu tổng hợp dùng để kiểm thử)
Số quan sát (Observations) đã nạp: 3
Phiên bản công thức (Formula version): commission-per-order/v1
Xếp hạng đường cơ sở (Baseline ranking — hiện chỉ dựa trên hoa hồng mỗi đơn):
...
Trạng thái quyết định (Decision state): RANK_SCENARIO (xếp hạng kịch bản; chưa phải khuyến nghị hành động)
Bằng chứng còn thiếu (Missing evidence): không có theo yêu cầu của baseline hiện tại
~~~

Nó đọc ba quan sát **synthetic (giả lập)** từ `data/m00-observations.json`, giữ `null` khác `0`, không trộn currency (đơn vị tiền tệ), chạy baseline `price × commission_rate` và trả `RANK_SCENARIO`.

Bộ khung cố ý chưa đầy đủ:

- chưa có bằng chứng thị trường công khai thật;
- mới có guard tối thiểu kiểm điều kiện bằng chứng, chưa có ingest validation/history đầy đủ;
- chưa lưu xếp hạng của người (`human ranking`);
- chưa có history, AI hoặc quyền hành động bên ngoài.

Đây là khoảng trống để M00 thực hành:

~~~text
CHẠY BASELINE GIẢ LẬP
→ quan sát Bot chưa được phép kết luận điều gì
→ ghi 5 quan sát công khai thật
→ chốt human ranking trước khi xem Bot
→ thêm một cải tiến output/explanation có test
→ kiểm thử input thiếu/xung đột
→ lưu so sánh người với Bot
~~~

Không đổi `evidence_kind` thành `real` nếu record vẫn là sample. Tạo/copy input mới từ quan sát công khai và lưu `source_url` + `observed_at` + `access_method: public_manual`.

Bạn có thể chạy một file khác:

~~~bash
go run ./cmd/bot path/to/your-observations.json
~~~

Ba input có sẵn để quan sát state (trạng thái) trước khi sửa code:

~~~bash
go run ./cmd/bot
go run ./cmd/bot data/m00-missing-input.json
go run ./cmd/bot data/m00-conflicting-input.json
~~~

## Bản đồ file cho người mới hoàn toàn

Trong M00, ưu tiên tập trung vào phạm vi nhỏ này:

~~~text
cmd/bot/main.go                 # đọc luồng/output hiện tại; chỉnh khi Mission yêu cầu
data/*.json                     # dữ liệu mẫu + quan sát công khai của bạn
cmd/bot/main_test.go            # test bảo vệ output/behavior của CLI
README.md + HINTS-M00.md        # hướng dẫn và gợi ý
~~~

Bạn **không cần hiểu toàn bộ repo** trước khi bắt đầu. Nếu thấy package/file liên quan history, AI, database, tools, approval, deployment hoặc capability của Mission sau, có thể bỏ qua cho đến khi Mission yêu cầu. Không refactor (tái cấu trúc code) trước chỉ vì thấy code chưa “đẹp”.

Nguyên tắc:

> Chỉ mở file tiếp theo khi một failure (lỗi), checkpoint (điểm kiểm tra) hoặc lesson chỉ rõ lý do cần mở.

Nếu bị chặn, mở từng mức trong [thang gợi ý M00](HINTS-M00.md). Không cần tự biết cách refactor output hay nullable JSON trước khi bắt đầu.

## Ranh giới

M00 chỉ dùng đọc công khai/thủ công (`public/manual read`) và tính toán cục bộ (`local compute`). Không login scraping, publish, message, spend, order hoặc thay đổi tài khoản.

## Bản tham chiếu

Không copy bản tham chiếu rồi coi là PASS. Bằng chứng học tập phải cho thấy bạn đã:

1. tự thử (`attempt`);
2. quan sát gap/failure;
3. kéo đúng kiến thức khi cần;
4. tự thay đổi và kiểm thử;
5. giải thích được giới hạn.
