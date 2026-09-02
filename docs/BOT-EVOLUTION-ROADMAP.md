# Bot evolution roadmap v2

> Sequence authority: [CURRICULUM.md](../CURRICULUM.md). The first two
> Missions intentionally produce market/measurement artifacts before a Bot
> release. Version labels start only at the smallest deterministic Bot.

| Mission | Bot version | Part | Product outcome | Reality | AI / authority |
|---|---|---|---|---|---|
| M00 | pre-bot | P0 | First Safe Market Loop; human-only artifact/publish | E1→E2 | A0 human-only / no Bot |
| M01 | pre-bot | P1 | First Outcome Snapshot | E3 | A0 manual measurement |
| M02 | v0.1 | P1 | Smallest Deterministic Bot | E1 support | A0 deterministic |
| M03 | v0.2 | P2 | Trustworthy History & Measurement | E3 | A0 deterministic |
| M04 | v0.3 | P2 | Grounded AI Advisor with fallback | E3 | A1 advisory; no tools/write |
| M05 | v0.4 | P3 | First Reviewed Improvement | E4 | A1 propose only |
| M06 | v1.0 | P4 | Reliable Watcher | E4 | A0 core + A1 triage |
| M07 | v1.1 | P4 | Decision and Abstention | E4 | A1 advisory |
| M08 | v1.2 | P5 | Read-only Evidence Agent | E4 | A2-RO |
| M09 | v1.3 | P5 | Shadow Action and Approval | E4 | A3-shadow |
| M10 | v1.4 | P5 | Governed Canary | E5 | A3-limited |
| M11 | v2.0 | P6 | Production Closed Loop | E6 | A3-production |

```text
O00 synthetic walkthrough (not PASS)
→ M00 human market action
→ M01 outcome snapshot ∥ M02 deterministic baseline
→ M03 history/measurement → M04 grounded advice → M05 reviewed improvement
→ M06 … M11 governed production
```

## Version rules

- `pre-bot` means no Bot release is claimed; it is not a hidden `v0.x`.
- M02 begins the deterministic implementation profile. Go may be a golden
  oracle/reference here, but another auditable profile is permitted by ADR-004.
- An AI/agent capability never replaces the deterministic evidence/policy
  boundary, and `ActionIntent` is never execution permission.
- The numeric Bot versions are targets for v2 authoring, not a claim that their
  delivery packages already exist.

## Optional advanced work

A4 multi-agent remains an **advanced option sau khi M11**, not a Core Mission.
