# Hướng dẫn đóng góp vào Affiliate Expert Learning Roadmap

Repo được phát triển như một curriculum có kiểm soát. Thay đổi cấu trúc hoặc execution model (mô hình thực thi) ưu tiên **issue-first (mở Issue trước)**.

## 1. Các lớp authority (nguồn có thẩm quyền)

```text
ACTIVE CANONICAL (BẢN CHUẨN HIỆN HÀNH)
= sources/SYLLABUS-v2026.09.md

HISTORICAL BASELINE (MỐC LỊCH SỬ)
= sources/SYLLABUS-v2026.08.md

KNOWLEDGE INVENTORY (KHO KIẾN THỨC)
= ROADMAP.md + roadmap/part-00..22.md

DEFAULT LEARNER EXECUTION (ĐƯỜNG HỌC MẶC ĐỊNH)
= BUILD-FIRST.md + Mission system

CURRENT FACTS (DỮ KIỆN HIỆN HÀNH)
= freshness policy + external source registers
```

Build-First thay execution order (thứ tự thực thi), **không** tự đổi Part/Chapter/Lesson IDs, 14 main Projects, provenance (nguồn gốc) hoặc learner PASS history.

## 2. Quy tắc Build-First

Đọc:

- [`BUILD-FIRST.md`](BUILD-FIRST.md)
- [`docs/BUILD-FIRST-LEARNING-MODEL.md`](docs/BUILD-FIRST-LEARNING-MODEL.md)
- [`docs/EXECUTION-MODEL.md`](docs/EXECUTION-MODEL.md)
- [`docs/LANGUAGE-POLICY.md`](docs/LANGUAGE-POLICY.md)

Quy tắc nền:

```text
Mission ≠ Lesson ≠ Project ≠ Bot Version
```

- Mission có thể pull kiến thức từ nhiều Part.
- Dùng Go sớm không đồng nghĩa đã mastery Part 15.
- Mission không được tự đánh dấu Lesson PASS.
- `required knowledge for Mission ≠ full Lesson PASS`.
- Không bulk-edit 671 Lesson chỉ để thêm Mission mapping; dùng central Mission ↔ Knowledge map.
- Reuse cùng implementation evidence cho Lesson/Mission/Project khi thật sự là cùng requirement; không double-count.

## 3. Learner workspace và reference implementation

Bootstrap hiện tại:

```text
learner workspace: lab/learner/affiliate-bot/
reference v0.3:    lab/affiliate-bot/
```

Reference không phải learner starting state. Không copy reference rồi coi là Mission PASS.

`PROGRESS.md` xác định Current Mission. Semantic CI dùng Current Mission để đặt capability ceiling (trần năng lực) cho learner workspace, tránh leak lời giải Mission sau nhưng vẫn cho workspace tiến hóa đúng M00 → M03.

## 4. Hướng Go-first

Primary implementation language (ngôn ngữ triển khai chính) là **Go**.

Nguyên tắc engineering:

```text
modular monolith first (khối đơn thể mô-đun trước)
+ deterministic logic before LLM (logic xác định trước LLM)
+ explicit tool boundary (ranh giới tool rõ ràng)
+ durable state when needed (state bền vững khi cần)
+ least privilege (quyền tối thiểu)
+ RISK 0/1/2 governance
+ Human Approval cho consequential action
+ audit/tracing/kill switch
```

Tài liệu:

- [`docs/ADR-001-GO-FIRST-BOT-STACK.md`](docs/ADR-001-GO-FIRST-BOT-STACK.md)
- [`docs/GO-BOT-ENGINEERING-STACK.md`](docs/GO-BOT-ENGINEERING-STACK.md)
- [`docs/AUTONOMY-AND-APPROVAL-MODEL.md`](docs/AUTONOMY-AND-APPROVAL-MODEL.md)
- [`docs/AGENT-SECURITY-AND-TOOL-GOVERNANCE.md`](docs/AGENT-SECURITY-AND-TOOL-GOVERNANCE.md)

Current runtime/library facts phải theo freshness layer. Không hard-code một version hiện hành thành permanent curriculum truth.

## 5. Lesson authoring (soạn bài)

Dùng:

- [`templates/LESSON.md`](templates/LESSON.md)
- [`docs/LESSON-AUTHORING-STANDARD.md`](docs/LESSON-AUTHORING-STANDARD.md)
- [`docs/PASS-CRITERIA.md`](docs/PASS-CRITERIA.md)

Hai state độc lập:

```text
Authoring: planned → draft → ready
Learner:   chưa PASS → PASS / RETRY
```

`ready` không bao giờ có nghĩa learner PASS.

## 6. Dữ kiện hiện hành

Platform/legal/API/software facts có thể thay đổi phải dùng external verification và `last_verified` theo [`docs/FRESHNESS-POLICY.md`](docs/FRESHNESS-POLICY.md).

Không biến current runtime/library/platform value thành canonical truth vĩnh viễn.

## 7. An toàn evidence

Không commit:

- API key/token/password;
- personal/sensitive raw export;
- credential;
- secret;
- nội dung không có quyền phân phối.

Artifact tồn tại không tự động nghĩa PASS.

## 8. Quy chuẩn ngôn ngữ

**Tiếng Việt là ngôn ngữ chính thức của repository.**

English term được giữ khi cần độ chính xác kỹ thuật hoặc đối chiếu nguồn ngoài; ở lần xuất hiện quan trọng nên có giải thích tiếng Việt. Không chuyển file Markdown learner-facing hoặc maintainer-facing thành English-only nếu không có lý do kỹ thuật.

Xem [`docs/LANGUAGE-POLICY.md`](docs/LANGUAGE-POLICY.md).

## 9. Kiểm tra trước Pull Request / Merge

Từ root repository:

```bash
python scripts/validate_curriculum.py
python scripts/validate_hardening.py
python scripts/validate_build_first.py
python -m unittest discover -s tests -v
```

Reference Bot:

```bash
cd lab/affiliate-bot
test -z "$(gofmt -l .)"
go vet ./...
go test ./...
```

Learner Bot:

```bash
cd lab/learner/affiliate-bot
test -z "$(gofmt -l .)"
go vet ./...
go test ./...
```

Chi tiết error codes và semantic guards: [`docs/CURRICULUM-CI.md`](docs/CURRICULUM-CI.md).

Checklist:

- [ ] active canonical vẫn là v2026.09;
- [ ] historical v2026.08 được giữ nguyên;
- [ ] 23 Parts / 89 Chapters / 671 lessons / 14 Projects không đổi trừ khi có canonical revision riêng được phê duyệt;
- [ ] Go-first vẫn là primary direction;
- [ ] relative links hoạt động;
- [ ] freshness metadata hợp lệ;
- [ ] không thay learner checkbox chỉ vì content/code tồn tại;
- [ ] không làm mờ Mission/Lesson/Project/Bot Version semantics;
- [ ] `bot_version_from` nối đúng version của Mission trước;
- [ ] Mission dependency thực sự tồn tại;
- [ ] Mission `ready` có explicit canonical required knowledge;
- [ ] Mission Project mapping khớp central Bot Evolution map;
- [ ] learner workspace không vượt capability ceiling của Current Mission;
- [ ] learner/reference Go line đồng bộ;
- [ ] consequential side effects vẫn giữ policy/risk/approval boundary;
- [ ] code/evidence không chứa secret;
- [ ] Markdown tuân thủ Language Policy.

## 10. Repository governance (quản trị repo)

Không merge PR khi `Curriculum CI` fail.

`main` nên được GitHub branch protection/ruleset cưỡng chế:

- require Pull Request;
- require `Curriculum CI / validate-curriculum` hoặc status check tương ứng;
- block force push;
- block deletion.

Xem [`docs/REPOSITORY-GOVERNANCE.md`](docs/REPOSITORY-GOVERNANCE.md).

## 11. Licensing (giấy phép)

Repository là public nhưng hiện chưa publish open-source license cho curriculum/content. Xem [`docs/LICENSING.md`](docs/LICENSING.md).