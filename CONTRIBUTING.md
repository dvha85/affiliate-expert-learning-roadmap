# Đóng góp vào Affiliate Intelligence Bot Curriculum

Repo được phát triển như một curriculum có kiểm soát nhưng **không bảo vệ số lượng Part/Lesson vì chính con số**. Thay đổi execution spine, authority, safety gate hoặc learner outcome cần issue/ADR trước.

## Authority

~~~text
ACTIVE CANONICAL
= CURRICULUM.md

ACTIVE KNOWLEDGE INVENTORY
= ROADMAP.md + roadmap/part-00..06.md

DEFAULT EXECUTION
= BUILD-FIRST.md + missions/

CURRENT FACTS
= freshness policy + external source registers

HISTORICAL INPUT
= sources/ + superseded revision documents
~~~

Historical material có thể cung cấp provenance nhưng không tự thêm lesson vào Core.

## Nguyên tắc thiết kế

1. Mission-first: learner TRY trước khi đọc concept.
2. Real evidence sớm: public observation ở M00, manual publish ở M03.
3. Một Bot xuyên suốt; không tạo project rời nếu cùng capability có thể tích hợp.
4. Deterministic/human baseline trước AI.
5. Evaluation trước authority.
6. Decision khác execution.
7. Bot có thể đề xuất cải tiến nhưng không tự sửa production behavior.
8. Core chỉ chứa knowledge cần cho Mission gần nhất; Advanced/Reference không phải PASS gate.

## Lesson

Dùng [lesson template](templates/LESSON.md) và [authoring standard](docs/LESSON-AUTHORING-STANDARD.md).

Lesson ready phải:

- có mission_refs và practice_first: true;
- bắt đầu bằng Trigger/Try First, không bắt đầu bằng lecture;
- giới hạn 1–3 concept;
- áp dụng ngay vào code/data/decision;
- có failure case, evidence và explain-back rubric;
- không dùng synthetic evidence thay Reality gate.

## Mission

Mission là đơn vị progress:

~~~text
TRY → RUN → OBSERVE → PULL → IMPROVE → TEST
→ REALITY CHECK → EVIDENCE → SHIP
~~~

Mission ready không được trỏ tới Core lesson chưa được author đủ để learner dùng. Mỗi Mission phải phân biệt:

- Capability PASS;
- Reality verified;
- Operated.

Order/revenue không phải PASS gate. Measurement integrity, safety và evidence đúng loại mới là gate.

## Safety

- M00–M02 không có external execution authority.
- M03 public action do learner review và tự thực hiện.
- M06 automatic collection chỉ dùng nguồn được phép.
- M08 agent chỉ có read-only tools.
- M09 dùng shadow/draft và durable approval.
- M10 chỉ auto action RISK0/RISK1 được allowlist/cap; RISK2 vẫn approval.
- Fake engagement/order, spam, policy bypass, credential sharing và unbounded spend là prohibited, không thể được “human approve” để hợp thức hóa.

## Learner và reference workspace

~~~text
learner:   lab/learner/affiliate-bot/
reference: lab/affiliate-bot/
~~~

Reference chỉ mở sau attempt hoặc để review; copy reference không tạo PASS.

## Trước Pull Request

~~~bash
python scripts/validate_curriculum.py
python scripts/validate_hardening.py
python scripts/validate_build_first.py
python scripts/validate_agentic_architecture.py
python -m unittest discover -s tests -v
~~~

Chạy gofmt, go vet và go test cho cả learner/reference workspace. Không merge khi gate fail; không dùng CI xanh để tự cập nhật learner progress.

## Không commit

- API key, token, password;
- raw personal/sensitive export;
- evidence giả hoặc synthetic nhưng ghi là real;
- current platform/legal fact không có nguồn/ngày xác minh.

Tiếng Việt là ngôn ngữ chính; thuật ngữ English được giữ khi cần độ chính xác và giải thích ở lần xuất hiện quan trọng.
