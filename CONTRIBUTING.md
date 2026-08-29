# Đóng góp vào chương trình Affiliate Intelligence Bot

Repo được phát triển như một curriculum (chương trình học) có kiểm soát nhưng **không bảo vệ số lượng Part/Lesson chỉ vì chính con số đó**. Thay đổi execution spine (trục thực thi), authority (quyền hành động), safety gate (cổng an toàn) hoặc learner outcome (đầu ra người học) cần issue/ADR trước.

## Thứ tự authority (nguồn có quyền ưu tiên)

~~~text
ACTIVE CANONICAL — NGUỒN CHUẨN ĐANG ÁP DỤNG
= CURRICULUM.md

ACTIVE KNOWLEDGE INVENTORY — DANH MỤC KIẾN THỨC ĐANG ÁP DỤNG
= ROADMAP.md + roadmap/part-00..06.md

DEFAULT EXECUTION — CÁCH THỰC THI MẶC ĐỊNH
= BUILD-FIRST.md + missions/

CURRENT FACTS — DỮ KIỆN HIỆN HÀNH
= freshness policy + external source registers

HISTORICAL INPUT — NGUỒN LỊCH SỬ
= sources/ + superseded revision documents
~~~

Tài liệu lịch sử có thể cung cấp provenance (nguồn gốc) nhưng không tự thêm lesson vào Core.

## Nguyên tắc thiết kế

1. Mission-first: người học TRY trước khi đọc concept.
2. Real evidence sớm: public observation ở M00, manual publish ở M03.
3. Một Bot xuyên suốt; không tạo project rời nếu cùng capability có thể tích hợp.
4. Deterministic/human baseline trước AI.
5. Evaluation trước authority.
6. Decision khác execution.
7. Bot có thể đề xuất cải tiến nhưng không tự sửa production behavior.
8. Core chỉ chứa knowledge cần cho Mission gần nhất; Advanced/Reference không phải PASS gate.

## Quy ước ngôn ngữ

**Tiếng Việt là ngôn ngữ chính của toàn bộ nội dung dành cho người học.** Thuật ngữ tiếng Anh chuyên ngành được giữ khi cần độ chính xác, khả năng tra cứu hoặc phải khớp code/schema, nhưng phải có giải thích tiếng Việt ở lần xuất hiện quan trọng.

Chuẩn chi tiết: [`docs/VIETNAMESE-LANGUAGE-STYLE.md`](docs/VIETNAMESE-LANGUAGE-STYLE.md).

Khi review tài liệu, phải kiểm:

- heading, câu giải thích và cột bảng ưu tiên tiếng Việt;
- thuật ngữ mới có giải thích tiếng Việt gần lần xuất hiện đầu;
- không dịch tên file, command, code identifier, schema key, enum/state một cách tùy tiện;
- không dùng tiếng Anh để thay cho một câu tiếng Việt đơn giản chỉ vì thuật ngữ nghe “kỹ thuật” hơn;
- historical source được giữ nguyên khi cần bảo toàn provenance.

## Lesson

Dùng [lesson template](templates/LESSON.md) và [authoring standard](docs/LESSON-AUTHORING-STANDARD.md).

Lesson ở trạng thái `ready` phải:

- có `mission_refs` và `practice_first: true`;
- bắt đầu bằng Trigger/Try First (tình huống kích hoạt/thử trước), không bắt đầu bằng lecture;
- giới hạn 1–3 concept;
- áp dụng ngay vào code/data/decision;
- có failure case, evidence và explain-back rubric;
- không dùng synthetic evidence thay Reality gate;
- tuân thủ quy ước tiếng Việt của repo.

## Mission

Mission là đơn vị tiến độ:

~~~text
TRY → RUN → OBSERVE → PULL → IMPROVE → TEST
→ REALITY CHECK → EVIDENCE → SHIP
~~~

Mission `ready` không được trỏ tới Core lesson chưa được author đủ để learner dùng. Mỗi Mission phải phân biệt:

- Capability PASS;
- Reality verified;
- Operated.

Order/revenue không phải PASS gate. Tính toàn vẹn của phép đo, safety và evidence đúng loại mới là gate.

## Safety (an toàn)

- M00–M02 không có quyền external execution.
- M03 public action do learner review và tự thực hiện.
- M06 automatic collection chỉ dùng nguồn được phép.
- M08 agent chỉ có read-only tools.
- M09 dùng shadow/draft và durable approval.
- M10 chỉ auto action RISK0/RISK1 được allowlist/cap; RISK2 vẫn approval.
- Fake engagement/order, spam, policy bypass, credential sharing và unbounded spend là prohibited, không thể được “human approve” để hợp thức hóa.

## Không gian người học và bản tham chiếu

~~~text
learner:   lab/learner/affiliate-bot/
reference: lab/affiliate-bot/
~~~

Reference chỉ mở sau attempt hoặc để review; copy reference không tạo PASS.

## Trước Pull Request

~~~bash
python scripts/validate_curriculum.py
python scripts/validate_authority.py
python scripts/validate_hardening.py
python scripts/validate_build_first.py
python scripts/validate_agentic_architecture.py
python -m unittest discover -s tests -v
~~~

Chạy `gofmt`, `go vet` và `go test` cho cả learner/reference workspace. Không merge khi gate fail; không dùng CI xanh để tự cập nhật learner progress.

Ngoài CI, reviewer phải thực hiện **language review (rà soát ngôn ngữ)** theo [`docs/VIETNAMESE-LANGUAGE-STYLE.md`](docs/VIETNAMESE-LANGUAGE-STYLE.md). Đây là review về prose và thuật ngữ, không được tự động dịch code/schema/token.

## Không commit

- API key, token, password;
- raw personal/sensitive export;
- evidence giả hoặc synthetic nhưng ghi là real;
- current platform/legal fact không có nguồn/ngày xác minh;
- learner-facing prose mới vi phạm quy ước ngôn ngữ tiếng Việt.
