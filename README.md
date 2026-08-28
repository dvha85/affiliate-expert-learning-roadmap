# Affiliate Expert Learning Roadmap

**Build an Affiliate Intelligence Bot while learning Affiliate, Data, Engineering and AI just-in-time.**

```text
Affiliate Expert
+
Affiliate Bot Engineer
=
Affiliate Intelligence Expert
```

## START HERE — Build First

The default learner path is now [`BUILD-FIRST.md`](BUILD-FIRST.md).

```text
Build
→ Run
→ Observe
→ Pull Knowledge
→ Improve
→ Test
→ Operate
→ Evidence
→ Next Bot Version
```

Do **not** interpret this as deleting the knowledge curriculum. [`ROADMAP.md`](ROADMAP.md) remains the normalized canonical knowledge inventory.

## Curriculum authority

- **Active canonical:** `sources/SYLLABUS-v2026.09.md`
- **Historical baseline:** `sources/SYLLABUS-v2026.08.md`
- **Knowledge inventory:** 23 Parts · 89 Chapters · 671 lessons
- **Main projects:** 14
- **Primary Bot Engineering language:** Go
- **Standard capacity:** ~9h/week · 15-month planning envelope
- **Accelerated:** ~11–12h/week · 12-month planning envelope

The source/provenance model is documented in [`sources/CURRICULUM-INDEX-v2026.09.md`](sources/CURRICULUM-INDEX-v2026.09.md).

## Two layers

```text
SYLLABUS / ROADMAP
= WHAT YOU MUST EVENTUALLY KNOW

BUILD-FIRST
= WHAT YOU BUILD NEXT
```

A Lesson is a knowledge unit. A Mission is a build/operate unit. A Project is one of the 14 canonical integration milestones. A Bot Version is product state.

```text
Mission ≠ Lesson ≠ Project ≠ Bot Version
```

See [`docs/BUILD-FIRST-LEARNING-MODEL.md`](docs/BUILD-FIRST-LEARNING-MODEL.md).

## Go from the beginning, mastery later

Build-First uses enough Go to ship the first runnable bot immediately. Formal Bot Engineering mastery still belongs to the wider Part 15+ evidence scope.

```text
USE GO EARLY
≠
CLAIM GO MASTERY EARLY
```

Go-first engineering standards remain:

- [`docs/ADR-001-GO-FIRST-BOT-STACK.md`](docs/ADR-001-GO-FIRST-BOT-STACK.md)
- [`docs/GO-BOT-ENGINEERING-STACK.md`](docs/GO-BOT-ENGINEERING-STACK.md)
- [`docs/AUTONOMY-AND-APPROVAL-MODEL.md`](docs/AUTONOMY-AND-APPROVAL-MODEL.md)
- [`docs/AGENT-SECURITY-AND-TOOL-GOVERNANCE.md`](docs/AGENT-SECURITY-AND-TOOL-GOVERNANCE.md)

## Safety and governed autonomy

```text
Deterministic Logic before LLM autonomy
Decision ≠ Execution
Model Output = Untrusted Input

RISK 0 → auto execute
RISK 1 → auto execute + audit
RISK 2 → persist → Human Approval → revalidate → execute/reject
```

## Knowledge PASS vs product progress

Lesson authoring and learner state remain separate:

```text
Authoring: planned → draft → ready
Learner:   not PASS → PASS / RETRY
```

A working bot or future Mission PASS never auto-marks a lesson PASS. Current lesson criteria remain in [`docs/PASS-CRITERIA.md`](docs/PASS-CRITERIA.md).

## Current knowledge layer

Current platform/software/legal facts remain separate from stable canonical structure:

- [`docs/FRESHNESS-POLICY.md`](docs/FRESHNESS-POLICY.md)
- [`docs/AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md`](docs/AFFILIATE-KNOWLEDGE-REFRESH-2026.08.md)
- [`docs/BOT-ENGINEERING-REFRESH-2026.08.md`](docs/BOT-ENGINEERING-REFRESH-2026.08.md)

## Key documents

- [Build-First Roadmap](BUILD-FIRST.md) — default learner execution entry point
- [Knowledge Roadmap](ROADMAP.md) — canonical normalized lesson inventory
- [Progress Dashboard](PROGRESS.md)
- [Execution Model](docs/EXECUTION-MODEL.md)
- [Build-First Learning Model](docs/BUILD-FIRST-LEARNING-MODEL.md)
- [Projects](docs/PROJECTS.md)
- [15-Month Plan](docs/15-MONTH-PLAN.md)
- [12-Month Plan](docs/12-MONTH-PLAN.md)
- [Curriculum CI](docs/CURRICULUM-CI.md)
- [Glossary VI](docs/GLOSSARY-VI.md)

## Core principles

```text
BUILD → RUN → OBSERVE → LEARN → FIX → TEST → OPERATE → MEASURE
UNDERSTAND → DECIDE → EXECUTE → MEASURE → LEARN → IMPROVE
```

- DATA > OPINION.
- EXPECTED VALUE > COMMISSION RATE.
- Do not automate what you do not understand manually.
- Do not optimize before measuring.
- Deterministic logic before LLM autonomy.
- High-risk action requires policy/risk control and Human Approval.

## Contribution model

The repository remains issue-first. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before structural or execution-model changes.

`ready` means authored enough to learn; it never means learner PASS.