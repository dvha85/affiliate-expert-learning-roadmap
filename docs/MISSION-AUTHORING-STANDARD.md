# Mission Authoring Standard

## 1. Purpose

Mission is a build/operate unit, not a replacement for a canonical lesson or project.

## 2. Naming

```text
missions/M00-bot-boots.md
missions/M01-product-ingest.md
```

Mission IDs are sequential, zero-padded, and independent from lesson IDs.

## 3. Required metadata

```yaml
mission_id: "M00"
title: "..."
status: planned|draft|ready
requires_missions: []
bot_version_from: null
bot_version_to: "v0.0"
estimated_hours: 2
knowledge:
  required: []
  on_demand: []
  reference: []
projects:
  contributes_to: []
risk_scope:
  external_side_effects: false
```

## 4. Knowledge semantics

- `required`: knowledge that must be understood before Mission PASS.
- `on_demand`: pull when implementation/business context exposes the need.
- `reference`: deeper material that is useful but not a Mission PASS gate.

Mission↔knowledge mapping is centralized. Do not bulk-edit all 671 lesson front matters to add mission metadata.

## 5. Required sections for `ready`

1. `## Ship Target`
2. `## Starting Bot State`
3. `## Build First`
4. `## Run`
5. `## Observe`
6. `## Knowledge Pull`
7. `## Improve`
8. `## Tests`
9. `## Operate`
10. `## Failure Case`
11. `## Evidence`
12. `## Explain-back`
13. `## Mission PASS`
14. `## Bot Version Result`
15. `## Next Mission`

## 6. Build-first rule

Mission should present the smallest runnable implementation before long theory blocks. Knowledge is introduced because the learner has a concrete decision, failure, measurement or design gap to resolve.

## 7. Tests and operation

Testing depth scales with mission scope. Early missions may need only unit/behavior tests. Later missions add integration, restart/recovery, idempotency, security, policy and approval tests when relevant.

Every mission must contain at least one explicit failure case.

## 8. Evidence

Evidence must be inspectable and may include:

- code path + commit SHA;
- test output;
- sample data/output;
- before/after result;
- logs/metrics;
- decision note;
- screenshot/link when needed.

Do not duplicate the same code into artifact files merely to create more evidence.

## 9. Project contribution

`projects.contributes_to` may reference only canonical Projects 1–14. Contribution does not automatically mark that Project PASS.

## 10. Safety

Mission scope must state whether external side effects exist. Consequential side effects require the appropriate deterministic policy/risk/approval controls by the stage where they are introduced.

## 11. Authoring Definition of Done

A mission may be `ready` only when:

- metadata is valid;
- ship target is observable;
- commands/steps are executable or intentionally design-only with clear reason;
- required knowledge mapping is explicit;
- tests + failure case exist;
- evidence path is defined;
- PASS criteria are measurable;
- no lesson PASS is mutated by mission completion;
- no secret/credential is required in committed material.