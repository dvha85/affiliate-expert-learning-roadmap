# Repository Governance — Quản trị repository

## Curriculum versioning and promotion

`CURRICULUM.md` is the active authority. Since ADR-005, its v2 Reality-First
sequence governs new work. The local tag `curriculum-v1-pre-reality-first`
preserves the v1 baseline; v1 Mission files remain historical/reference until
their v2 replacements are authored.

Do not equate `status: ready` with a delivered learning experience. Every
Mission must declare `curriculum_version`, `release_kind`, and `delivery`.
`python scripts/validate_readiness.py` checks metadata and paths; the `--strict`
mode is required before a new v2 Mission is promoted to ready.

Curriculum PRs must state migration impact, authority/evidence changes, and
whether a starter/eval/verification bundle is present. Preserve prior evidence and
links; do not silently renumber a learner's completed work.

## 1. Mục tiêu

Repository là curriculum có CI và learner evidence, vì vậy `main` phải được coi là protected integration branch (nhánh tích hợp được bảo vệ), không phải nơi push thử nghiệm trực tiếp.

Mục tiêu quản trị:

```text
Issue khi thay đổi đáng kể
→ branch riêng
→ Pull Request
→ Curriculum CI PASS
→ review diff
→ merge
→ push-CI trên main PASS
```

## 2. Quy tắc bắt buộc cho `main`

GitHub branch protection/ruleset nên cưỡng chế tối thiểu:

- Require a pull request before merging (bắt buộc Pull Request trước merge);
- Require status checks to pass before merging (bắt buộc CI xanh);
- required check: workflow/job `Curriculum CI / validate-curriculum` hoặc check context tương ứng GitHub đang hiển thị;
- Block force pushes (chặn force push);
- Block branch deletion (chặn xóa `main`).

Khuyến nghị thêm khi không gây cản trở không cần thiết:

- Require branches to be up to date before merging;
- Require conversation resolution trước merge;
- không cho bypass rules trừ tình huống recovery có audit rõ ràng.

## 3. Tại sao CI chạy trên `main` vẫn chưa đủ

Workflow hiện chạy với cả Pull Request và push vào `main`, nhưng:

```text
CI tồn tại
≠
CI được GitHub bắt buộc trước merge/push
```

Nếu branch protection/ruleset không bật, người có quyền vẫn có thể push/merge thay đổi làm CI đỏ rồi mới phát hiện sau.

Vì vậy có hai lớp:

```text
PROCESS POLICY
= CONTRIBUTING + review discipline

GITHUB ENFORCEMENT
= branch protection / ruleset + required checks
```

Cần cả hai.

## 4. Trạng thái audit 2026-08-28

Tại thời điểm Issue #37 được audit, GitHub API cho thấy `main` chưa được branch-protected và required status checks chưa được enforce.

Đây là repository configuration issue (vấn đề cấu hình repository), không phải lỗi trong curriculum source code.

Sau khi bật protection/ruleset, cần verify lại bằng GitHub repository settings/API và cập nhật trạng thái audit nếu cần.

## 5. Merge checklist

Trước merge:

- [ ] PR scope rõ ràng;
- [ ] inventory/sequence thay đổi có chủ đích, đồng bộ với `CURRICULUM.md` và learner evidence; không bảo vệ một fixed count;
- [ ] `Curriculum CI` hoàn thành `success`;
- [ ] semantic Build-First guards PASS;
- [ ] reference Go `gofmt`/`vet`/`test` PASS;
- [ ] learner Go `gofmt`/`vet`/`test` PASS;
- [ ] Markdown tuân thủ Language Policy;
- [ ] không auto-mark learner PASS;
- [ ] không có secret/credential/raw sensitive data;
- [ ] consequential automation vẫn giữ policy/risk/approval boundary.

## 6. Sau merge

Kiểm tra push-CI của merge commit trên `main`.

Nếu push-CI fail:

1. không tiếp tục xếp thêm structural changes lên lỗi chưa hiểu;
2. xác định regression;
3. mở fix PR nhỏ nhất;
4. không sửa learner PASS để “làm CI xanh”.

## 7. Quyền và ngoại lệ

Branch protection không thay thế security design của Bot. Nó chỉ bảo vệ code/curriculum change process.

Các thay đổi emergency (khẩn cấp) nếu buộc phải bypass phải có:

- lý do;
- actor;
- diff;
- kết quả CI sau thay đổi;
- follow-up review.

Mục tiêu cuối cùng là:

```text
MAIN = trạng thái đã review + đã kiểm tự động
```

chứ không phải nơi chứa work-in-progress chưa được kiểm chứng.
