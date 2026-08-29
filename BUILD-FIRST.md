# Lộ trình học Build-First

> **BẮT ĐẦU TỪ ĐÂY.** Đây là đường học mặc định của curriculum v2026.09.

## Mô hình tư duy

```text
Build (Xây)
→ Run (Chạy)
→ Observe (Quan sát)
→ Pull Knowledge just-in-time (Lấy kiến thức đúng lúc)
→ Improve (Cải tiến)
→ Test (Kiểm thử)
→ Operate (Vận hành)
→ Save Evidence (Lưu bằng chứng)
→ Ship next Bot Version (Bàn giao phiên bản Bot tiếp theo)
```

Từ M00–M06, software loop chạy song song với **Manual Affiliate Loop**:

```text
Observe business manually
→ Record evidence + provenance
→ Make human judgment
→ Compare with Bot
→ Find disagreement / uncertainty
→ Improve data or model
```

Xem [`docs/MANUAL-AFFILIATE-LOOP.md`](docs/MANUAL-AFFILIATE-LOOP.md). Lane này tạo business grounding sớm nhưng **không cấp execution authority sớm cho Bot**.

`ROADMAP.md` và 23 file Part vẫn là **canonical knowledge inventory (kho kiến thức chuẩn hóa)** gồm 23 Parts / 89 Chapters / 671 lessons. Build-First không đổi số thứ tự, không xóa lesson và không thay learner PASS; nó chỉ thay **thứ tự thực thi việc học**.

## Lộ trình tiến hóa của Bot

| Mission | Bot Version (Phiên bản Bot) | Ship target (Mục tiêu bàn giao) | AI level |
|---|---:|---|---|
| M00 | v0.0 | Bot khởi động và có output quan sát được | A0 |
| M01 | v0.1 | Product ingest (đọc dữ liệu sản phẩm) | A0 |
| M02 | v0.2 | Product store + history (lưu trữ + lịch sử) | A0 |
| M03 | v0.3 | Product ranking (xếp hạng sản phẩm) đầu tiên | A0 |
| M04 | v0.4 | Product watcher (theo dõi thay đổi) | A0 |
| M05 | v0.5 | Reliable alerts + AI advisory triage | A1 |
| M06 | v1.0 | Product Intelligence + AI product research | A1 |
| M07 | v2.0 | Content Intelligence | A1 |
| M08 | v3.0 | Revenue & Attribution Intelligence + investigation | A1 |
| M09 | v4.0 | Experiment Engine + AI experiment copilot | A1 |
| M10 | v5.0 | Decision Intelligence & Policy Engine | A1 |
| M11 | v6.0 | AI Analysis Assistant + model routing/evaluation | A2 |
| M12 | v7.0 | Tool-Using Agent / MCP | A2 |
| M13 | v8.0 | Governed Automation | A3 |
| M14 | v9.0 | Production Agentic Bot | A3 |
| M15 | v10.0 | Affiliate Intelligence Platform | A4 optional |

Xem chi tiết tại [`docs/BOT-EVOLUTION-ROADMAP.md`](docs/BOT-EVOLUTION-ROADMAP.md). Bản đồ kiến thức đúng lúc nằm tại [`docs/MISSION-KNOWLEDGE-MAP.md`](docs/MISSION-KNOWLEDGE-MAP.md).

## Bốn loại đơn vị

- **Lesson (Bài học)** — một đơn vị kiến thức trong canonical curriculum.
- **Mission (Nhiệm vụ thực hành)** — một đơn vị build/run/operate có mục tiêu bàn giao cụ thể.
- **Project (Dự án)** — một trong 14 mốc tích hợp chuẩn của curriculum.
- **Bot Version (Phiên bản Bot)** — trạng thái sản phẩm sau mỗi Mission.

```text
Mission ≠ Lesson ≠ Project ≠ Bot Version
```

## Workspace học thật và bản tham chiếu

Người học làm việc tại:

```text
lab/learner/affiliate-bot/
```

Bản triển khai tham chiếu hiện tại nằm tại:

```text
lab/affiliate-bot/
```

Quy tắc mặc định:

```text
TỰ THỬ BUILD
→ RUN / OBSERVE
→ PULL KNOWLEDGE
→ FIX / TEST
→ chỉ mở reference (bản tham chiếu) khi cần đối chiếu hoặc sau khi đã có attempt (lần thử)
```

Mục tiêu là tự tạo progression (tiến trình) M00 → M03, không đọc sẵn lời giải v0.3 rồi coi đó là học Build-First.

## Quy tắc học mặc định

1. Mở Mission hiện tại trong `PROGRESS.md`.
2. Build phần nhỏ nhất chạy được trong learner workspace.
3. Chạy và quan sát lỗi, thiếu sót hoặc assumption (giả định) bị sai.
4. Pull đúng knowledge slice (phần kiến thức cần ngay) từ Mission/knowledge map.
5. Áp dụng kiến thức vào Bot.
6. Test happy path (luồng đúng) và failure case (tình huống lỗi) phù hợp scope.
7. Chạy/operate đủ để quan sát output.
8. Lưu evidence (bằng chứng) và explain-back (giải thích lại bằng lời của mình).
9. Với M00–M06, thực hiện manual-business slice tương ứng và so human judgment với Bot khi Mission có decision/ranking.
10. Chỉ PASS Mission khi ship target thực sự đạt.

## Go từ ngày đầu, mastery đến sau

Build-First dùng Go ngay từ M00. Điều đó **không** có nghĩa learner đã mastery (làm chủ) Part 15.

```text
USE GO EARLY (dùng Go sớm)
≠
CLAIM GO MASTERY EARLY (tuyên bố làm chủ Go sớm)
```

Go concepts (khái niệm Go) được lấy đúng lúc: package/function ở M00; struct/JSON/error/validation ở M01; database/repository ở M02; context/concurrency khi làm scheduler; retry/idempotency khi làm reliability.

## Viết code sớm không đồng nghĩa tự động hóa kinh doanh thật sớm

```text
BUILD CODE EARLY (viết code sớm)
≠
AUTOMATE REAL BUSINESS EARLY (tự động hóa hoạt động kinh doanh thật quá sớm)
```

M00–M03 dùng dữ liệu mẫu/local và không có external side effect (tác động bên ngoài). Không publish nội dung, không tiêu tiền, không thay đổi tài khoản và không gọi hành động có hậu quả trên platform.

Manual Affiliate Loop có thể dùng public/read-only observations để learner hiểu business signal, nhưng observation không phải permission để Bot hành động.

## AI xuất hiện sớm nhưng authority tăng dần

Build-First dùng AI từ M05 ở vai trò **A1 advisory/read-only (tư vấn/chỉ đọc)**, nhưng không đưa execution authority lên sớm.

```text
A0 — deterministic only
A1 — AI advisory/read-only
A2 — tool-assisted agent
A3 — governed action agent
A4 — optional multi-agent tại M15
```

```text
AI APPEARS EARLY
≠
AI GETS AUTHORITY EARLY
```

Luồng Decision Intelligence chuẩn:

```text
EVENT / DATA
→ Freshness + Quality Gate
→ Deterministic Analytics / Forecast / ML
→ AI Analysis
→ Decision Fusion
→ DecisionPacket
→ Policy + Risk
→ Auto hoặc Human Approval
→ Action
→ Outcome
→ Evaluation / Learn
↺
```

Chi tiết:

- [`docs/AI-AGENT-DECISION-ARCHITECTURE.md`](docs/AI-AGENT-DECISION-ARCHITECTURE.md)
- [`docs/AI-CAPABILITY-LEVELS.md`](docs/AI-CAPABILITY-LEVELS.md)
- [`docs/DECISION-CONTRACTS.md`](docs/DECISION-CONTRACTS.md)
- [`docs/AI-PROVIDER-CAPABILITY-MATRIX.md`](docs/AI-PROVIDER-CAPABILITY-MATRIX.md)

## Safety / Autonomy (An toàn / Tự chủ)

```text
Deterministic logic (logic xác định) trước LLM autonomy (tự chủ bằng LLM)
Decision (quyết định) ≠ Execution (thực thi)
Model output (đầu ra mô hình) = untrusted input (đầu vào không được tin cậy mặc định)
RISK 0 → auto (tự chạy)
RISK 1 → auto + audit (tự chạy + ghi vết)
RISK 2 → Human Approval (phê duyệt của con người)
```

AI analysis có thể tạo `AnalysisPacket` hoặc đề xuất `DecisionPacket`, nhưng external execution luôn phải đi qua Policy/Risk boundary.

## Knowledge mastery (Làm chủ kiến thức) vẫn tồn tại

Lesson PASS vẫn theo `docs/PASS-CRITERIA.md`. Mission PASS theo [`docs/MISSION-PASS-CRITERIA.md`](docs/MISSION-PASS-CRITERIA.md). Hoàn thành Mission **không được tự động tick Lesson PASS**.

Một Mission chỉ yêu cầu learner hiểu **phần kiến thức đủ để giải thích implementation (cách triển khai) hiện tại**; full lesson PASS vẫn là một evidence gate (cổng bằng chứng) độc lập.

## Trạng thái bootstrap hiện tại

M00–M03 đã được author ở trạng thái `ready` trong `missions/`.

- learner workspace bắt đầu ở M00 với capability tối thiểu;
- reference implementation hiện tương đương v0.3 để đối chiếu;
- M04–M15 mới là roadmap targets và chưa có file Mission `ready`.

Việc thêm AI architecture hoặc Manual Affiliate Loop không auto-author M04–M15 và không thay learner progress hiện tại.

## Quy chuẩn ngôn ngữ

Tiếng Việt là ngôn ngữ chính thức của repository. Tiếng Anh chỉ giữ cho thuật ngữ chuyên ngành, tên công nghệ/protocol và identifier, kèm giải thích tiếng Việt khi cần. Xem [`docs/LANGUAGE-POLICY.md`](docs/LANGUAGE-POLICY.md).