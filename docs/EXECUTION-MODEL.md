# Build-First Execution Model

> Curriculum v2026.09 dùng **Mission-first execution + just-in-time knowledge pulls + persistent operating loops**.

## 1. Mental model

```text
                 BUILD-FIRST SPINE

Mission M00 → M01 → M02 → M03 → ...
    │          │      │
    ▼          ▼      ▼
Knowledge   Knowledge Knowledge
  Pull        Pull      Pull
    │          │        │
    └──────────┴────────┘
             ↓
        Bot Version evolves
```

`ROADMAP.md` vẫn là canonical knowledge inventory. Mission system quyết định learner build gì tiếp theo; knowledge prerequisites quyết định learner phải hiểu gì để mission đó PASS.

## 2. Build-first loop

```text
Ship Target
→ Build smallest working slice
→ Run
→ Observe failure/gap
→ Pull required knowledge
→ Improve
→ Test
→ Operate
→ Measure
→ Explain
→ Save evidence
→ Next Bot Version
```

The learner should not wait until Part 15 to touch Go. Early missions use narrow Go concepts; Part 15 remains formal Bot Engineering mastery.

## 3. Knowledge dependency semantics

Mission knowledge may be classified as:

- **REQUIRED** — must be understood for Mission PASS.
- **ON-DEMAND** — pull when implementation or business context triggers the need.
- **REFERENCE** — useful depth, not a Mission PASS gate.

Mission completion never auto-marks a lesson PASS.

## 4. Operating loops remain cumulative

As capability grows, these loops stay active when relevant:

- Compliance / Platform Watch
- Market / Customer / Product Watch
- Content Production
- Traffic Distribution
- Funnel / Revenue / Data Capture
- Experiment Loop
- Bot / Automation
- AI-assisted Workflow
- Governed Action / Approval

Build-First changes **when** capabilities are introduced, not the requirement to keep useful loops running.

## 5. Governed Action / Approval

Consequential execution keeps the current policy model:

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

Human review is for consequential decisions/exceptions, not mechanical babysitting.

## 6. Go-first progression

```text
Early Missions
→ minimal Go usage to ship

Later Missions
→ database / concurrency / reliability / workflow

Part 15+ mastery
→ broader engineering evidence and project integration
```

This is intentionally **USE before MASTER**, not mastery-by-copying.

## 7. AI progression

```text
Deterministic data/logic
→ AI summarize/classify/analyze
→ evaluated recommendation
→ explicit tool contract
→ ActionIntent
→ Policy/Risk
→ Auto or Human Approval
```

Do not jump from prompt directly to privileged external action.

## 8. Capacity

- Standard: ~9h/week.
- Accelerated: ~11–12h/week.

Heuristic during Build-First:

```text
50–70% build/run/debug/operate
20–30% required knowledge pull
10–20% evidence/review
```

Ratios are adaptive; PASS quality is not reduced to hit a calendar date.

## 9. Capstone evolution

```text
Runnable Go Bot
→ Product Data
→ Product Watcher
→ Product Intelligence
→ Content / Revenue Intelligence
→ Experiment Engine
→ Decision / Policy Engine
→ AI Tool Workflow
→ Governed Production Bot
→ Affiliate Intelligence Platform
```

Project artifacts should evolve and be reused instead of being rebuilt from scratch.

## 10. Final operating rule

```text
ONE current Mission
+
ONLY necessary Knowledge Pulls
+
ACTIVE operating loops within capacity
+
PASS evidence before mastery
+
POLICY before consequential execution
```