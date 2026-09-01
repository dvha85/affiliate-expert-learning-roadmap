# Lộ trình học Affiliate Intelligence Bot

Chương trình dành cho người mới xây **một Affiliate Intelligence Bot (bot phân tích và hỗ trợ quyết định Affiliate) tiến hóa dần từ quyết định dựa trên bằng chứng tới tự động hóa có kiểm soát**.

## Bắt đầu trong 5 phút

Chưa cần đọc hết chương trình học. Trước khi chạy bộ khởi đầu (`starter`), hãy kiểm tra môi trường máy và chắc chắn cửa sổ lệnh (`terminal`) đang đứng trong đúng kho mã (`repo`):

~~~bash
git --version
go version
git rev-parse --show-toplevel
test -f lab/learner/affiliate-bot/go.mod
~~~

Nếu `go version` báo `command not found`, hoặc `git rev-parse` / `test -f` thất bại, **chưa chạy Bot tiếp**. Hãy sửa môi trường hoặc đường dẫn kho mã trước; đây là bước kiểm tra trước khi chạy (`preflight`), không phải bài học hay cổng đạt (`PASS gate`).

Khi bốn lệnh trên đều ổn:

~~~bash
cd lab/learner/affiliate-bot
go env GOMOD
go run ./cmd/bot
go test ./...
~~~

Bạn phải thấy `Bot version: pre-v0.1` và `Decision state: RANK_SCENARIO`. Sau đó mở [Mission M00](missions/M00-first-evidence-backed-decision.md), thực hiện Checkpoint hiện hành và chỉ kéo bài học nhỏ (`micro-lesson`) khi đã thấy một khoảng trống hoặc lỗi cụ thể. Nếu bị chặn, dùng [thang gợi ý M00](lab/learner/affiliate-bot/HINTS-M00.md) từng mức.

Nếu bạn chưa truy cập được bằng chứng sản phẩm công khai thật, ghi trạng thái chặn là `BLOCKED_EXTERNAL`/pending và tiếp tục phần kỹ thuật có thể làm bằng dữ liệu mẫu. **Không đổi dữ liệu mẫu thành “real” chỉ để vượt gate.**

Sau lần chạy đầu, dùng [chương trình chuẩn](CURRICULUM.md) để hiểu mục tiêu và ranh giới, [Build-First](BUILD-FIRST.md) để hiểu mô hình thực thi và [Progress](PROGRESS.md) để xem/lưu tiến độ người học.

~~~text
THỬ TRÊN BẰNG CHỨNG THẬT
→ CHẠY / QUAN SÁT
→ KÉO 1–3 MẢNH KIẾN THỨC
→ CẢI TIẾN / KIỂM THỬ
→ SO SÁNH NGƯỜI VỚI BOT
→ LƯU BẰNG CHỨNG
→ PHÁT HÀNH PHIÊN BẢN BOT TIẾP THEO
~~~

## Cấu trúc đang áp dụng

- **Nguồn chuẩn chính thức (`active canonical`):** [CURRICULUM.md](CURRICULUM.md).
- **Trục thực thi (`execution spine`):** 12 Mission, M00–M11.
- **Kiến thức cốt lõi (`Core`):** 7 Part · 21 Chapter · 63 micro-lesson.
- **Mốc kiểm chứng (`milestone`):** 4 gate trên cùng một Bot, không phải nhiều project rời.
- **Phần nâng cao (`Advanced`):** chỉ mở khi nút thắt thực tế yêu cầu.
- **Lịch sử/tham chiếu (`historical/reference`):** các file trong `sources/` và revision cũ không còn quyết định cấu trúc active.

Số lượng 7/21/63 là inventory hiện tại, **không phải bất biến (`invariant`) cần bảo vệ bằng mọi giá**. Chương trình được phép giảm, gộp hoặc thay đổi khi bằng chứng từ người học cho thấy cấu trúc khác tốt hơn.

## “Thông minh” và “tự động” nghĩa là gì?

Bot thông minh không đồng nghĩa “gọi LLM”. Bot phải:

- dùng bằng chứng có nguồn và thời điểm;
- phân biệt `fact` (sự thật quan sát được), `estimate` (ước lượng), `assumption` (giả định), `unknown` (chưa biết);
- có đường cơ sở tất định (`deterministic baseline`) trước AI;
- biết độ tin cậy (`confidence`), độ bất định (`uncertainty`) và biết từ chối quyết định (`abstain`);
- nối `Decision → Action → Outcome → Evaluation` (Quyết định → Hành động → Kết quả → Đánh giá);
- đề xuất cải tiến nhưng không âm thầm tự sửa hành vi đang chạy ở production (môi trường vận hành thật).

Quyền hành động (`authority`) tăng theo từng gate:

~~~text
A0 quyết định tất định
→ A1 AI tư vấn có căn cứ bằng chứng
→ A2 agent dùng công cụ chỉ-đọc
→ A3 chạy bóng/phê duyệt
→ tự động hóa giới hạn có quản trị
~~~

Xuất bản công khai, chi tiêu, đổi cài đặt tài khoản, xóa dữ liệu và giao tiếp có hậu quả luôn phải đi qua chính sách, đánh giá rủi ro và phê duyệt phù hợp.

## Thực tế xuất hiện khi nào?

- M00: quan sát sản phẩm công khai và so sánh phán đoán người với Bot.
- M01: chụp nhanh (`snapshot`) thật lần hai.
- M02: AI đọc bằng chứng công khai thật.
- M03: người học tự duyệt và xuất bản một nội dung có theo dõi (`tracking`).
- M04: phân tích (`analytics`) thật; giá trị `0` vẫn là kết quả hợp lệ.
- M05: vòng cải tiến thị trường đầu tiên.
- M06+: tự động quan sát chỉ-đọc (`read-only`), rồi mới tăng quyền hành động.

Đơn hàng/doanh thu không phải điều kiện PASS vì nằm ngoài quyền kiểm soát. Tính toàn vẹn của phép đo mới là gate.

## Không gian làm việc

~~~text
lab/learner/affiliate-bot/   # nơi người học tự xây
lab/affiliate-bot/           # bản tham chiếu để đối chiếu sau khi đã tự thử
~~~

Không sao chép bản tham chiếu rồi coi là PASS.

## Trạng thái hiện tại — không hard-code learner progress ở README

README không phải nguồn chuẩn của tiến độ người học vì trạng thái này thay đổi sau mỗi checkpoint.

- **Learner progress hiện hành:** xem [PROGRESS.md](PROGRESS.md). Đây là canonical learner-state source.
- **Mức sẵn sàng của Mission:** xem [missions/README.md](missions/README.md). Đây là canonical authoring-state source.
- **Kiến trúc runtime hiện hành:** xem [ADR-003](docs/ADR-003-HYBRID-GO-N8N-AGENT-RUNTIME.md).

Việc biên soạn dần là có chủ đích: pilot Mission hiện hành trước, dùng blocker/thời gian/bằng chứng thực tế để gộp, bỏ hoặc sửa các bài sau. Authoring status và learner progress là hai trục độc lập.

## Kiểm tra repository

~~~bash
python scripts/validate_curriculum.py
python scripts/validate_authority.py
python scripts/validate_hardening.py
python scripts/validate_build_first.py
python scripts/validate_agentic_architecture.py
python scripts/validate_hybrid_runtime.py
python -m unittest discover -s tests -v
~~~

Các bước kiểm tra Go cho cả không gian người học và bản tham chiếu vẫn là điều kiện merge.

## Quy ước ngôn ngữ

Tiếng Việt là ngôn ngữ chính của toàn bộ nội dung dành cho người học. Thuật ngữ tiếng Anh chuyên ngành được giữ khi cần độ chính xác, nhưng phải có diễn giải tiếng Việt ở lần xuất hiện quan trọng. Quy tắc chi tiết nằm tại [Quy ước ngôn ngữ](docs/VIETNAMESE-LANGUAGE-STYLE.md).
