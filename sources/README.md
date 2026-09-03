# Tài liệu nguồn và archive

Thư mục `sources/` là **historical/research archive**, không phải nguồn chuẩn vận hành.

## Authority hiện hành

Chỉ có một chuỗi authority cho learner/runtime work mới:

1. [`../CURRICULUM.md`](../CURRICULUM.md) — outcome, sequence, evidence, authority và PASS boundary;
2. [`../ROADMAP.md`](../ROADMAP.md) — projection learner-facing của curriculum hiện hành;
3. active Mission/lesson files được curriculum hiện hành tham chiếu;
4. ADR/operating standards — chi tiết kiến trúc, safety và quality;
5. `sources/` — provenance, nghiên cứu và lịch sử thiết kế.

Nếu nội dung trong `sources/` mâu thuẫn với curriculum hiện hành, **curriculum hiện hành thắng**.

## Archive trước curriculum reset

Snapshot trước đợt reset ngày 2026-09-03 được giữ tại nhánh:

```text
archive/pre-curriculum-reset-2026-09-03
```

Dùng snapshot/Git history khi cần xem nguyên văn các syllabus, lesson hoặc migration mapping cũ. Không đưa chúng trở lại learner path chỉ để giữ compatibility.

## Các nguồn lịch sử

- `SYLLABUS-v2026.08.md` — structural baseline lịch sử;
- `SYLLABUS-v2026.09.md` — archival stub cho revision Go-first trước reset;
- `CURRICULUM-INDEX-v2026.09.md` — archival stub cho inventory cũ;
- `Noi-dung-dao-tao.txt` — nguồn đào tạo;
- `Nghien-cuu.txt` — nguồn nghiên cứu.

Các con số 23 Parts / 89 Chapters / 671 lessons / 14 projects là **historical inventory**, không mô tả chương trình hiện hành.

## Quy tắc công nghệ

Không source historical nào được quyết định rằng Go, n8n, Agent SDK, rule engine hay framework cụ thể là prerequisite chỉ vì revision cũ từng chọn nó.

Curriculum hiện hành giữ nguyên tắc:

```text
DETERMINISTIC CORE FIRST
!= CODE FIRST

implementation is chosen by auditability, safety, evidence and measured need
```

Go có thể là deterministic reference/fallback; n8n có thể là orchestration reference; Agent runtime có thể cung cấp intelligence. Không runtime nào tự sở hữu truth, policy hoặc execution authority chỉ vì được chọn làm implementation.

## Dữ kiện dễ thay đổi

Platform policy, pháp luật, privacy, attribution, SDK/protocol và software version phải đi qua freshness layer ở `docs/`, không được lấy từ syllabus lịch sử làm operating truth.

Nguyên tắc cuối cùng:

> **Một nguồn chuẩn hiện hành. Lịch sử giữ ở archive. Dữ kiện hiện hành phải kiểm chứng được.**
