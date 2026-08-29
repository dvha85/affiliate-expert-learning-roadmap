# Build-First Execution Model — Mô hình thực thi Build-First

> Curriculum v2026.09 dùng **Mission-first execution (thực thi theo Mission) + just-in-time knowledge pulls (lấy kiến thức đúng lúc) + persistent operating loops (các vòng vận hành được duy trì)**.

## 1. Mental Model — Mô hình tư duy

```text
                 BUILD-FIRST SPINE
                 (Xương sống Build-First)

Mission M00 → M01 → M02 → M03 → ...
    │          │      │
    ▼          ▼      ▼
Knowledge   Knowledge Knowledge
  Pull        Pull      Pull
    │          │        │
    └──────────┴────────┘
             ↓
        Bot Version evolves
        (Phiên bản Bot tiến hóa)
```

`ROADMAP.md` vẫn là canonical knowledge inventory (kho kiến thức chuẩn). Mission system quyết định learner build gì tiếp theo; knowledge dependencies quyết định learner phải hiểu **knowledge slice (phần kiến thức cần thiết)** nào để Mission PASS.

## 2. Build-First Loop — Vòng học Build-First

```text
Ship Target (Mục tiêu bàn giao)
→ Build smallest working slice (Xây phần nhỏ nhất chạy được)
→ Run (Chạy)
→ Observe failure/gap (Quan sát lỗi/thiếu sót)
→ Pull required knowledge (Lấy kiến thức cần ngay)
→ Improve (Cải tiến)
→ Test (Kiểm thử)
→ Operate (Vận hành)
→ Measure (Đo lường)
→ Explain (Giải thích)
→ Save evidence (Lưu bằng chứng)
→ Next Bot Version (Phiên bản Bot tiếp theo)
```

Learner không chờ tới Part 15 mới chạm Go. Mission đầu dùng Go scope hẹp; Part 15 vẫn là formal Bot Engineering mastery (phạm vi làm chủ Bot Engineering chính thức).

## 3. Knowledge Dependency Semantics — Ý nghĩa quan hệ kiến thức

Mission knowledge có ba mức:

- **REQUIRED (Bắt buộc cho Mission)** — phải hiểu phần cần thiết để Mission PASS.
- **ON-DEMAND (Khi phát sinh nhu cầu)** — pull khi implementation/business context làm lộ nhu cầu.
- **REFERENCE (Tham khảo)** — kiến thức đào sâu, không phải Mission PASS gate.

```text
REQUIRED FOR MISSION
≠
FULL LESSON PASS
```

Mission completion không bao giờ tự đánh dấu Lesson PASS.

## 4. Operating Loops Remain Cumulative — Các vòng vận hành được tích lũy

Khi capability (năng lực) tăng, các loop sau tiếp tục chạy khi relevant:

- Compliance / Platform Watch — theo dõi tuân thủ/nền tảng;
- Market / Customer / Product Watch — theo dõi thị trường/khách hàng/sản phẩm;
- Content Production — sản xuất nội dung;
- Traffic Distribution — phân phối traffic;
- Funnel / Revenue / Data Capture — ghi nhận funnel/doanh thu/dữ liệu;
- Experiment Loop — vòng thử nghiệm;
- Bot / Automation — Bot/tự động hóa;
- AI-assisted Workflow — workflow có AI hỗ trợ;
- Governed Action / Approval — hành động/phê duyệt có kiểm soát.

Build-First thay **thời điểm capability được đưa vào**, không xóa yêu cầu giữ các operating loop hữu ích.

## 5. Decision Intelligence Loop — Vòng trí tuệ quyết định

Từ M05, AI có thể xuất hiện ở vai trò advisory/read-only nhưng authority tăng dần theo `docs/AI-CAPABILITY-LEVELS.md`.

```text
Event / Data
→ Freshness + Quality Gate
→ SignalPacket
→ Deterministic Analytics / Forecast / ML
→ AI AnalysisPacket khi có giá trị
→ Evidence Escalation nếu thiếu dữ liệu
→ Decision Fusion
→ DecisionPacket
→ Policy + Risk
→ ActionIntent
→ Auto hoặc Human Approval
→ Execute
→ Outcome
→ Evaluation / Learning
↺
```

Bốn state/contract phải tách biệt:

```text
Signal / Fact
≠
Analysis
≠
Decision
≠
Execution Record
```

Điều này cho phép audit rõ hệ thống đã thấy gì, AI/rule đã phân tích gì, quyết định nào được chọn và executor thực sự đã làm gì.

## 6. Event-driven Invocation — Chỉ gọi AI khi có trigger đáng giá

Không mặc định poll toàn bộ dữ liệu rồi hỏi LLM liên tục.

Ưu tiên trigger như:

- material state change;
- anomaly;
- threshold crossing;
- freshness expiry;
- experiment completion;
- revenue reconciliation;
- approval completion;
- policy/platform change.

```text
DETERMINISTIC EVENT
→ IS IT MATERIAL?
→ YES: collect evidence + run analysis/decision workflow
```

Mục tiêu là phản ứng nhanh hơn khi có thay đổi thật, đồng thời giảm model cost và noise.

## 7. AI Capability Progression — Tiến trình quyền AI

```text
A0 — deterministic only              M00–M04
A1 — AI advisory/read-only           M05–M10
A2 — tool-assisted Agent             M11–M12
A3 — governed action Agent           M13–M14
A4 — optional multi-agent            M15
```

```text
AI APPEARS EARLY
≠
AI GETS AUTHORITY EARLY
```

Ở A1, AI được phân tích/đề xuất nhưng không external execute. Ở A2+, tool permission/risk/approval contract vẫn là bắt buộc.

## 8. Governed Action / Approval — Hành động và phê duyệt có kiểm soát

Consequential execution (thực thi có hậu quả đáng kể) giữ policy model hiện hành:

```text
Observe (Quan sát)
→ Analyze (Phân tích)
→ DecisionPacket / ActionIntent
→ deterministic Policy + Risk (Chính sách + Rủi ro xác định)
   ├── RISK 0 → auto execute (tự thực thi)
   ├── RISK 1 → auto execute + mandatory audit (tự thực thi + bắt buộc ghi vết)
   └── RISK 2 → persist → approval → revalidate → execute/reject
→ Audit / Trace (Ghi vết)
→ Measure outcome (Đo kết quả)
→ Learn (Học)
```

Human review dùng cho consequential decisions/exceptions, không dùng để babysit từng bước cơ học.

## 9. Evidence Escalation — Thiếu dữ liệu thì lấy thêm, không đoán

```text
Enough evidence?
├─ YES → DecisionPacket
└─ NO
   → request allowed read tools/data
   → collect more evidence
   → reevaluate
```

`WAIT`, `GET_MORE_DATA`, `HUMAN_REVIEW` là decision hợp lệ. AI phải thể hiện `missing_evidence` và `uncertainty` thay vì tạo certainty giả.

## 10. Go-First Progression — Tiến trình Go-first

```text
Early Missions (Mission đầu)
→ dùng Go tối thiểu để ship

Later Missions (Mission sau)
→ database / concurrency / reliability / workflow

Part 15+ mastery
→ engineering evidence rộng hơn + Project integration
```

Đây là chủ ý **USE BEFORE MASTER (dùng trước, làm chủ sau)**, không phải mastery-by-copying (làm chủ bằng cách copy lời giải).

Learner workspace và reference implementation phải tách nhau để progression này có ý nghĩa.

## 11. Provider-Neutral AI — AI trung lập nhà cung cấp

Go domain/Decision/Policy core không phụ thuộc trực tiếp provider SDK.

```text
Go Domain / Decision / Policy
→ AI Provider Interface
→ Provider Adapter
```

Provider capability được đánh giá theo `docs/AI-PROVIDER-CAPABILITY-MATRIX.md`. Exact model/API/version thuộc freshness layer.

## 12. Capacity — Quỹ thời gian

- Standard: khoảng 9h/tuần.
- Accelerated: khoảng 11–12h/tuần.

Heuristic (gợi ý) trong Build-First:

```text
50–70% build / run / debug / operate
20–30% required knowledge pull
10–20% evidence / review
```

Tỷ lệ có thể adaptive; không hạ PASS quality chỉ để đạt ngày trên lịch.

## 13. Capstone Evolution — Tiến hóa tới Capstone

```text
Runnable Go Bot
→ Product Data
→ Product Watcher
→ Product Intelligence
→ Content / Revenue Intelligence
→ Experiment Engine
→ Decision Intelligence / Policy Engine
→ AI Tool Workflow
→ Governed Production Bot
→ Affiliate Intelligence Platform
```

Project artifact nên tiến hóa và reuse, không rebuild toàn bộ từ đầu ở mỗi Project.

## 14. Final Operating Rule — Quy tắc vận hành cuối cùng

```text
ONE current Mission
+
ONLY necessary Knowledge Pulls
+
ACTIVE operating loops within capacity
+
PASS evidence before mastery claim
+
EVIDENCE before AI confidence
+
POLICY before consequential execution
```

## 15. Quy tắc code sớm

```text
BUILD CODE EARLY
≠
AUTOMATE REAL BUSINESS EARLY
```

Mission đầu dùng sample/local data và side effect thấp để learner học bằng thực hành mà không vượt quá mức hiểu biết hoặc policy boundary.