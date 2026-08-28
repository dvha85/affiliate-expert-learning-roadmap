# Affiliate Expert Learning Roadmap

**Structured, evidence-based curriculum for becoming an Affiliate Expert + Affiliate Bot Engineer → Affiliate Intelligence Expert.**

Roadmap thực hành để phát triển đồng thời ba năng lực:

**Affiliate Expert + Affiliate Bot Engineer = Affiliate Intelligence Expert**

Roadmap được chuẩn hóa từ ba tài liệu nguồn v2026.08. Lộ trình mặc định hiện là **15 tháng ở khoảng 9 giờ/tuần**, review cố định **12:00 Chủ nhật**. Track **12 tháng** được giữ dưới dạng accelerated plan cho người có thể duy trì khoảng **11–12 giờ/tuần**.

## Trạng thái curriculum hiện tại

Repo đã hoàn tất **Curriculum Repair Program v1** về architecture, timeline, source traceability, authoring standard, evidence system, scaffolding và Curriculum CI.

Trạng thái nội dung không được suy diễn từ số file:

- **0.1 — Affiliate Expert là gì?**: `ready`, reference implementation;
- **0.2 — Affiliate Bot Engineer là gì?**: `planned`, scaffold test, chưa authored;
- các lesson còn lại: chỉ được coi là authored khi có file `draft|ready` đúng contract và được link từ roadmap;
- checkbox `[x]` chỉ phản ánh **learner PASS**, không phản ánh file existence hay authoring status.

Repo có **23 Part · 89 Chapter · 671 lesson**, nhưng điều đó **không có nghĩa 671 lesson đã có nội dung hoàn chỉnh**.

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

## Lesson status convention

Repo tách ba trạng thái khác nhau:

```text
File scaffold
→ authoring status: planned

Nội dung đang viết / đã đủ học
→ authoring status: draft / ready

Người học hoàn thành evidence
→ learner result: PASS / RETRY
```

Quy ước roadmap:

- `planned` scaffold tồn tại trong `lessons/` nhưng **chưa link** từ roadmap;
- `draft` hoặc `ready` phải được link từ roadmap;
- checkbox `[x]` chỉ phản ánh **learner PASS**, không phản ánh authoring status.

Bài [`0.1 — Affiliate Expert là gì?`](lessons/part-00/chapter-00/0.1-affiliate-expert-la-gi.md) là **reference implementation** cho một lesson `ready`. Bài 0.2 hiện vẫn chỉ là scaffold `planned`.

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
- metadata bắt buộc cho mọi lesson file;
- `planned|draft|ready` linkage convention;
- heading hierarchy cơ bản.

Từ Step 9, **không còn legacy exception cho lesson 0.1**. Tất cả lesson file đều phải pass cùng metadata/heading contract.

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

Reference implementation: [`0.1 — Affiliate Expert là gì?`](lessons/part-00/chapter-00/0.1-affiliate-expert-la-gi.md).

Xem [Lesson Authoring Standard](docs/LESSON-AUTHORING-STANDARD.md).

## Effort-aware planning

- **S:** 15–30 phút
- **M:** 45–75 phút
- **L:** 1.5–3 giờ
- **XL:** Lab/Project/Pass Gate integration

Xem [Effort Model](docs/EFFORT-MODEL.md).

## Contributing

Repo dùng mô hình **issue-first** cho thay đổi curriculum. Không bulk-generate lesson placeholder và không thay đổi canonical structure khi chưa có quyết định rõ ràng.

Trước PR, chạy:

```bash
python scripts/validate_curriculum.py
python -m unittest discover -s tests -v
```

Đọc [`CONTRIBUTING.md`](CONTRIBUTING.md) để xem authoring workflow, source policy, current-fact verification và PR checklist.

## Licensing

Repository hiện **public nhưng không được phát hành theo open-source license**. Không mặc định MIT/Apache/GPL và không có quyền sao chép, sửa đổi, tái phân phối hoặc thương mại hóa nội dung chỉ vì repo có thể xem công khai.

Xem [`docs/LICENSING.md`](docs/LICENSING.md) để biết trạng thái và phạm vi licensing hiện tại.

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
- [Contribution Guide](CONTRIBUTING.md)
- [Licensing Status](docs/LICENSING.md)
- [Tài liệu nguồn](sources/README.md)
