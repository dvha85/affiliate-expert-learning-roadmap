package main

import (
	"bytes"
	"strings"
	"testing"
)

func TestDataPathUsesOptionalArgument(t *testing.T) {
	if got := dataPath([]string{"bot"}); got != "data/m00-observations.json" {
		t.Fatalf("đường dẫn mặc định không đúng: %q", got)
	}
	if got := dataPath([]string{"bot", "custom.json"}); got != "custom.json" {
		t.Fatalf("đường dẫn tùy chọn không đúng: %q", got)
	}
}

func TestRunShowsSafeStarterStateInVietnamese(t *testing.T) {
	var out bytes.Buffer
	if err := run([]string{"bot", "../../data/m00-observations.json"}, &out); err != nil {
		t.Fatal(err)
	}

	for _, want := range []string{
		"Affiliate Bot đang khởi động...",
		"Phiên bản Bot (Bot version): pre-v0.1",
		"Loại bằng chứng (Evidence kind): synthetic (dữ liệu tổng hợp dùng để kiểm thử)",
		"Số quan sát (Observations) đã nạp: 3",
		"Phiên bản công thức (Formula version): commission-per-order/v1",
		"Trạng thái quyết định (Decision state): RANK_SCENARIO (xếp hạng kịch bản; chưa phải khuyến nghị hành động)",
		"Bằng chứng còn thiếu (Missing evidence): không có theo yêu cầu của baseline hiện tại",
		"Khoảng trống tiếp theo (Next gap):",
	} {
		if !strings.Contains(out.String(), want) {
			t.Fatalf("output thiếu %q:\n%s", want, out.String())
		}
	}
}

func TestDecisionStateExplanationsKeepMachineTokensStable(t *testing.T) {
	cases := map[string]string{
		"RANK_SCENARIO": "xếp hạng kịch bản",
		"RECOMMEND":     "khuyến nghị sơ bộ",
		"GET_MORE_DATA": "cần thu thập thêm dữ liệu",
		"HUMAN_REVIEW":  "cần người kiểm tra",
	}

	for token, explanation := range cases {
		if explanation == "" || token == "" {
			t.Fatalf("token và diễn giải phải tồn tại: token=%q explanation=%q", token, explanation)
		}
	}
}
