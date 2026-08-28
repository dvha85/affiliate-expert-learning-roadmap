# Curriculum CI

Curriculum CI ngăn roadmap drift khi số lesson tăng lên. Validator dùng **Python standard library**, chạy được local và trong GitHub Actions.

## Chạy local

```bash
python scripts/validate_curriculum.py
python -m unittest discover -s tests -v
```

Exit code `0` nghĩa là PASS; khác `0` nghĩa là phải sửa consistency trước khi merge.

## Các kiểm tra chính

### 1. Roadmap counts

Validator đối chiếu:

- tổng **23 Part / 89 Chapter / 671 lesson** trong `ROADMAP.md`;
- từng Part row với `roadmap/part-XX.md`;
- chapter range và lesson count của từng Part;
- Part file ngoài index.

### 2. Timeline contract

Mọi `roadmap/part-XX.md` phải có dòng metadata chuẩn:

```text
- Timeline: **...**
```

CI fail nếu thiếu `Timeline:` hoặc còn header legacy `Lịch đề xuất:`. Mục tiêu là ngăn per-Part files quay lại lịch 12 tháng cũ trong khi repo đã tách Standard 15-month và Accelerated 12-month.

### 3. Lesson IDs

Kiểm tra duplicate lesson ID, suffix gap, lesson nằm sai chapter, duplicate lesson file ID và lesson file không có ID tương ứng trong roadmap.

### 4. Relative links

Kiểm tra Markdown relative links trong:

- mọi root-level `*.md` (`README.md`, `ROADMAP.md`, `PROGRESS.md`, `CONTRIBUTING.md`, ...);
- `docs/`, `roadmap/`, `lessons/`, `templates/`, `artifacts/`, `sources/`.

External URL và anchor-only link không được resolve local.

### 5. Lesson metadata

Mọi lesson file phải có tối thiểu:

```yaml
lesson_id:
title:
part:
chapter:
effort:
estimated_minutes:
status:
prerequisites:
source_refs:
last_verified:
```

Validator cũng kiểm tra `status`, `effort`, `estimated_minutes`, path metadata và canonical `S:P/C/L` source ref.

Không có legacy lesson exception. Bài 0.1 phải pass cùng contract như mọi lesson khác.

### 6. Freshness metadata contract

Current facts được quản lý theo [`FRESHNESS-POLICY.md`](FRESHNESS-POLICY.md).

CI enforce metadata-level invariants:

```text
external refs có dữ liệu
→ last_verified bắt buộc là YYYY-MM-DD

last_verified có ngày
→ phải có ít nhất một external ref
```

Error codes:

- `FRESH001` — external refs nhưng thiếu `last_verified`;
- `FRESH002` — có `last_verified` nhưng không có external refs;
- `FRESH003` — ngày không phải ISO `YYYY-MM-DD`.

CI **không thể tự chứng minh một policy/law/API còn đúng**. HIGH/MEDIUM/LOW review cadence vẫn cần human research theo Freshness Policy.

Current source register bắt đầu tại [`AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md`](AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md).

## Planned-only convention

Scaffold `status: planned` **không được link từ roadmap như một lesson đã authored**. Khi lesson chuyển sang `draft` hoặc `ready`, roadmap phải link tới file lesson đó.

```text
scaffold file ≠ authored lesson ≠ learner PASS
```

## Heading checks

Lesson phải có đúng một H1, H1 là heading đầu tiên và không nhảy heading level.

## Reference implementation

`lessons/part-00/chapter-00/0.1-affiliate-expert-la-gi.md` là bài reference cho authored lesson `ready` với front matter, source refs, effort, heading hierarchy, objectives, concept, example/case, misconceptions, artifact, quiz/answer key, explain-back, PASS criteria, Knowledge Base, summary, sources và next action.

## Mutation / regression tests

`tests/test_curriculum_validator.py` bảo vệ:

1. broken relative link;
2. broken root/source links;
3. count mismatch;
4. duplicate lesson ID;
5. missing required metadata;
6. missing normalized timeline;
7. broken external-ref/verification-date contract.

`tests/test_scaffold_lesson.py` bảo vệ:

- dry-run trên target đã tồn tại là non-fatal;
- write thật vẫn từ chối overwrite.

## GitHub Actions

Workflow `.github/workflows/curriculum-ci.yml` chạy trên mọi pull request và mọi push vào `main`. Một PR không nên merge khi Curriculum CI đang fail.

## Error-code groups

- `ROADMAP*` — canonical roadmap/index format;
- `COUNT*` — count/chapter/part mismatch;
- `TIME*` — per-Part timeline contract;
- `ID*` — duplicate/gap/wrong placement;
- `LINK*` — broken or invalid relative link;
- `META*` — lesson metadata/path mismatch;
- `FRESH*` — current-source verification metadata;
- `STATE*` — planned/draft/ready linkage convention;
- `HEAD*` — Markdown heading structure.

Validator cố gắng báo nhiều lỗi trong một lần chạy thay vì dừng ở lỗi đầu tiên để repair nhanh hơn.
