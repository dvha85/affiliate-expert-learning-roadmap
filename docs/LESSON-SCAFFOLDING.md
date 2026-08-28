# Lesson Scaffolding Guide

`script/scaffold_lesson.py` không tồn tại; script chuẩn là:

```text
scripts/scaffold_lesson.py
```

Mục tiêu của scaffolder là tạo **khung lesson có trạng thái rõ ràng** từ roadmap, không phải sinh nội dung hoàn chỉnh hàng loạt.

## Nguyên tắc an toàn

Scaffolder:

- đọc lesson ID/title/chapter từ `roadmap/part-XX.md`;
- dùng `templates/LESSON.md` làm source template;
- luôn tạo `status: planned`;
- tự sinh canonical source ref `S:P{part}/C{chapter}/L{lesson}`;
- lấy T/R supplement ở mức chapter từ `docs/SOURCE-MAPPING.md` khi parse được;
- thêm `effort`, `estimated_minutes`, `prerequisites`;
- không overwrite file lesson đã tồn tại;
- không tick roadmap;
- không đổi learner PASS state;
- không đổi lesson sang `ready`.

> File scaffold tồn tại **không đồng nghĩa lesson đã authored**.

## Dùng cho một lesson

Dry-run:

```bash
python scripts/scaffold_lesson.py --lesson 0.2 --effort M --minutes 60 --prerequisite 0.1 --dry-run
```

Tạo thật:

```bash
python scripts/scaffold_lesson.py --lesson 0.2 --effort M --minutes 60 --prerequisite 0.1
```

Output path tự sinh:

```text
lessons/part-00/chapter-00/0.2-affiliate-bot-engineer-la-gi.md
```

## Dùng cho một chapter

```bash
python scripts/scaffold_lesson.py --chapter 38 --effort M --minutes 60 --dry-run
```

Khi tạo theo chapter/part, effort/minutes truyền vào là **provisional planning value**. Author phải review từng lesson trước khi đổi sang `draft` hoặc `ready`.

## Dùng cho một Part

```bash
python scripts/scaffold_lesson.py --part 12 --effort M --minutes 60 --dry-run
```

Không dùng lệnh này để tạo toàn bộ 671 files chỉ để “lấp chỗ trống”. Scaffold theo nhu cầu authoring thực tế.

## Validate

```bash
python scripts/scaffold_lesson.py --lesson 0.2 --validate
```

Validator hiện kiểm tra tối thiểu:

- lesson ID;
- `status`;
- `effort`;
- `prerequisites`;
- `source_refs`;
- canonical `S:P/C/L` ref.

Step 8 sẽ bổ sung curriculum CI toàn repo.

## Collision behavior

Nếu file đích đã tồn tại, script dừng và trả exit code khác 0.

Ví dụ bài 0.1 đã tồn tại:

```bash
python scripts/scaffold_lesson.py --lesson 0.1
```

phải bị từ chối. Không có `--force` ở Step 7 để tránh overwrite nội dung thật.

## Status lifecycle

```text
scaffold
→ status: planned
→ author nội dung
→ status: draft
→ đạt Lesson Authoring DoD
→ status: ready
→ learner học + làm evidence
→ PASS / RETRY
```

Scaffolder chỉ thực hiện bước đầu tiên.

## Effort

`--effort` nhận `S|M|L`.

`--minutes` là estimate cụ thể và phải được author review theo `docs/EFFORT-MODEL.md`.

Không dùng `XL` cho lesson scaffold; XL chủ yếu là LAB/PROJECT/PASS Gate.

## Source refs

Canonical ref được tạo deterministic từ roadmap:

```text
S:P{part}/C{chapter}/L{lesson-id}
```

Training/research supplement chỉ là chapter-level hint lấy từ `SOURCE-MAPPING.md`. Author lesson phải đọc nguồn thật và xóa/refine ref không sử dụng trước khi `ready`.

## Prerequisites

Script không đoán prerequisite từ thứ tự lesson.

Dùng `--prerequisite` lặp lại khi dependency đã biết:

```bash
python scripts/scaffold_lesson.py \
  --lesson 0.2 \
  --prerequisite 0.1 \
  --prerequisite "concept: affiliate system flow"
```

Nếu không truyền, metadata là:

```yaml
prerequisites: []
```

Điều này phù hợp với Lesson Authoring Standard: chỉ ghi dependency thật.
