# Affiliate Expert Learning Roadmap

Roadmap thực hành để phát triển đồng thời ba năng lực:

**Affiliate Expert + Affiliate Bot Engineer = Affiliate Intelligence Expert**

Roadmap được chuẩn hóa từ ba tài liệu nguồn v2026.08. Lộ trình mặc định hiện là **15 tháng ở khoảng 9 giờ/tuần**, review cố định **12:00 Chủ nhật**. Track **12 tháng** được giữ dưới dạng accelerated plan cho người có thể duy trì khoảng **11–12 giờ/tuần**.

## Bắt đầu ở đây

1. Mở [ROADMAP.md](ROADMAP.md) để xem toàn bộ 23 phần.
2. Chọn timeline: [15-month Standard](docs/15-MONTH-PLAN.md) hoặc [12-month Accelerated](docs/12-MONTH-PLAN.md).
3. Đọc [Hybrid Execution Model](docs/EXECUTION-MODEL.md).
4. Tra [Source-to-Roadmap Traceability Map](docs/SOURCE-MAPPING.md) khi author/học lesson.
5. Chỉ đổi `[ ]` thành `[x]` sau khi đạt đủ [5 tiêu chí PASS](docs/PASS-CRITERIA.md).
6. Dùng [Lesson Notes](templates/LESSON-NOTES.md) và lưu evidence theo [Artifact conventions](artifacts/README.md).
7. Trước khi merge thay đổi curriculum, chạy [Curriculum CI](docs/CURRICULUM-CI.md).
8. Cập nhật [PROGRESS.md](PROGRESS.md) vào review Chủ nhật.

## Quy mô chương trình

- **23 phần**
- **89 chương**
- **671 bài học có thể tick**
- **14 main projects**
- Labs và Pass Gates là integration checkpoints riêng, không tính thành Project #15+
- **Standard:** 15 tháng, khoảng 9 giờ/tuần
- **Accelerated:** 12 tháng, khoảng 11–12 giờ/tuần

## Learning operating system

Authoring và evidence được tách rõ:

- [`templates/LESSON.md`](templates/LESSON.md) — authoring template cho bài giảng
- [`templates/LESSON-NOTES.md`](templates/LESSON-NOTES.md) — learner evidence cho từng lesson
- [`templates/EXPERIMENT-LOG.md`](templates/EXPERIMENT-LOG.md) — experiment hypothesis/result/learning
- [`templates/REVENUE-JOURNAL.md`](templates/REVENUE-JOURNAL.md) — revenue/reconciliation/economics
- [`templates/KNOWLEDGE-ENTRY.md`](templates/KNOWLEDGE-ENTRY.md) — knowledge base entry
- [`templates/PROJECT-README.md`](templates/PROJECT-README.md) — project scope/acceptance/evidence
- [`templates/RETROSPECTIVE.md`](templates/RETROSPECTIVE.md) — retrospective
- [`artifacts/README.md`](artifacts/README.md) — naming, linking, reuse và sensitive-data rules

Artifact tồn tại không tự động đồng nghĩa PASS. Lesson vẫn cần Concept + Example + Quiz ≥80% + Practice + Explain-back; project/lab/gate cần acceptance criteria riêng.

## Lesson scaffolding

Dùng [`scripts/scaffold_lesson.py`](scripts/scaffold_lesson.py) để tạo lesson scaffold **theo nhu cầu**, không sinh hàng loạt 670 file rỗng.

Ví dụ:

```bash
python scripts/scaffold_lesson.py --lesson 0.2 --effort M --minutes 60 --prerequisite 0.1 --dry-run
```

Scaffolder:

- đọc ID/title/chapter từ roadmap;
- dùng `templates/LESSON.md`;
- luôn tạo `status: planned`;
- tạo canonical `source_refs`;
- không overwrite file đã tồn tại;
- không tick roadmap và không thay đổi learner PASS state.

Xem [Lesson Scaffolding Guide](docs/LESSON-SCAFFOLDING.md).

## Curriculum CI

Repo có validator không cần dependency ngoài:

```bash
python scripts/validate_curriculum.py
python -m unittest discover -s tests -v
```

GitHub Action chạy trên mọi pull request và mọi push vào `main`.

Validator kiểm tra tối thiểu:

- broken relative links;
- Part/Chapter/Lesson counts giữa `ROADMAP.md` và part files;
- duplicate/gap lesson IDs;
- lesson path/link consistency;
- metadata bắt buộc cho lesson mới;
- `planned|draft|ready` linkage convention;
- heading hierarchy cơ bản.

Lesson 0.1 đang có legacy exception tạm thời cho metadata/heading tới Issue #9; relative links vẫn được kiểm tra bình thường.

Xem [Curriculum CI Guide](docs/CURRICULUM-CI.md).

## Hybrid execution

Roadmap không phải tuyến tính tuyệt đối. Knowledge spine đi theo prerequisite; execution loops đã mở khóa tiếp tục chạy song song trong cùng weekly capacity.

Xem [Hybrid Execution Model](docs/EXECUTION-MODEL.md).

## Source traceability

`SYLLABUS-v2026.08.md` là nguồn cấu trúc chuẩn; training/research files là supplement. Không tạo source mapping giả khi nguồn không hỗ trợ claim.

Xem [SOURCE-MAPPING.md](docs/SOURCE-MAPPING.md).

## Lesson authoring standard

Lesson mới phải được viết từ [`templates/LESSON.md`](templates/LESSON.md). `status: planned|draft|ready` là authoring status, không phải learner PASS state.

Lesson `ready` phải có answer key hoặc scoring rubric, artifact rõ ràng và external verification khi có claim hiện hành về platform/legal/tax/policy/API.

Xem [Lesson Authoring Standard](docs/LESSON-AUTHORING-STANDARD.md).

## Effort-aware planning

- **S:** 15–30 phút
- **M:** 45–75 phút
- **L:** 1.5–3 giờ
- **XL:** Lab/Project/Pass Gate integration

Xem [Effort Model](docs/EFFORT-MODEL.md).

## Nguyên tắc vận hành

```text
LEARN → EXPLAIN → APPLY → TEST → PASS
```

- Data > Opinion.
- Expected Value > Commission Rate.
- Không automate thứ chưa hiểu bằng tay.
- Timeline là forecast; PASS evidence mới là gate.
- Reuse artifact bằng link; không double-count effort.
- Scaffold file ≠ authored lesson ≠ learner PASS.
- Curriculum CI phải PASS trước khi merge thay đổi curriculum.

## Tài liệu

- [Roadmap](ROADMAP.md)
- [Hybrid Execution Model](docs/EXECUTION-MODEL.md)
- [Source Mapping](docs/SOURCE-MAPPING.md)
- [Lesson Authoring Standard](docs/LESSON-AUTHORING-STANDARD.md)
- [Lesson Scaffolding Guide](docs/LESSON-SCAFFOLDING.md)
- [Curriculum CI Guide](docs/CURRICULUM-CI.md)
- [Effort Model](docs/EFFORT-MODEL.md)
- [15-Month Standard](docs/15-MONTH-PLAN.md)
- [12-Month Accelerated](docs/12-MONTH-PLAN.md)
- [14 Projects + Labs/Pass Gates](docs/PROJECTS.md)
- [PASS Criteria](docs/PASS-CRITERIA.md)
- [Artifact conventions](artifacts/README.md)
- [Tài liệu nguồn](sources/README.md)
