# Contributing to Affiliate Expert Learning Roadmap

Repo này được phát triển như một curriculum có kiểm soát. Mọi structural/execution change ưu tiên **issue-first**.

## 1. Authority layers

```text
ACTIVE CANONICAL
= sources/SYLLABUS-v2026.09.md

HISTORICAL BASELINE
= sources/SYLLABUS-v2026.08.md

KNOWLEDGE INVENTORY
= ROADMAP.md + roadmap/part-00..22.md

DEFAULT LEARNER EXECUTION
= BUILD-FIRST.md + Mission system

CURRENT FACTS
= freshness policy + external source registers
```

Build-First thay execution order, **không** tự đổi Part/Chapter/Lesson IDs, 14 main Projects, provenance hoặc learner PASS history.

## 2. Build-First rules

Read:

- [`BUILD-FIRST.md`](BUILD-FIRST.md)
- [`docs/BUILD-FIRST-LEARNING-MODEL.md`](docs/BUILD-FIRST-LEARNING-MODEL.md)
- [`docs/EXECUTION-MODEL.md`](docs/EXECUTION-MODEL.md)

Rules:

```text
Mission ≠ Lesson ≠ Project ≠ Bot Version
```

- Mission may pull knowledge from multiple Parts.
- Early Go usage does not imply Part 15 mastery.
- A Mission must never auto-mark lesson PASS.
- Do not bulk-edit all 671 lesson front matters merely to add mission mappings; central mission↔knowledge mapping is preferred until a lesson is genuinely authored/revised.
- Reuse the same implementation evidence across lesson/mission/project when it is genuinely the same artifact; do not double-count work.

## 3. Go-first direction

Primary implementation language remains Go.

Core engineering principles:

```text
modular monolith first
+ deterministic logic before LLM
+ explicit tool boundary
+ durable state when needed
+ least privilege
+ RISK 0/1/2 governance
+ Human Approval for consequential action
+ audit/tracing/kill switch
```

References:

- [`docs/ADR-001-GO-FIRST-BOT-STACK.md`](docs/ADR-001-GO-FIRST-BOT-STACK.md)
- [`docs/GO-BOT-ENGINEERING-STACK.md`](docs/GO-BOT-ENGINEERING-STACK.md)
- [`docs/AUTONOMY-AND-APPROVAL-MODEL.md`](docs/AUTONOMY-AND-APPROVAL-MODEL.md)
- [`docs/AGENT-SECURITY-AND-TOOL-GOVERNANCE.md`](docs/AGENT-SECURITY-AND-TOOL-GOVERNANCE.md)

## 4. Lesson authoring remains valid

Use:

- [`templates/LESSON.md`](templates/LESSON.md)
- [`docs/LESSON-AUTHORING-STANDARD.md`](docs/LESSON-AUTHORING-STANDARD.md)
- [`docs/PASS-CRITERIA.md`](docs/PASS-CRITERIA.md)

Authoring state:

```text
planned → draft → ready
```

Learner state:

```text
not PASS → PASS / RETRY
```

`ready` never means learner PASS.

## 5. Current facts

Platform/legal/API/software facts that can change must use external verification and `last_verified` according to [`docs/FRESHNESS-POLICY.md`](docs/FRESHNESS-POLICY.md).

Do not turn a current runtime/library/platform value into permanent canonical truth.

## 6. Evidence safety

Do not commit:

- API keys/tokens/passwords;
- personal/sensitive raw exports;
- credentials;
- content without distribution rights.

Artifact existence alone never means PASS.

## 7. Pull request checklist

Before merge:

```bash
python scripts/validate_curriculum.py
python scripts/validate_hardening.py
python -m unittest discover -s tests -v
```

Checklist:

- [ ] active canonical remains v2026.09;
- [ ] historical v2026.08 preserved;
- [ ] 23 Parts / 89 Chapters / 671 lessons / 14 Projects unchanged unless a separately approved canonical revision explicitly changes them;
- [ ] Go-first remains primary direction;
- [ ] relative links work;
- [ ] freshness metadata remains valid;
- [ ] no learner checkbox is changed merely because content/code exists;
- [ ] Build-First change does not blur Mission/Lesson/Project/Bot Version semantics;
- [ ] consequential bot side effects retain policy/risk/approval boundaries;
- [ ] code and evidence contain no secrets.

Mission-specific authoring/CI contracts are introduced by subsequent phases of Issue #30.

## 8. Licensing

Repository is public but does not currently publish an open-source license for curriculum/content. See [`docs/LICENSING.md`](docs/LICENSING.md).