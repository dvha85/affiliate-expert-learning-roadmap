# Contributing to Affiliate Expert Learning Roadmap

Repo này đang được phát triển như một curriculum có kiểm soát, không phải wiki mở nơi mọi thay đổi cấu trúc đều được merge trực tiếp.

## 1. Contribution model

Ưu tiên **issue-first**:

1. Mở Issue mô tả thay đổi đề xuất.
2. Chỉ sửa canonical structure sau khi xác nhận ảnh hưởng tới syllabus, roadmap và source mapping.
3. Với lesson mới, scaffold từ công cụ của repo rồi author theo chuẩn.
4. Chạy Curriculum CI trước khi mở/merge PR.

Không bulk-generate lesson file để tạo cảm giác curriculum đã hoàn thiện.

## 2. Canonical sources và current overlay

Thứ tự nguồn:

```text
STRUCTURE: SYLLABUS v2026.08
PACING: current 15/12-month plans
EXECUTION ORDER: docs/EXECUTION-MODEL.md
SUPPLEMENTS: training + research sources
CURRENT FACTS: external source register + verified date
```

Xem:

- [`docs/SOURCE-MAPPING.md`](docs/SOURCE-MAPPING.md)
- [`docs/FRESHNESS-POLICY.md`](docs/FRESHNESS-POLICY.md)
- [`docs/AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md`](docs/AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md)

Không tự ý đổi Part/Chapter/Lesson ID, main Project, LAB hoặc PASS Gate chỉ vì một platform đổi tên metric/chính sách. Khi canonical term đã cũ nhưng cấu trúc vẫn đúng, dùng **current-state override** và giữ provenance.

## 3. Authoring lesson

Dùng:

- [`templates/LESSON.md`](templates/LESSON.md)
- [`docs/LESSON-AUTHORING-STANDARD.md`](docs/LESSON-AUTHORING-STANDARD.md)
- [`scripts/scaffold_lesson.py`](scripts/scaffold_lesson.py)

Ví dụ inspection:

```bash
python scripts/scaffold_lesson.py --lesson 0.2 --effort M --minutes 60 --prerequisite 0.1 --dry-run
```

0.2 hiện đã tồn tại dưới dạng scaffold test; dry-run phải báo `EXISTS ... would not overwrite` và không fail. Write thật vẫn không overwrite file hiện hữu.

Status contract:

```text
planned = scaffold/chưa authored
draft   = đang author
ready   = nội dung đủ để học

PASS/RETRY = kết quả người học, không phải authoring status
```

Lesson `ready` phải có đủ 5 PASS flows:

1. Concept
2. Example / case
3. Quiz ≥80% + answer key/rubric
4. Practice artifact
5. Explain-back

## 4. Source refs và current facts

Mọi lesson phải có canonical `S:` ref. `T:` và `R:` chỉ thêm khi nguồn thực sự hỗ trợ nội dung.

Với claim hiện hành về platform policy, eligibility, attribution, commission, API, legal, tax, privacy, AIGC, pricing, payment hoặc software/search behavior có thể thay đổi, author phải external-verify tại thời điểm viết.

Metadata contract:

```yaml
source_refs:
  external:
    - "EXT:<provider>:<topic>"
last_verified: "YYYY-MM-DD"
```

- có external refs → bắt buộc `last_verified`;
- có `last_verified` → bắt buộc external refs;
- ưu tiên official/government/primary source;
- HIGH-volatility facts re-check tối đa 30 ngày, MEDIUM tối đa 90 ngày, LOW tối đa 12 tháng hoặc khi có evidence thay đổi.

Không hard-code current platform threshold như sự thật vĩnh viễn.

## 5. Artifact/evidence

Tuân theo [`artifacts/README.md`](artifacts/README.md).

Không commit:

- API key, token, password;
- dữ liệu cá nhân nhạy cảm;
- credential;
- raw export chứa thông tin không cần thiết;
- nội dung có vấn đề bản quyền mà repo không có quyền phân phối.

Artifact tồn tại không tự động đồng nghĩa PASS.

## 6. Pull request checklist

Trước khi PR:

```bash
python scripts/validate_curriculum.py
python -m unittest discover -s tests -v
```

PR thay đổi curriculum nên tự kiểm tra:

- [ ] Không làm drift 23 Part / 89 Chapter / 671 lesson nếu không có thay đổi canonical được duyệt.
- [ ] 23 Part files vẫn dùng normalized `Timeline:` metadata; không tái xuất hiện `Lịch đề xuất:` legacy.
- [ ] Không tạo duplicate/gap lesson ID.
- [ ] Relative links hoạt động, gồm root Markdown và `sources/`.
- [ ] Lesson metadata/path/source ref khớp nhau.
- [ ] External refs ↔ `last_verified` đúng contract.
- [ ] `planned` không được link như authored lesson.
- [ ] `draft|ready` được link từ roadmap.
- [ ] Không tick learner checkbox chỉ vì lesson file đã tồn tại.
- [ ] Nội dung policy/legal/current-platform đã external-verify khi cần.
- [ ] Current-state override dùng khi platform terminology thay đổi nhưng canonical syllabus chưa đổi.
- [ ] Không làm mất answer key/rubric hoặc PASS evidence contract.

## 7. Reference implementation

Bài [`0.1 — Affiliate Expert là gì?`](lessons/part-00/chapter-00/0.1-affiliate-expert-la-gi.md) là reference implementation hiện tại cho lesson `ready`.

Không yêu cầu mọi lesson dài bằng 0.1. Depth phải phù hợp effort S/M/L.

## 8. Licensing và quyền sử dụng

Repo hiện **không cấp open-source license** cho curriculum/content.

Việc repository public không tự động cấp quyền sao chép, sửa đổi, tái phân phối hoặc thương mại hóa nội dung. Xem [`docs/LICENSING.md`](docs/LICENSING.md).

Contributor chỉ nên gửi nội dung mà họ có quyền đóng góp. Việc merge contribution không tự động thay đổi licensing policy của toàn repo.
