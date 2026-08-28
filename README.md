# Affiliate Expert Learning Roadmap

**Xây Affiliate Intelligence Bot (Bot trí tuệ Affiliate) trong khi học Affiliate, Data, Engineering và AI theo kiểu just-in-time (đúng lúc cần).**

```text
Affiliate Expert (Chuyên gia Affiliate)
+
Affiliate Bot Engineer (Kỹ sư Bot Affiliate)
=
Affiliate Intelligence Expert (Chuyên gia Affiliate Intelligence)
```

## BẮT ĐẦU TỪ ĐÂY — Build-First

Đường học mặc định là [`BUILD-FIRST.md`](BUILD-FIRST.md).

```text
Build (Xây)
→ Run (Chạy)
→ Observe (Quan sát)
→ Pull Knowledge (Lấy kiến thức cần ngay)
→ Improve (Cải tiến)
→ Test (Kiểm thử)
→ Operate (Vận hành)
→ Evidence (Bằng chứng)
→ Next Bot Version (Phiên bản Bot tiếp theo)
```

Điều này **không** có nghĩa xóa curriculum kiến thức. [`ROADMAP.md`](ROADMAP.md) vẫn là normalized canonical knowledge inventory (kho kiến thức chuẩn hóa).

## Authority (nguồn có thẩm quyền) của curriculum

- **Active canonical (bản chuẩn hiện hành):** `sources/SYLLABUS-v2026.09.md`
- **Historical baseline (mốc lịch sử):** `sources/SYLLABUS-v2026.08.md`
- **Knowledge inventory (kho kiến thức):** 23 Parts · 89 Chapters · 671 lessons
- **Main Projects (dự án chính):** 14
- **Ngôn ngữ triển khai Bot chính:** Go
- **Standard capacity (nhịp chuẩn):** ~9h/tuần · planning envelope (khung kế hoạch) 15 tháng
- **Accelerated (tăng tốc):** ~11–12h/tuần · planning envelope 12 tháng

Mô hình source/provenance (nguồn gốc nội dung) nằm ở [`sources/CURRICULUM-INDEX-v2026.09.md`](sources/CURRICULUM-INDEX-v2026.09.md).

## Hai lớp của chương trình

```text
SYLLABUS / ROADMAP
= NHỮNG GÌ CUỐI CÙNG PHẢI BIẾT

BUILD-FIRST
= TIẾP THEO CẦN XÂY GÌ
```

- **Lesson (Bài học)** là đơn vị kiến thức.
- **Mission (Nhiệm vụ thực hành)** là đơn vị build/run/operate.
- **Project (Dự án)** là một trong 14 integration milestones (mốc tích hợp) chuẩn.
- **Bot Version (Phiên bản Bot)** là trạng thái sản phẩm.

```text
Mission ≠ Lesson ≠ Project ≠ Bot Version
```

Xem [`docs/BUILD-FIRST-LEARNING-MODEL.md`](docs/BUILD-FIRST-LEARNING-MODEL.md).

## Workspace của người học và bản tham chiếu

Người học trực tiếp sửa:

```text
lab/learner/affiliate-bot/
```

Reference implementation (bản triển khai tham chiếu) hiện tại:

```text
lab/affiliate-bot/
```

Learner workspace bắt đầu từ M00 tối giản và **không có sẵn M01–M03 capability (năng lực)**. Bản tham chiếu chỉ dùng để đối chiếu sau khi đã tự thử hoặc khi bị kẹt.

## Go từ đầu, mastery (làm chủ) đến sau

Build-First dùng đủ Go để chạy Bot ngay từ M00. Formal Bot Engineering mastery (làm chủ kỹ thuật Bot chính thức) vẫn thuộc phạm vi evidence (bằng chứng) rộng hơn của Part 15+.

```text
USE GO EARLY (dùng Go sớm)
≠
CLAIM GO MASTERY EARLY (tuyên bố làm chủ Go sớm)
```

Chuẩn Go-first vẫn nằm ở:

- [`docs/ADR-001-GO-FIRST-BOT-STACK.md`](docs/ADR-001-GO-FIRST-BOT-STACK.md)
- [`docs/GO-BOT-ENGINEERING-STACK.md`](docs/GO-BOT-ENGINEERING-STACK.md)
- [`docs/AUTONOMY-AND-APPROVAL-MODEL.md`](docs/AUTONOMY-AND-APPROVAL-MODEL.md)
- [`docs/AGENT-SECURITY-AND-TOOL-GOVERNANCE.md`](docs/AGENT-SECURITY-AND-TOOL-GOVERNANCE.md)

## Viết code sớm không đồng nghĩa tự động hóa kinh doanh thật sớm

```text
BUILD CODE EARLY (viết code sớm)
≠
AUTOMATE REAL BUSINESS EARLY (tự động hóa hoạt động kinh doanh thật quá sớm)
```

M00–M03 dùng sample/local data (dữ liệu mẫu/cục bộ), không publish, không tiêu tiền, không thay đổi tài khoản và không tạo external side effect (tác động bên ngoài) có hậu quả.

## Safety & Governed Autonomy (An toàn & Tự chủ có kiểm soát)

```text
Deterministic Logic (logic xác định) trước LLM autonomy (tự chủ bằng LLM)
Decision (quyết định) ≠ Execution (thực thi)
Model Output (đầu ra mô hình) = Untrusted Input (đầu vào không được tin mặc định)

RISK 0 → auto execute (tự chạy)
RISK 1 → auto execute + audit (tự chạy + ghi vết)
RISK 2 → persist → Human Approval (phê duyệt con người) → revalidate → execute/reject
```

## Knowledge PASS và product progress (tiến độ sản phẩm)

Authoring state (trạng thái nội dung) và learner state (trạng thái người học) độc lập:

```text
Authoring: planned → draft → ready
Learner:   chưa PASS → PASS / RETRY
```

Bot chạy được hoặc Mission PASS không được tự động đánh dấu Lesson PASS. Tiêu chí Lesson hiện tại nằm ở [`docs/PASS-CRITERIA.md`](docs/PASS-CRITERIA.md).

## Current knowledge layer (lớp kiến thức hiện hành)

Các fact (dữ kiện) platform/software/legal có thể thay đổi được tách khỏi cấu trúc canonical ổn định:

- [`docs/FRESHNESS-POLICY.md`](docs/FRESHNESS-POLICY.md)
- [`docs/AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md`](docs/AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md)
- [`docs/BOT-ENGINEERING-REFRESH-2026.08.md`](docs/BOT-ENGINEERING-REFRESH-2026.08.md)

## Tài liệu chính

- [Build-First Roadmap](BUILD-FIRST.md) — điểm vào mặc định của người học
- [Knowledge Roadmap](ROADMAP.md) — kho lesson chuẩn hóa
- [Progress Dashboard](PROGRESS.md) — bảng tiến độ
- [Execution Model](docs/EXECUTION-MODEL.md) — mô hình thực thi
- [Build-First Learning Model](docs/BUILD-FIRST-LEARNING-MODEL.md) — mô hình học Build-First
- [Projects](docs/PROJECTS.md) — hệ thống Project
- [15-Month Plan](docs/15-MONTH-PLAN.md) — kế hoạch chuẩn
- [12-Month Plan](docs/12-MONTH-PLAN.md) — kế hoạch tăng tốc
- [Curriculum CI](docs/CURRICULUM-CI.md) — kiểm tra tự động
- [Glossary VI](docs/GLOSSARY-VI.md) — bảng thuật ngữ
- [Language Policy](docs/LANGUAGE-POLICY.md) — quy chuẩn tiếng Việt

## Nguyên tắc cốt lõi

```text
BUILD → RUN → OBSERVE → LEARN → FIX → TEST → OPERATE → MEASURE
UNDERSTAND → DECIDE → EXECUTE → MEASURE → LEARN → IMPROVE
```

- **DATA > OPINION** — Dữ liệu quan trọng hơn ý kiến.
- **EXPECTED VALUE > COMMISSION RATE** — Giá trị kỳ vọng quan trọng hơn tỷ lệ hoa hồng đơn lẻ.
- Không automate (tự động hóa) thứ mình chưa hiểu thủ công.
- Không optimize (tối ưu) trước khi đo.
- Deterministic logic trước LLM autonomy.
- High-risk action (hành động rủi ro cao) phải qua policy/risk control (kiểm soát chính sách/rủi ro) và Human Approval khi cần.

## Quy chuẩn ngôn ngữ

**Tiếng Việt là ngôn ngữ chính thức của repository.** Tiếng Anh chỉ giữ cho thuật ngữ chuyên ngành, tên công nghệ/protocol và identifier, kèm nội dung tiếng Việt giải thích khi cần. Xem [`docs/LANGUAGE-POLICY.md`](docs/LANGUAGE-POLICY.md).

## Contribution model (mô hình đóng góp)

Repository tiếp tục theo issue-first (mở Issue trước cho thay đổi cấu trúc/thực thi). Đọc [`CONTRIBUTING.md`](CONTRIBUTING.md) trước khi thay đổi execution model.

`ready` nghĩa là nội dung đã được author đủ để học; **không** có nghĩa learner đã PASS.