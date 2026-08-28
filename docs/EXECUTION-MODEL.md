# Hybrid Execution Model

> Curriculum dùng **sequential knowledge prerequisites + parallel execution loops** theo active curriculum v2026.09.

## 1. Mental model

```text
                    KNOWLEDGE SPINE

Orientation → Foundation/Economics/Tracking
            → Market/Customer/Product
            → Content/Traffic/Funnel
            → Data/Analytics/Experiment
            → Bot/Decision/AI
            → Advanced/Production
            → Capstone

                         │
                         │ unlocks
                         ↓

              PARALLEL EXECUTION LOOPS

Compliance / Platform Watch ────────────────────→
Market / Product Watch ─────────────────────────→
Content Production ─────────────────────────────→
Traffic Distribution ───────────────────────────→
Tracking / Funnel / Data Capture ───────────────→
Experiment Loop ────────────────────────────────→
Bot / Automation Loop ──────────────────────────→
AI-assisted Workflow ───────────────────────────→
Governed Action / Approval Loop ────────────────→
```

**Knowledge spine** trả lời: cần hiểu gì trước khi học concept tiếp theo.  
**Execution loop** trả lời: hoạt động thực tế nào đã mở khóa và phải tiếp tục tạo evidence.

## 2. Hai loại dependency

### Minimum prerequisite

Knowledge tối thiểu phải có trước khi bắt đầu Part/lesson. Nếu thiếu, implementation dễ trở thành làm theo mà không hiểu business logic.

### Recommended context

Kiến thức nên có nhưng có thể overlap nếu capacity phù hợp. Không phải hard gate.

Không dùng dependency để biến toàn bộ curriculum thành tuyến tính tuyệt đối.

## 3. Dependency map cho 23 Part

| Part | Trọng tâm | Minimum prerequisite | Unlock chính |
|---:|---|---|---|
| 0 | Orientation & Affiliate Lab | — | learning/evidence system |
| 1 | Affiliate Fundamentals | Part 0 baseline | ecosystem/business vocabulary |
| 2 | Affiliate Economics | Part 1 | revenue/economic decision lens |
| 3 | Tracking & Attribution | Part 1 | tracking/data capture |
| 4 | Legal, Tax & Compliance | Part 1 | Compliance Watch |
| 5 | Platform Expert | Part 1 + Parts 3–4 context | Platform Policy Watch |
| 6 | Market & Niche | Parts 1–2 | Market/Niche Watch |
| 7 | Customer Intelligence | Part 6 baseline | customer research |
| 8 | Product Intelligence | Parts 2,6,7 | Product Watch/scoring evidence |
| 9 | Content & Psychology | Parts 7–8 + compliance context | Real Content Production |
| 10 | Traffic & Distribution | Part 9 | Traffic Distribution |
| 11 | Funnel & Conversion | Parts 2–3 + 9–10 baseline | Funnel/Revenue Measurement |
| 12 | Data Engineering | Parts 3,8,11 | structured historical data |
| 13 | Analytics | Parts 2,11,12 | diagnostic analytics |
| 14 | Experimentation | Part 13 | Formal Experiment Loop |
| 15 | Bot Engineering | Parts 12–13; Part14 useful | Bot/Automation Loop |
| 16 | Decision & Recommendation | Parts 8,13–15 | deterministic decision/policy |
| 17 | AI Affiliate Bot | Parts 9,15–16 | AI-assisted workflow + approval |
| 18 | Advanced Intelligence | Parts 13–14,16 | forecasting/adaptive decision models |
| 19 | Production/Security/Automation | Parts 15,17 | reliable governed production action |
| 20 | Business & Scale | revenue signal + relevant loops | management by exception / scale |
| 21 | Capstone | core deliverables Parts 0–19 | integrated intelligence platform |
| 22 | Continuous Mastery | formal mastery after Part 21 | continuous watch/research cycle |

`baseline` không mặc định nghĩa là mọi lesson trước đó đều PASS; lesson-level prerequisites có thể hẹp hơn khi được author.

## 4. Execution loops

### Loop A — Compliance & Platform Watch

**Mở:** Parts 4–5.

```text
Policy/legal change
→ impact analysis
→ required action
→ update workflow/content/bot
→ evidence/change log
```

### Loop B — Market / Customer / Product Watch

**Mở:** Parts 6–8. Market, customer và product là state thay đổi, không phải snapshot một lần.

### Loop C — Real Content Production

**Mở:** Part 9 foundation.

```text
Create → Publish → Measure → Learn → next version
```

### Loop D — Traffic Distribution

**Mở:** Part 10 foundation. Traffic bổ sung cho Content, không thay thế Content.

### Loop E — Funnel / Revenue / Data Capture

Tracking thinking bắt đầu Part 3; operational funnel measurement mở đầy đủ ở Part 11 và tiếp tục cung cấp dữ liệu cho Parts 12–18.

### Loop F — Formal Experiments

**Mở:** Part 14.

```text
Hypothesis → Experiment → Measure → Decision → Learning backlog
```

### Loop G — Bot / Automation

**Mở:** Part 15.

```text
manual understanding
→ deterministic Go implementation
→ reliable pipeline
→ automation
```

Giữ rule: **không automate thứ chưa hiểu bằng tay**.

### Loop H — AI-assisted Workflow

**Mở:** Part 17.

AI có thể draft/analyze/recommend/use tools, nhưng không thay evidence, policy hoặc authorization boundary.

### Loop I — Governed Action / Approval

**Mở dần:** deterministic policy từ Part 16; HITL/action intents ở Part 17; production hardening ở Part 19.

```text
Observe
→ Analyze
→ Recommend / ActionIntent
→ deterministic Policy + Risk
   ├── RISK 0 → auto execute
   ├── RISK 1 → auto execute + mandatory audit
   └── RISK 2 → persist → approval → revalidate → execute/reject
→ Audit / Trace
→ Measure outcome
→ Learn
```

Loop này là end-state vận hành: human review **consequential decisions/exceptions**, không babysit từng bước cơ học.

## 5. Part 9 → 10 → 11

Sai:

```text
xong Content → dừng Content → học Traffic → dừng Traffic → học Funnel
```

Đúng:

```text
Part 9  mở Content ───────────────────────────→
Part 10 thêm Traffic ─────────────────────────→
Part 11 thêm Funnel/Data ─────────────────────→
```

## 6. Part 15 → 16 → 17 → 19

Đây là progression engineering mới:

```text
Part 15: reliable Go bot + workflow primitives
→ Part 16: deterministic decision/policy
→ Part 17: AI/tool workflow + HITL
→ Part 19: production reliability/security/governance
```

Không nhảy thẳng từ LLM prompt sang privileged external action.

## 7. Weekly capacity rule

Tất cả active loops phải nằm trong track capacity:

- Standard: khoảng **9h/tuần**;
- Accelerated: khoảng **11–12h/tuần**.

Heuristic:

```text
50–70%: primary knowledge/current Part
30–50%: active execution loops + evidence + review
```

Nếu vượt capacity:

1. ưu tiên evidence cho current Part/project;
2. giữ compliance/security bắt buộc;
3. giảm frequency của watch/maintenance loops;
4. không giảm PASS criteria.

## 8. Current Part và active loops

Repo giữ một **primary current Part/lesson** trong `PROGRESS.md`. Active loops có thể chạy song song nhưng không có nghĩa đang học nhiều Part ngang nhau.

## 9. Capstone được build dần

```text
Manual Affiliate Lab
→ Product/Content/Tracking artifacts
→ Data Warehouse/Dashboard
→ Experiment System
→ Go Product Tracker Bot
→ Opportunity/Policy Engine
→ AI Tool Workflow
→ Governed Production Bot
→ Capstone integration
```

Project artifact từ Part trước được nâng cấp/reuse, không làm xong rồi bỏ.

## 10. Quy tắc vận hành cuối

```text
ONE primary knowledge focus
+
ONLY unlocked execution loops
+
ALL within weekly capacity
+
PASS evidence before mastery
+
POLICY before consequential execution
```
