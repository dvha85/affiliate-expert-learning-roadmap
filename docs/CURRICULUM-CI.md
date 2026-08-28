# Curriculum CI

Curriculum CI protects three independent layers plus the executable bootstrap bot.

## Run locally

```bash
python scripts/validate_curriculum.py
python scripts/validate_hardening.py
python scripts/validate_build_first.py
python -m unittest discover -s tests -v

cd lab/affiliate-bot
go test ./...
```

Exit code `0` means PASS.

## Layer 1 — Canonical curriculum validator

`scripts/validate_curriculum.py` protects:

- active canonical v2026.09 + historical v2026.08;
- 23 Parts / 89 Chapters / 671 lessons;
- Go-first Part 15 direction;
- timeline metadata;
- lesson IDs, metadata, lifecycle and headings;
- relative links;
- freshness metadata contract.

Representative error groups: `CANON*`, `TECH*`, `ROADMAP*`, `COUNT*`, `TIME*`, `ID*`, `LINK*`, `META*`, `FRESH*`, `STATE*`, `HEAD*`.

## Layer 2 — Curriculum integrity hardening validator

`scripts/validate_hardening.py` protects:

- external source IDs against Affiliate + Bot source registers;
- normalized provenance authority;
- exact 671 lesson / 89 chapter inventory;
- canonical Project 1–14 inventory and Part placement;
- authority-document consistency.

It keeps Build-First from weakening the source/provenance rules introduced before the migration.

## Layer 3 — Build-First validator

`scripts/validate_build_first.py` protects the execution architecture without redefining the canonical syllabus.

### BUILD001 — authority files

Requires:

- `BUILD-FIRST.md`;
- `docs/BUILD-FIRST-LEARNING-MODEL.md`;
- `docs/MISSION-AUTHORING-STANDARD.md`;
- `docs/MISSION-PASS-CRITERIA.md`;
- `docs/BOT-EVOLUTION-ROADMAP.md`;
- `docs/MISSION-KNOWLEDGE-MAP.md`.

### BUILD002 — Mission identity

Mission IDs must be valid/unique and authored filenames must start with their own `MXX-` ID.

### BUILD003 — Mission sequence

The product roadmap must contain exactly `M00` through `M15` in order.

Authored Mission files are allowed to be only a **contiguous prefix** from `M00`. Current intent is M00–M03 authored; M04–M15 remain roadmap targets until genuinely authored. CI therefore does not force placeholder Mission files.

### BUILD004 — knowledge refs

Explicit lesson IDs in authored Mission knowledge metadata must resolve in the canonical 671-lesson inventory.

### BUILD005 — dependency graph

Mission dependencies must point backward and may not contain cycles.

### BUILD006 — Bot Version progression

Bot versions in the M00–M15 roadmap must strictly increase. An authored Mission's `bot_version_to` must match its roadmap target.

### BUILD007 — ready Mission contract

Every `status: ready` Mission must contain:

```text
Ship Target
Starting Bot State
Build First
Run
Observe
Knowledge Pull
Improve
Tests
Operate
Failure Case
Evidence
Explain-back
Mission PASS
Bot Version Result
Next Mission
```

### BUILD008 — learner-state separation

Mission content may not contain a mechanism that declares canonical lesson PASS automatically.

```text
Mission PASS ≠ Lesson PASS
```

### BUILD009 — canonical Projects only

Mission `projects.contributes_to` may reference only Projects 1–14. Mission IDs do not create Project 15+.

### BUILD010 — bootstrap bot

The executable learning workspace must retain its minimum bootstrap files, including `lab/affiliate-bot/go.mod`, command entry point and sample product data.

## Executable Go gate

GitHub Actions also runs:

```bash
cd lab/affiliate-bot
go test ./...
```

This prevents documentation from claiming a working Build-First bot while the bootstrap code no longer compiles/tests.

Fast CI intentionally does not require a PostgreSQL service yet. M02 ships the persistence boundary + migration contract while fast tests use the in-memory Repository. Integration infrastructure can be added when its operational value justifies the extra CI dependency.

## Regression / mutation tests

`tests/test_build_first_validator.py` protects at least:

- current repo is clean;
- missing authority files;
- broken M00–M15 sequence;
- backwards Bot Version;
- unknown lesson ref;
- forward Mission dependency;
- missing required section in a ready Mission;
- lesson-PASS mutation mechanism;
- Project 15 reference;
- missing bootstrap bot.

Existing curriculum/hardening/scaffolder regression tests continue to run unchanged.

## GitHub Actions merge rule

Workflow `.github/workflows/curriculum-ci.yml` runs on every pull request and every push to `main`.

```text
canonical validator
→ hardening validator
→ Build-First validator
→ Python regression tests
→ Go bootstrap tests
```

A Build-First PR should not merge while any layer is failing.

## State rule

CI validates structure and code, not learner achievement. A passing CI run must never be interpreted as learner Mission PASS, lesson PASS or Project PASS.