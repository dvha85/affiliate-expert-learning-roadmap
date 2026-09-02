# Contract schemas v1

These JSON Schema documents define the portable v2 record vocabulary. The
repository's standard-library validator checks the invariants needed by O00 and
starter packs; implementation profiles may add fields but must not weaken
origin, provenance, missing/zero or authority semantics.

`origin` is one of `synthetic`, `real`, `test`, `replay`. It never substitutes
for Reality-level eligibility.
