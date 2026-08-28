# Affiliate Expert Learning Roadmap

**Structured, evidence-based curriculum for becoming an Affiliate Expert + Affiliate Bot Engineer → Affiliate Intelligence Expert.**

Roadmap thực hành để phát triển đồng thời ba năng lực:

**Affiliate Expert + Affiliate Bot Engineer = Affiliate Intelligence Expert**

Roadmap được chuẩn hóa từ ba tài liệu nguồn v2026.08. Lộ trình mặc định là **15 tháng ở khoảng 9 giờ/tuần**; track **12 tháng** là accelerated plan cho người duy trì khoảng **11–12 giờ/tuần**.

## Trạng thái curriculum hiện tại

- Curriculum Repair Program v1: **hoàn tất**.
- Post-repair audit + Affiliate knowledge refresh 2026.08: **đang được quản lý qua Issue #18 / CI**.
- **0.1 — Affiliate Expert là gì?**: `ready`, reference implementation.
- **0.2 — Affiliate Bot Engineer là gì?**: `planned`, scaffold test, chưa authored.
- Các lesson còn lại chỉ được coi là authored khi có file `draft|ready` đúng contract và được link từ roadmap.
- Checkbox `[x]` chỉ phản ánh **learner PASS**.

Repo có **23 Part · 89 Chapter · 671 lesson · 14 main projects**, nhưng điều đó **không có nghĩa 671 lesson đã có nội dung hoàn chỉnh**.

## 2026 current-knowledge layer

Canonical syllabus được giữ ổn định; các dữ kiện biến động theo platform/law/tax/privacy/API/search/AI được quản lý bằng một freshness layer riêng:

- [Freshness Policy](docs/FRESHNESS-POLICY.md)
- [Affiliate Knowledge Refresh 2026.08](docs/AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md)

Các update nổi bật đã được map vào curriculum:

- TikTok Shop Vietnam: **PQP → Promotion Performance Score (PPS)** từ 2026-08-27;
- TikTok Shop AIGC truthfulness/disclosure requirements;
- Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 + Nghị định 356/2025/NĐ-CP, hiệu lực 2026;
- Luật Quảng cáo sửa đổi + nghị định hướng dẫn 2026;
- tax framework mới cho hộ/cá nhân kinh doanh;
- privacy-era attribution: không hard-code narrative “third-party cookies chắc chắn biến mất theo lịch X”;
- Google AI Mode/AI Overviews + generative-AI visibility/reporting;
- YouTube Shopping Affiliate hiện có Vietnam trong danh sách thị trường đủ điều kiện;
- agentic commerce/UCP là emerging layer cần theo dõi.

Nguyên tắc:

```text
STABLE CANONICAL CURRICULUM
+
VERIFIED CURRENT FACTS
+
CONTINUOUS WATCH
=
AFFILIATE INTELLIGENCE CURRICULUM
```

Web research không tự động sửa `sources/SYLLABUS-v2026.08.md` hoặc renumber lesson.

## Bắt đầu ở đây

1. Mở [ROADMAP.md](ROADMAP.md) để xem toàn bộ 23 phần.
2. Chọn [15-month Standard](docs/15-MONTH-PLAN.md) hoặc [12-month Accelerated](docs/12-MONTH-PLAN.md).
3. Đọc [Hybrid Execution Model](docs/EXECUTION-MODEL.md).
4. Tra [Source Mapping](docs/SOURCE-MAPPING.md) và [Freshness Policy](docs/FRESHNESS-POLICY.md) khi author lesson.
5. Chỉ tick `[x]` sau khi đạt đủ [5 tiêu chí PASS](docs/PASS-CRITERIA.md).
6. Lưu evidence theo [Artifact conventions](artifacts/README.md).
7. Chạy [Curriculum CI](docs/CURRICULUM-CI.md) trước merge.
8. Cập nhật [PROGRESS.md](PROGRESS.md) trong review định kỳ.

## Timeline contract

Per-Part roadmap files hiện dùng metadata thống nhất:

```text
- Timeline: **Standard ... · Accelerated ...** — forecast; PASS evidence mới là gate.
```

Ngoại lệ có chủ ý:

- Part 20 — Business & Scale: **conditional** khi có tín hiệu doanh thu;
- Part 22 — Continuous Mastery: **post-core continuous**.

Không dùng lại `Lịch đề xuất:` legacy từ lịch cũ.

## Learning operating system

Authoring và learner evidence được tách rõ:

- [`templates/LESSON.md`](templates/LESSON.md) — lesson authoring template
- [`templates/LESSON-NOTES.md`](templates/LESSON-NOTES.md) — learner evidence
- [`templates/EXPERIMENT-LOG.md`](templates/EXPERIMENT-LOG.md) — experiment log
- [`templates/REVENUE-JOURNAL.md`](templates/REVENUE-JOURNAL.md) — revenue/economics
- [`templates/KNOWLEDGE-ENTRY.md`](templates/KNOWLEDGE-ENTRY.md) — knowledge base
- [`templates/PROJECT-README.md`](templates/PROJECT-README.md) — project scope/evidence
- [`templates/RETROSPECTIVE.md`](templates/RETROSPECTIVE.md) — retrospective
- [`artifacts/README.md`](artifacts/README.md) — naming, linking, reuse, sensitive-data rules

Artifact tồn tại không tự động đồng nghĩa PASS. Lesson vẫn cần **Concept + Example + Quiz ≥80% + Practice + Explain-back**.

## Lesson status convention

```text
File scaffold
→ authoring status: planned

Nội dung đang viết / đã đủ học
→ authoring status: draft / ready

Người học hoàn thành evidence
→ learner result: PASS / RETRY
```

- `planned` scaffold tồn tại nhưng **chưa link** từ roadmap;
- `draft|ready` phải được link;
- `[x]` chỉ phản ánh learner PASS.

Reference implementation: [`0.1 — Affiliate Expert là gì?`](lessons/part-00/chapter-00/0.1-affiliate-expert-la-gi.md).

## Lesson scaffolding

Dùng [`scripts/scaffold_lesson.py`](scripts/scaffold_lesson.py) theo nhu cầu, không bulk-generate 670 placeholder files.

Inspection example:

```bash
python scripts/scaffold_lesson.py --lesson 0.2 --effort M --minutes 60 --prerequisite 0.1 --dry-run
```

0.2 đã tồn tại dưới dạng scaffold test nên dry-run báo `EXISTS ... would not overwrite` và exit 0. Actual write vẫn từ chối overwrite.

Xem [Lesson Scaffolding Guide](docs/LESSON-SCAFFOLDING.md).

## Curriculum CI

```bash
python scripts/validate_curriculum.py
python -m unittest discover -s tests -v
```

GitHub Action chạy trên pull request và push vào `main`.

CI hiện kiểm tra:

- 23/89/671 counts và Part/Chapter/Lesson consistency;
- normalized per-Part timeline contract;
- duplicate/gap IDs;
- relative links ở root, docs, roadmap, lessons, templates, artifacts và sources;
- lesson metadata/path/source refs;
- external refs ↔ `last_verified` freshness contract;
- `planned|draft|ready` linkage convention;
- heading hierarchy;
- scaffold dry-run regression behavior.

Xem [Curriculum CI Guide](docs/CURRICULUM-CI.md).

## Source traceability

- `sources/SYLLABUS-v2026.08.md`: canonical curriculum structure.
- training/research files: supplement cho pacing/practice/rationale.
- external web/current sources: **không sửa canonical source**, được quản lý bằng source register + verified date.

Xem:

- [Source Mapping](docs/SOURCE-MAPPING.md)
- [Source README](sources/README.md)
- [Freshness Policy](docs/FRESHNESS-POLICY.md)
- [Affiliate Knowledge Refresh 2026.08](docs/AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md)

## Lesson authoring standard

Lesson mới phải theo [`templates/LESSON.md`](templates/LESSON.md) và [Lesson Authoring Standard](docs/LESSON-AUTHORING-STANDARD.md).

Lesson `ready` phải có answer key/rubric, artifact rõ, current-fact verification khi cần và không còn placeholder.

Volatility guideline:

- **HIGH:** platform policy/eligibility/commission/attribution/legal/tax/privacy/API/AIGC/payment → review tối đa 30 ngày;
- **MEDIUM:** search/discovery/browser/privacy ecosystem/AI-agent capabilities → tối đa 90 ngày;
- **LOW:** fundamentals/formulas/statistics/architecture → tối đa 12 tháng hoặc khi có evidence thay đổi.

## Effort-aware planning

- **S:** 15–30 phút
- **M:** 45–75 phút
- **L:** 1.5–3 giờ
- **XL:** Lab/Project/Pass Gate integration

Xem [Effort Model](docs/EFFORT-MODEL.md).

## Contributing

Repo dùng mô hình **issue-first**. Không bulk-generate placeholder, không thay canonical structure chỉ vì trend/platform rename và không merge curriculum khi CI fail.

Xem [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Licensing

Repository public nhưng **không được phát hành theo open-source license**. Không mặc định MIT/Apache/GPL.

Xem [`docs/LICENSING.md`](docs/LICENSING.md).

## Nguyên tắc vận hành

```text
LEARN → EXPLAIN → APPLY → TEST → PASS
UNDERSTAND → DECIDE → EXECUTE → MEASURE → LEARN → IMPROVE
```

- DATA > OPINION.
- EXPECTED VALUE > COMMISSION RATE.
- Không automate thứ chưa hiểu bằng tay.
- Không optimize trước khi đo.
- Timeline là forecast; PASS evidence mới là gate.
- Scaffold file ≠ authored lesson ≠ learner PASS.
- Current facts cần source + verified date.
- AI/agentic capability không loại bỏ human accountability/compliance.

## Tài liệu

- [Roadmap](ROADMAP.md)
- [15-Month Standard](docs/15-MONTH-PLAN.md)
- [12-Month Accelerated](docs/12-MONTH-PLAN.md)
- [Hybrid Execution Model](docs/EXECUTION-MODEL.md)
- [Source Mapping](docs/SOURCE-MAPPING.md)
- [Freshness Policy](docs/FRESHNESS-POLICY.md)
- [Affiliate Knowledge Refresh 2026.08](docs/AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md)
- [Lesson Authoring Standard](docs/LESSON-AUTHORING-STANDARD.md)
- [Lesson Scaffolding Guide](docs/LESSON-SCAFFOLDING.md)
- [Curriculum CI Guide](docs/CURRICULUM-CI.md)
- [Effort Model](docs/EFFORT-MODEL.md)
- [14 Projects + Labs/Pass Gates](docs/PROJECTS.md)
- [PASS Criteria](docs/PASS-CRITERIA.md)
- [Artifact conventions](artifacts/README.md)
- [Contribution Guide](CONTRIBUTING.md)
- [Licensing Status](docs/LICENSING.md)
- [Tài liệu nguồn](sources/README.md)
