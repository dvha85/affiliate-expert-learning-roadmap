# Workspace privacy — learner-local evidence

`workspace/`, raw analytics/export và learner-local data bị Git ignore. Đây là
boundary hỗ trợ learner, không phải permission để thu thập nhiều dữ liệu hơn
mức cần thiết.

## Được lưu local/private

- raw analytics/export, account/dashboard URL private, screenshot nhạy cảm;
- personal progress và blocker detail;
- credentials/secret **chỉ** trong password manager hoặc secret manager phù hợp,
  không trong repo/workspace template.

## Được commit sau review

- fixture synthetic/test/replay;
- redacted evidence summary/reference;
- contract/eval expected output không chứa raw account data.

Mọi external action M00 vẫn là `human_only`. Privacy boundary không biến Bot/AI
thành actor có quyền publish, đọc account hay execution.
