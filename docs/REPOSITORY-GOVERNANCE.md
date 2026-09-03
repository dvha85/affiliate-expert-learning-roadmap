# Repository Governance — Quản trị repository

`CURRICULUM.md` là authority hiện hành duy nhất cho learner sequence, evidence, autonomy ceiling và PASS boundary. Các syllabus/lesson/migration lịch sử không được dùng để ghi đè curriculum hiện hành.

## 1. Merge path bắt buộc

```text
issue/spec
→ branch
→ Pull Request
→ required CI
→ human review
→ merge/reject
```

Development Agent có thể viết code/docs/tests và mở PR, nhưng không tự cấp quyền merge hoặc production activation.

## 2. Required checks trên `main`

Sau PR hardening, workflow `Curriculum CI` được tách thành bốn check dễ chẩn đoán:

- `Curriculum CI / curriculum`
- `Curriculum CI / evidence-and-safety`
- `Curriculum CI / python-regression`
- `Curriculum CI / deterministic-runtime`

Branch protection hoặc repository ruleset nên require cả bốn check trước merge.

## 3. GitHub settings cần bật

- Require a pull request before merging;
- Require status checks to pass before merging;
- Block force pushes;
- Block branch deletion;
- khuyến nghị require conversation resolution;
- bypass chỉ dành cho recovery có audit rõ.

CI tồn tại trong Git tree không đồng nghĩa GitHub đang enforce CI trước merge. Hai lớp phải tách rõ:

```text
SOURCE CONTROL
= workflow + validators + tests

REPOSITORY ENFORCEMENT
= ruleset / branch protection / required checks
```

## 4. Repository metadata

Description không được hard-code inventory dễ drift như `23 parts / 671 lessons`.

Mô tả đề xuất:

```text
Evidence-first curriculum for building a governed Affiliate Intelligence Bot that evolves from real observations to controlled automation.
```

Repository description và ruleset là GitHub settings, không thể hoàn tất chỉ bằng source PR. Phải verify riêng sau khi thay đổi settings.

## 5. Canonical authority guard

CI chạy `scripts/validate_canonical_authority.py` để chặn regression trong đó historical source lại tự nhận `active canonical`.

Snapshot trước curriculum reset được giữ tại:

```text
archive/pre-curriculum-reset-2026-09-03
```

Không giữ compatibility bằng cách cho nhiều file cùng tự nhận authority.

## 6. Development Agent boundary

Development Agent được phép:

- implement/refactor;
- viết test;
- sửa workflow artifact;
- đề xuất policy/rule change;
- mở Pull Request.

Không được suy ra:

```text
agent authored PR
→ safe to merge

CI green
→ Mission authority increased

policy code changed
→ production policy authorized
```

Policy/runtime/authority change vẫn cần human review và activation gate riêng.

## 7. Merge checklist

- [ ] scope PR rõ;
- [ ] `CURRICULUM.md` không bị authority file thấp hơn ghi đè;
- [ ] bốn required CI groups PASS;
- [ ] không auto-mark learner Reality/PASS;
- [ ] không có secret/credential/raw sensitive data;
- [ ] evidence semantics giữ `0 != missing != pending != inconclusive`;
- [ ] consequential action vẫn qua policy/risk/approval/audit;
- [ ] runtime test có failure case cho authority/safety behavior thay đổi.

## 8. Sau merge

Push-CI trên `main` phải xanh. Nếu fail, mở fix PR nhỏ nhất; không chỉnh learner evidence/PASS chỉ để làm CI xanh.

Mục tiêu cuối:

```text
MAIN
= reviewed source
+ automated checks
+ enforced merge path

PRODUCTION AUTHORITY
= separate governed activation decision
```
