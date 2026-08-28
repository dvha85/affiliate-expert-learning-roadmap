# Curriculum CI

Curriculum CI ngăn roadmap drift khi số lesson tăng lên. Validator dùng **Python standard library**, chạy được local và trong GitHub Actions.

## Chạy local

```bash
python scripts/validate_curriculum.py
```

Chạy mutation tests:

```bash
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

### 2. Lesson IDs

Kiểm tra:

- duplicate lesson ID trong roadmap;
- lesson suffix gap trong từng chapter;
- lesson ID nằm sai chapter;
- duplicate lesson file ID;
- lesson file không có ID tương ứng trong roadmap.

### 3. Relative links

Kiểm tra Markdown relative links trong:

- root docs (`README.md`, `ROADMAP.md`, `PROGRESS.md`);
- `docs/`;
- `roadmap/`;
- `lessons/`;
- `templates/`;
- `artifacts/`.

External URL và anchor-only link không được resolve local.

### 4. Lesson metadata

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

Validator cũng kiểm tra:

- `status ∈ planned|draft|ready`;
- `effort ∈ S|M|L`;
- `estimated_minutes > 0`;
- part/chapter metadata khớp path;
- canonical source ref `S:P/C/L` khớp lesson.

Từ Step 9 trở đi **không còn legacy lesson exception**. Bài 0.1 đã được migrate thành reference implementation và phải pass cùng contract như các lesson khác.

## Planned-only convention

Scaffold `status: planned` **không được link từ roadmap như một lesson đã authored**.

Khi lesson chuyển sang `draft` hoặc `ready`, roadmap phải link tới file lesson đó.

Điều này bảo vệ nguyên tắc:

```text
scaffold file ≠ authored lesson ≠ learner PASS
```

## Heading checks

Lesson phải:

- có đúng một H1;
- H1 là heading đầu tiên;
- không nhảy heading level, ví dụ H2 → H4.

## Reference implementation

`lessons/part-00/chapter-00/0.1-affiliate-expert-la-gi.md` là bài reference cho authored lesson `ready`:

- front matter đầy đủ;
- source refs và prerequisites rõ;
- effort estimate cụ thể;
- đúng heading hierarchy;
- có objectives, concept, explanation, example, real case, misconceptions;
- có artifact + DoD;
- có quiz + answer key;
- có explain-back + 5 PASS criteria;
- có Knowledge Base update, summary, source list và next action.

## Mutation tests

`tests/test_curriculum_validator.py` chứng minh validator fail khi cố ý tạo:

1. broken relative link;
2. count mismatch;
3. duplicate lesson ID;
4. missing required metadata.

Đây là regression guard cho acceptance criteria của Issue #8.

## GitHub Actions

Workflow:

```text
.github/workflows/curriculum-ci.yml
```

Chạy trên:

- mọi pull request;
- mọi push vào `main`.

Một PR không nên merge khi Curriculum CI đang fail.

## Error codes

Các nhóm chính:

- `ROADMAP*` — canonical roadmap/index format;
- `COUNT*` — count/chapter/part mismatch;
- `ID*` — duplicate/gap/wrong placement;
- `LINK*` — broken or invalid relative link;
- `META*` — lesson metadata/path mismatch;
- `STATE*` — planned/draft/ready linkage convention;
- `HEAD*` — Markdown heading structure.

Validator cố gắng báo nhiều lỗi trong một lần chạy thay vì dừng ở lỗi đầu tiên để repair nhanh hơn.
