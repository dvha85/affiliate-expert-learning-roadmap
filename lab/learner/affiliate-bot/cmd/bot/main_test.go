package main

import (
	"bytes"
	"strings"
	"testing"

	"github.com/dvha85/affiliate-expert-learning-roadmap/lab/learner/affiliate-bot/internal/decision"
)

func TestDataPathUsesOptionalArgument(t *testing.T) {
	if got := dataPath([]string{"bot"}); got != "data/m00-observations.json" {
		t.Fatalf("đường dẫn mặc định không đúng: %q", got)
	}
	if got := dataPath([]string{"bot", "custom.json"}); got != "custom.json" {
		t.Fatalf("đường dẫn tùy chọn không đúng: %q", got)
	}
}

func TestRunShowsSafeDeterministicBaselineInVietnamese(t *testing.T) {
	var out bytes.Buffer
	if err := run([]string{"bot", "../../data/m00-observations.json"}, &out); err != nil {
		t.Fatal(err)
	}

	for _, want := range []string{
		"Affiliate Bot đang khởi động...",
		"Phiên bản Bot (Bot version): v0.1 deterministic baseline",
		"Loại bằng chứng (Evidence kind): synthetic (dữ liệu tổng hợp dùng để kiểm thử)",
		"Số quan sát (Observations) đã nạp: 3",
		"Phiên bản công thức (Formula version): commission-per-order/v1",
		"Giới hạn đường cơ sở (Baseline limitation):",
		"khả năng chuyển đổi (Conversion potential)",
		"mức phù hợp với nhóm mục tiêu (Audience fit)",
		"rủi ro hoàn/hủy (Refund risk)",
		"Trạng thái quyết định (Decision state): RANK_SCENARIO (xếp hạng kịch bản; chưa phải khuyến nghị hay quyền hành động)",
		"Authority boundary: real evidence không tự nâng RANK_SCENARIO thành RECOMMEND",
		"Khoảng trống tiếp theo (Next gap):",
	} {
		if !strings.Contains(out.String(), want) {
			t.Fatalf("output thiếu %q:\n%s", want, out.String())
		}
	}
}

func TestDecisionStateExplanationsCoverStableMachineTokens(t *testing.T) {
	cases := []struct {
		state decision.State
		want  string
	}{
		{decision.StateRankScenario, "xếp hạng kịch bản"},
		{decision.StateGetMoreData, "cần thu thập thêm dữ liệu"},
		{decision.StateHumanReview, "cần người kiểm tra"},
	}

	for _, tc := range cases {
		got := decisionStateExplanation(tc.state)
		if !strings.Contains(got, tc.want) {
			t.Fatalf("state %s phải có diễn giải chứa %q, nhận được %q", tc.state, tc.want, got)
		}
	}
}
