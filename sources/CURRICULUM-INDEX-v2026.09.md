# Curriculum Index v2026.09 — normalized canonical resolution

> This file defines the authoritative resolution model for all **671 active lesson IDs** without duplicating 671 roadmap rows into a second hand-maintained list.

## 1. Authority

The active lesson index is the validated union of:

```text
ROADMAP.md
+ roadmap/part-00.md ... roadmap/part-22.md
+ SYLLABUS-v2026.09 explicit overrides
+ SYLLABUS-v2026.08 historical source evidence
```

The 23 Part files are the normalized lesson inventory. Curriculum CI is responsible for proving that the inventory is exactly **23 Parts / 89 Chapters / 671 lessons** and that every lesson ID is unique and correctly placed.

This file defines how each normalized lesson is traced back to source material; it is not a second copy of the roadmap.

## 2. Provenance classes

Every active lesson resolves to one of three provenance classes.

### `source_explicit`

The lesson ID/title is explicitly present in the historical syllabus source.

Example:

```text
0.1 — Affiliate Expert là gì?
4.6 — CTR
27.3 — Ranking
```

Resolution:

```text
roadmap lesson
→ explicit lesson in SYLLABUS-v2026.08
→ apply v2026.09 override only if declared
```

### `normalized_from_chapter`

The historical syllabus contains a canonical chapter/design block but does **not** explicitly enumerate the active lesson IDs. The roadmap normalized that block into lesson-sized units during curriculum construction.

Known examples include architecture/data-model chapters such as:

```text
Chapter 38 — Affiliate Data Model
Chapter 50 — Bot Architecture
Chapter 51 — Technology Stack
```

Resolution:

```text
roadmap lesson
→ normalized from the historical chapter/block
→ provenance is chapter-level, not a claim that the exact lesson ID existed in v2026.08
```

### `normalized_then_overridden`

The lesson was normalized from a historical chapter/block and its active scope/title was subsequently changed by an explicit v2026.09 override.

Primary examples are Go-first Bot Engineering lessons in Parts 15–19/21 where the active curriculum replaced C#/.NET-first implementation assumptions with Go, durable workflows, tool/MCP boundaries, governed autonomy and agent-security scope.

Resolution:

```text
historical chapter/block
→ normalized roadmap lesson
→ explicit v2026.09 override
```

## 3. `S:P/C/L` semantics

`S:P{part}/C{chapter}/L{lesson}` is a **version-neutral normalized canonical identifier**.

It means:

```text
Locate active lesson X.Y in the validated roadmap inventory
→ inspect v2026.09 explicit override if present
→ inspect v2026.08 source evidence
→ classify provenance as source_explicit / normalized_from_chapter / normalized_then_overridden
```

It does **not** mean that the exact `Lx.y` token necessarily appeared verbatim in `SYLLABUS-v2026.08.md`.

For normalized lessons, chapter-level source provenance is the truthful historical claim.

## 4. Active structure invariants

```text
Parts: 23
Chapters: 89
Lessons: 671
Main projects: 14
PRIMARY IMPLEMENTATION LANGUAGE = Go
```

These values are protected by Curriculum CI. A provenance repair must not silently change them.

## 5. Source hierarchy

```text
ACTIVE NORMATIVE OVERRIDES
= SYLLABUS-v2026.09.md

HISTORICAL SOURCE EVIDENCE
= SYLLABUS-v2026.08.md

NORMALIZED ACTIVE LESSON INVENTORY
= ROADMAP.md + roadmap/part-00.md ... roadmap/part-22.md

PACING
= docs/15-MONTH-PLAN.md / docs/12-MONTH-PLAN.md

EXECUTION
= docs/EXECUTION-MODEL.md

SUPPLEMENTS
= Noi-dung-dao-tao.txt + Nghien-cuu.txt

CURRENT FACTS
= external source registers + freshness policy
```

## 6. Authoring rule

Before authoring a lesson:

1. find its normalized lesson ID/title in the Part roadmap;
2. inspect `SYLLABUS-v2026.09.md` for an explicit override;
3. inspect the historical syllabus at lesson level when the lesson is source-explicit, otherwise at chapter/block level;
4. do not claim a normalized lesson ID was present verbatim in the historical source when it was derived from a chapter block;
5. add training/research/current external refs only when they genuinely support the authored content.

## 7. Why the index is resolved instead of duplicated

A manually duplicated 671-row file would create a second mutable curriculum inventory and increase drift risk. The authoritative normalized index is therefore **computed by rule from the validated roadmap inventory**, while this document records provenance semantics and the historical/override relationship.

Future CI hardening must validate that every roadmap lesson can be resolved under this model and report provenance gaps explicitly.
