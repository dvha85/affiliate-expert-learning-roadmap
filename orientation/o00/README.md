# O00 runnable orientation

Đây là fixture synthetic cố ý nhỏ. Không nhập product/account data thật, không
thêm credential, không đổi `orientation_only` thành `false` và không dùng output
này làm evidence E1+.

```bash
python orientation/o00/run_o00.py --validate
python orientation/o00/run_o00.py
```

Bạn quan sát chain `Observation → HumanPrediction → BotDecision → DRY_RUN →
Outcome → Evaluation → ChangeProposal(PENDING_REVIEW)`. Mọi record synthetic,
replay idempotent và không có external action; sau đó mở
`../../docs/O00-SAFE-SYNTHETIC-WALKTHROUGH.md`.
