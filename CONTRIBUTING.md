# Contributing to Affiliate Expert Learning Roadmap

Repo này được phát triển như một curriculum có kiểm soát, không phải wiki mở nơi mọi thay đổi cấu trúc đều được merge trực tiếp.

## 1. Contribution model

Ưu tiên **issue-first**:

1. Mở Issue mô tả thay đổi đề xuất.
2. Chỉ sửa canonical structure sau khi xác nhận ảnh hưởng tới syllabus, roadmap và source mapping.
3. Với lesson mới, scaffold từ công cụ của repo rồi author theo chuẩn.
4. Chạy Curriculum CI trước khi mở/merge PR.

Không bulk-generate lesson file để tạo cảm giác curriculum đã hoàn thiện.

## 2. Canonical sources và current overlay

Active source resolution:

```text
ACTIVE CANONICAL:
sources/SYLLABUS-v2026.09.md

INHERITED STRUCTURAL BASELINE:
sources/SYLLABUS-v2026.08.md

PACING:
current 15/12-month plans

EXECUTION ORDER:
docs/EXECUTION-MODEL.md

SUPPLEMENTS:
training + research sources

CURRENT FACTS:
external source registers + verified date
```

Quy tắc:

```text
v2026.09 explicit override
→ v2026.09 thắng

v2026.09 không nói tới
→ kế thừa v2026.08

current software/platform/legal fact
→ freshness layer
```

Xem:

- [`sources/README.md`](sources/README.md)
- [`docs/ADR-001-GO-FIRST-BOT-STACK.md`](docs/ADR-001-GO-FIRST-BOT-STACK.md)
- [`docs/SOURCE-MAPPING.md`](docs/SOURCE-MAPPING.md)
- [`docs/FRESHNESS-POLICY.md`](docs/FRESHNESS-POLICY.md)
- [`docs/AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md`](docs/AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md)
- [`docs/BOT-ENGINEERING-REFRESH-2026.08.md`](docs/BOT-ENGINEERING-REFRESH-2026.08.md)

Không tự ý đổi Part/Chapter/Lesson ID, main Project, LAB hoặc PASS Gate chỉ vì framework/platform đổi. Khi current fact thay đổi nhưng curriculum concept vẫn đúng, dùng freshness/current-state update thay vì rewrite history.

## 3. Go-first engineering direction

Active primary implementation language:

```text
Go
```

C#/.NET được phép trong:

- historical v2026.08 source;
- comparison/reference discussion;
- migration context.

Không đưa C#/.NET-specific framework trở lại active Part 15 primary path nếu chưa có canonical decision mới.

Bot Engineering changes phải đọc cùng:

- [`docs/GO-BOT-ENGINEERING-STACK.md`](docs/GO-BOT-ENGINEERING-STACK.md)
- [`docs/AUTONOMY-AND-APPROVAL-MODEL.md`](docs/AUTONOMY-AND-APPROVAL-MODEL.md)
- [`docs/AGENT-SECURITY-AND-TOOL-GOVERNANCE.md`](docs/AGENT-SECURITY-AND-TOOL-GOVERNANCE.md)

Core architecture principles:

```text
modular monolith first
+ deterministic logic before LLM
+ durable state for long waits
+ explicit tool boundary
+ least privilege
+ RISK 0/1/2 governance
+ human approval for consequential actions
+ audit/tracing/kill switch
```

## 4. Authoring lesson

Dùng:

- [`templates/LESSON.md`](templates/LESSON.md)
- [`docs/LESSON-AUTHORING-STANDARD.md`](docs/LESSON-AUTHORING-STANDARD.md)
- [`scripts/scaffold_lesson.py`](scripts/scaffold_lesson.py)

Ví dụ inspection:

```bash
python scripts/scaffold_lesson.py --lesson 0.2 --effort M --minutes 60 --prerequisite 0.1 --dry-run
```

Status contract:

```text
planned = scaffold/chưa authored
draft   = đang author
ready   = nội dung đủ để học

PASS/RETRY = kết quả người học, không phải authoring status
```

Lesson `ready` phải có đủ:

1. Concept
2. Example / case
3. Quiz ≥80% + answer key/rubric
4. Practice artifact
5. Explain-back

## 5. Source refs và current facts

Mọi lesson phải có canonical `S:` ref. `T:` và `R:` chỉ thêm khi nguồn thực sự hỗ trợ nội dung.

Với claim hiện hành về platform policy, attribution, commission, API, legal, tax, privacy, AIGC, Go runtime, MCP, workflow engine, SDK hoặc software behavior có thể thay đổi, author phải external-verify tại thời điểm viết.

Metadata contract:

```yaml
source_refs:
  external:
    - "EXT:<provider>:<topic>"
last_verified: "YYYY-MM-DD"
```

- external refs → bắt buộc `last_verified`;
- `last_verified` → bắt buộc external refs;
- ưu tiên official/government/primary source;
- không hard-code current library/runtime version thành permanent curriculum truth.

## 6. Artifact/evidence

Tuân theo [`artifacts/README.md`](artifacts/README.md).

Không commit:

- API key, token, password;
- dữ liệu cá nhân nhạy cảm;
- credential;
- raw export chứa thông tin không cần thiết;
- nội dung không có quyền phân phối.

Artifact tồn tại không tự động đồng nghĩa PASS.

## 7. Pull request checklist

Trước PR:

```bash
python scripts/validate_curriculum.py
python -m unittest discover -s tests -v
```

Checklist:

- [ ] Active canonical vẫn là v2026.09 và historical v2026.08 còn nguyên provenance.
- [ ] Không drift 23 Part / 89 Chapter / 671 lesson / 14 projects.
- [ ] Active Part 15 vẫn Go-first; không tái đưa C#/.NET-specific framework vào primary path.
- [ ] Part files vẫn dùng normalized `Timeline:` metadata.
- [ ] Không duplicate/gap lesson ID.
- [ ] Relative links hoạt động.
- [ ] Lesson metadata/path/source ref khớp.
- [ ] External refs ↔ `last_verified` đúng contract.
- [ ] `planned` không link như authored lesson; `draft|ready` phải link.
- [ ] Không tick learner checkbox chỉ vì file tồn tại.
- [ ] Current facts đã external-verify khi cần.
- [ ] Bot side effects có risk/policy/approval boundary nếu relevant.
- [ ] Không làm mất answer key/rubric/PASS evidence contract.

## 8. Reference implementations

- [`0.1 — Affiliate Expert là gì?`](lessons/part-00/chapter-00/0.1-affiliate-expert-la-gi.md) — general ready-lesson reference.
- `0.2 — Affiliate Bot Engineer là gì?` sẽ trở thành Go-first Bot Engineer reference sau migration PR4.

Không yêu cầu mọi lesson dài bằng 0.1/0.2. Depth phải phù hợp effort S/M/L.

## 9. Licensing

Repo hiện **không cấp open-source license** cho curriculum/content.

Repository public không tự động cấp quyền sao chép, sửa đổi, tái phân phối hoặc thương mại hóa nội dung. Xem [`docs/LICENSING.md`](docs/LICENSING.md).
