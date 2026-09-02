# Bắt đầu cho người mới — Curriculum v2

Bạn không cần biết Go, terminal nâng cao, API key hay có tài khoản Affiliate để
chạy bước đầu tiên. O00 chỉ là demo E0 synthetic: không publish, không có
credential, không tạo learner PASS hay market evidence.

## 1. Mở repo và kiểm tra tối thiểu

Mở terminal tại thư mục repo, rồi chạy:

```bash
python scripts/preflight.py
python orientation/o00/run_o00.py --validate
```

Nếu lệnh đầu báo `BLOCKED`, đọc dòng `Next step` tương ứng. Không gửi ảnh chụp
credential, link dashboard private hay raw analytics để nhờ hỗ trợ.

## 2. Xem full loop an toàn

```bash
python orientation/o00/run_o00.py
```

Output là synthetic trace từ Observation đến ChangeProposal `PENDING_REVIEW`.
Nó dừng ở `DRY_RUN`, external side-effect count bằng 0, và không thay thế M00.

## 3. Tạo state riêng của bạn

```bash
python scripts/init_learner_workspace.py --init
```

Folder `workspace/` bị Git ignore. Lưu progress, raw export và private evidence
tại đó; chỉ commit summary đã redact sau review.

## OS quick path

| Hệ điều hành | Python/Git | Khi bị block |
|---|---|---|
| macOS | Python 3 và Git thường có qua Command Line Tools | chạy `python3` thay cho `python` nếu máy chưa map alias |
| Windows | cài Python từ python.org, Git for Windows | đóng/mở lại PowerShell sau khi cài để PATH có hiệu lực |
| Linux | cài package `python3` và `git` từ package manager | dùng `python3` nếu không có command `python` |

Devcontainer là lựa chọn bổ sung, không phải prerequisite. Xem
[`../.devcontainer/devcontainer.json`](../.devcontainer/devcontainer.json) nếu
bạn đã dùng VS Code/compatible container tooling.

## 4. Khi cần giúp

Dùng issue template **Beginner blocker** và chỉ ghi OS, lệnh, blocker code,
output đã redact và bước mong đợi. Không dán `.env`, token, cookie, email,
customer data hoặc raw analytics.

## Sau O00

Đọc [M00 First Safe Market Loop](../missions/M00-first-safe-market-loop.md).
Nếu chưa có channel/account được phép, ghi `BLOCKED_EXTERNAL`; bạn vẫn có thể
học capability bằng fixture, nhưng không gọi đó là E1/E2.
