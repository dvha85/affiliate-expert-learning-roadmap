# O00 runnable orientation

Đây là fixture synthetic cố ý nhỏ. Không nhập product/account data thật, không
thêm credential, không đổi `orientation_only` thành `false` và không dùng output
này làm evidence E1+.

```bash
python run_o00.py
```

Bạn chỉ cần quan sát chain `evidence → decision state → no action → next
measurement`, rồi mở `../../docs/O00-SAFE-SYNTHETIC-WALKTHROUGH.md`.
