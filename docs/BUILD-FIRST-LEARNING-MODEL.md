# Build-First Learning Model v1

## 1. Authority

Build-First is an **execution layer** on top of the active canonical curriculum.

```text
WHAT MUST EVENTUALLY BE KNOWN
= sources/SYLLABUS-v2026.09.md
+ inherited v2026.08 baseline
+ normalized ROADMAP inventory

WHAT TO BUILD NEXT
= BUILD-FIRST.md + Mission system
```

It does not create a new canonical syllabus revision and does not change 23 Parts / 89 Chapters / 671 lessons / 14 main projects.

## 2. Learning loop

```text
Ship Target
→ Build smallest working slice
→ Run
→ Observe gap/failure
→ Pull required knowledge
→ Improve implementation/decision logic
→ Test
→ Operate
→ Measure result
→ Explain
→ Save evidence
→ Ship bot version
```

The learner should encounter a concrete reason to learn a concept before spending large blocks of time studying that concept in isolation.

## 3. Four entities

### Lesson
Canonical knowledge unit. Lesson PASS remains independent and evidence-based.

### Mission
Build/operate unit with one inspectable ship target. Mission may pull several lessons from different Parts.

### Canonical Project
One of the 14 integration milestones defined by the curriculum. Missions may contribute reusable evidence to a Project, but Mission IDs never become Project IDs.

### Bot Version
Product state after a mission. It is not a learner grade.

## 4. Two progress axes

```text
PRODUCT PROGRESS
Mission → working Bot Version → operational evidence

KNOWLEDGE PROGRESS
Lesson → knowledge evidence → PASS/RETRY
```

A learner may ship a small feature while still having lessons not yet PASS. A mission may require a subset of those lessons to be understood before Mission PASS, but must never mutate lesson PASS automatically.

## 5. Just-in-time knowledge classes

Mission knowledge links use three levels:

- **REQUIRED** — must be understood for Mission PASS.
- **ON-DEMAND** — pull when implementation/decision context triggers the need.
- **REFERENCE** — useful deeper material; not a Mission PASS gate.

This mapping lives outside the 671 lesson front matter to avoid a bulk metadata migration before lessons are authored.

## 6. Go-first progression

Part 15 remains formal Bot Engineering mastery. Build-First permits early Go usage with narrow scope.

```text
M00: package/main/functions/basic tests
M01: struct/JSON/errors/validation
M02: SQL/repository/migrations/history
M04+: context/scheduling/concurrency
M05+: retry/backoff/idempotency/timeout
later: durable workflow/tool/AI/governance
```

Formal mastery is proven later through broader engineering evidence.

## 7. Build-first does not mean unsafe-first

Early missions should minimize external side effects. Consequential execution remains behind deterministic policy/risk boundaries and Human Approval where required.

## 8. Capacity rule

Build-first changes sequencing, not weekly capacity. Standard remains ~9h/week; Accelerated remains ~11–12h/week until actual mission data supports recalibration.

## 9. Anti-patterns

Do not:

- delete or renumber canonical lessons because missions cross Parts;
- create Project 15+ from Mission IDs;
- bulk-mark lessons PASS when a mission ships;
- teach months of Go syntax before the first runnable bot;
- add AI autonomy before deterministic decision/policy boundaries;
- count the same implementation separately as lesson artifact + mission artifact + project artifact when it is genuinely the same evidence.

## 10. End state

The curriculum should ultimately feel like:

```text
I build a real Affiliate Intelligence Bot
→ the bot exposes what I do not understand
→ I learn exactly that concept
→ I improve the bot
→ I operate and measure it
→ the evidence proves both product and knowledge progress
```