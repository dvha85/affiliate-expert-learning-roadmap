# O00 — Safe Synthetic Walkthrough

O00 là orientation tối đa 30 phút cho người mới nhìn thấy một decision loop
hoàn chỉnh trước M00. Nó **không phải Mission**, không có checklist PASS, không
đòi account/Go/API key và không tạo external side effect.

## Mục tiêu

```text
synthetic observation
→ human note
→ deterministic recommendation state
→ no action
→ explicit missing evidence
→ next measurement
```

Sau O00, learner hiểu lý do M00 bắt đầu bằng human market loop thay vì gọi AI
hoặc viết Bot: output synthetic chỉ chứng minh shape/safety của luồng, không
chứng minh product, audience hay market truth.

## Chạy demo

Từ repository root:

```bash
python orientation/o00/run_o00.py
python scripts/validate_o00.py
```

Kết quả phải cho thấy `evidence_kind: synthetic`, `recommended_state:
GET_MORE_DATA`, `action: null` và `orientation_only: true`. Nếu sửa fixture để
đề xuất publish/execute hoặc đổi synthetic thành real, validator phải fail.

## Chuyển sang M00

O00 không tạo credit/lesson/Mission PASS. Chỉ khi learner có public observation
thật, human review và human manual publish với disclosure/tracking phù hợp mới
được bắt đầu evidence M00. Dùng [privacy boundary](PRIVACY-AND-LEARNER-EVIDENCE.md)
khi lưu bất kỳ screenshot/export/account evidence nào.
