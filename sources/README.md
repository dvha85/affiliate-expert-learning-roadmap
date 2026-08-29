# Tài liệu nguồn

Thư mục `sources/` là **kho lưu lịch sử/nghiên cứu (`historical/research archive`)**, không phải nguồn chuẩn đang vận hành của chương trình.

## Nguồn chuẩn đang áp dụng

Thứ tự tài liệu đang vận hành:

1. [`../CURRICULUM.md`](../CURRICULUM.md) — chương trình chuẩn đang áp dụng (`active canonical curriculum`);
2. [`../ROADMAP.md`](../ROADMAP.md) và các file `../roadmap/part-*.md` — danh mục thực thi (`execution inventory`) của chương trình hiện tại;
3. [`../docs/SOURCE-MAPPING.md`](../docs/SOURCE-MAPPING.md) — bản đồ truy nguồn (`traceability`) từ chương trình hiện tại về tài liệu lịch sử/đào tạo/nghiên cứu.

Nếu nội dung trong `sources/` mâu thuẫn với các nguồn chuẩn ở trên, **nguồn chuẩn hiện tại được ưu tiên**. Không sửa file lịch sử chỉ để làm nó trông giống trạng thái hiện tại.

## Giáo trình lịch sử

- `SYLLABUS-v2026.08.md` — đường cơ sở lịch sử ban đầu (`historical baseline`).
- `SYLLABUS-v2026.09.md` — revision lịch sử trước đợt thiết kế lại theo outcome.
- `CURRICULUM-INDEX-v2026.09.md` — chỉ mục chuẩn hóa lịch sử của revision v2026.09.

Các file này vẫn quan trọng để truy `provenance` (nguồn gốc), rationale (lý do thiết kế) và các ý tưởng domain đã sinh ra curriculum hiện tại, nhưng **không còn là manifest đang hoạt động**.

Các con số **23 Part / 89 Chapter / 671 lesson / 14 main projects** thuộc revision lịch sử và không được dùng để mô tả chương trình hiện tại.

## Nguồn bổ sung

- `Noi-dung-dao-tao.txt` — nguồn đào tạo về nhịp học, tiến hóa project và thực hành.
- `Nghien-cuu.txt` — nguồn nghiên cứu về Affiliate Bot, Product Intelligence, feedback loop (vòng phản hồi), kiến trúc và triển khai.

Các nguồn bổ sung cung cấp evidence/rationale cho thiết kế bài học; chúng không tự động ghi đè chương trình chuẩn.

## Thứ tự ưu tiên nguồn

```text
CHƯƠNG TRÌNH CHUẨN ĐANG ÁP DỤNG:
CURRICULUM.md

DANH MỤC THỰC THI:
ROADMAP.md + roadmap/part-*.md

TRUY NGUỒN / GIẢI QUYẾT XUNG ĐỘT:
docs/SOURCE-MAPPING.md

GIÁO TRÌNH / CHỈ MỤC LỊCH SỬ:
sources/SYLLABUS-v2026.08.md
sources/SYLLABUS-v2026.09.md
sources/CURRICULUM-INDEX-v2026.09.md

NGUỒN ĐÀO TẠO / NGHIÊN CỨU BỔ SUNG:
sources/Noi-dung-dao-tao.txt
sources/Nghien-cuu.txt

LỚP DỮ KIỆN HIỆN HÀNH:
docs/FRESHNESS-POLICY.md
và các knowledge refresh docs
```

Quy tắc tra cứu:

```text
câu hỏi về lesson / mission hiện tại
→ CURRICULUM.md
→ ROADMAP + active part/mission docs
→ docs/SOURCE-MAPPING.md để truy provenance
→ nguồn lịch sử/đào tạo/nghiên cứu khi cần rationale
→ xác minh bên ngoài cho dữ kiện hiện hành
```

Một định danh lịch sử như `S:P/C/L` là vị trí truy provenance, **không mặc định là active lesson ID**.

## Quyết định kỹ thuật Go-first

Go vẫn là ngôn ngữ triển khai chính (`primary implementation language`) của Bot track hiện tại. Xem:

- [`../docs/ADR-001-GO-FIRST-BOT-STACK.md`](../docs/ADR-001-GO-FIRST-BOT-STACK.md)
- [`../CURRICULUM.md`](../CURRICULUM.md)

Các quyết định C#/.NET-first trong giáo trình lịch sử được giữ để truy lịch sử thiết kế, không phải chỉ dẫn triển khai hiện tại.

## Lớp kiến thức hiện hành

Nguồn lịch sử không bị âm thầm sửa bằng nghiên cứu web mới. Các dữ kiện có thể thay đổi theo platform, luật, privacy (quyền riêng tư), API, search, Go runtime hoặc AI/agent protocol được quản lý ở lớp current-state riêng.

Xem:

- [Freshness Policy](../docs/FRESHNESS-POLICY.md)
- [Affiliate Knowledge Refresh 2026.08](../docs/AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md)
- [Bot Engineering Refresh 2026.08](../docs/BOT-ENGINEERING-REFRESH-2026.08.md)
- [Source-to-Roadmap Traceability Map](../docs/SOURCE-MAPPING.md)

Nguyên tắc cuối cùng:

> **Lịch sử giữ nguyên là lịch sử. Nguồn chuẩn hiện tại phải duy nhất. Dữ kiện hiện hành phải kiểm chứng được.**
