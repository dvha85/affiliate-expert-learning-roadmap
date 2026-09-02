# Quyền riêng tư và bằng chứng người học

Tài liệu này áp dụng cho O00 và mọi Mission v2. Nó không phải tư vấn pháp lý;
trước hành động thật phải kiểm tra policy/pháp lý hiện hành cho channel và địa
phương liên quan theo [Freshness Policy](FRESHNESS-POLICY.md).

## Default an toàn

```text
raw personal/account/analytics export → local private storage
redacted evidence summary + provenance/checksum/reference → repository khi cần review
secret/credential/token → never commit, never paste into prompt/log
```

`workspace/artifacts/local/`, `workspace/artifacts/private/`,
`workspace/artifacts/missions/*/private/` và `workspace/artifacts/missions/*/raw/`
bị ignore. Điều này không biến dữ liệu thành an toàn tự động: learner vẫn chịu
trách nhiệm kiểm redaction trước share/commit.

## Phân loại dữ liệu trước khi lưu hoặc gửi downstream

| Class | Ví dụ | Default repo action |
|---|---|---|
| Public product evidence | URL công khai, claim/product price | redacted summary có source + observed_at |
| Account/channel data | dashboard ID, handle, settings | local/private; chỉ share reference tối thiểu |
| Personal/customer data | email, name, click/user-level export | không commit; aggregate/redact hoặc secure store |
| Secret | token, cookie, password, API key | không commit, không prompt/log |
| Synthetic/test | fixture dựng để kiểm behavior | được commit nếu gắn nhãn rõ |

## DataAccessContext

Khi một task có personal/customer/account data, dùng
[template](../templates/DATA-ACCESS-CONTEXT.md) để ghi purpose, minimum data,
retention, downstream sharing và redaction. Public product observation nhỏ
không cần paperwork đầy đủ nếu không có dữ liệu nhạy cảm.

## Evidence review checklist

1. Có secret, token, cookie, email, ID người dùng, raw export hoặc screenshot
   nhạy cảm không? Nếu có, chuyển ra private/local và redact.
2. Có đủ `source_url`/reference, `observed_at`, access method, evidence kind
   và limitation để reviewer hiểu mà không cần raw data không?
3. Có thể dùng aggregate, hash hoặc safe reference thay raw value không?
4. Khi gửi sang model, workflow, tool hay log service: downstream thật sự cần
   field này không và policy/basis có còn hợp lệ không?
5. Retention/deletion khi Mission kết thúc đã rõ chưa?

`scripts/validate_privacy_boundary.py` chỉ phát hiện một số marker/secret rất
cơ bản. Nó không thể chứng minh legal compliance hay redaction hoàn hảo.
