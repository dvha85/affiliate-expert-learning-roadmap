package main

import (
	"fmt"
	"io"
	"os"

	"github.com/dvha85/affiliate-expert-learning-roadmap/lab/learner/affiliate-bot/internal/decision"
	"github.com/dvha85/affiliate-expert-learning-roadmap/lab/learner/affiliate-bot/internal/observation"
)

const formulaVersion = "commission-per-order/v1"

func dataPath(args []string) string {
	if len(args) > 1 {
		return args[1]
	}
	return "data/m00-observations.json"
}

func evidenceKindExplanation(kind string) string {
	switch kind {
	case observation.EvidenceSynthetic:
		return "dữ liệu tổng hợp dùng để kiểm thử"
	case observation.EvidenceReal:
		return "bằng chứng quan sát từ nguồn thật"
	case "mixed":
		return "đang trộn bằng chứng thật và dữ liệu tổng hợp; cần người kiểm tra"
	default:
		return "chưa xác định được loại bằng chứng"
	}
}

func decisionStateExplanation(state decision.State) string {
	switch state {
	case decision.StateRankScenario:
		return "xếp hạng kịch bản; chưa phải khuyến nghị hay quyền hành động"
	case decision.StateGetMoreData:
		return "chưa đủ bằng chứng; cần thu thập thêm dữ liệu"
	case decision.StateHumanReview:
		return "có xung đột hoặc rủi ro diễn giải; cần người kiểm tra"
	default:
		return "trạng thái chưa có diễn giải"
	}
}

func run(args []string, out io.Writer) error {
	records, err := observation.Load(dataPath(args))
	if err != nil {
		return err
	}
	result := decision.Evaluate(records)

	fmt.Fprintln(out, "Affiliate Bot đang khởi động...")
	fmt.Fprintln(out, "Phiên bản Bot (Bot version): v0.1 deterministic baseline")
	fmt.Fprintf(out, "Loại bằng chứng (Evidence kind): %s (%s)\n", result.EvidenceMode, evidenceKindExplanation(result.EvidenceMode))
	fmt.Fprintf(out, "Số quan sát (Observations) đã nạp: %d\n", len(records))
	fmt.Fprintf(out, "Phiên bản công thức (Formula version): %s\n", formulaVersion)
	fmt.Fprintln(out, "Giới hạn đường cơ sở (Baseline limitation): chưa xét khả năng chuyển đổi (Conversion potential), mức phù hợp với nhóm mục tiêu (Audience fit) và rủi ro hoàn/hủy (Refund risk).")
	fmt.Fprintln(out, "Xếp hạng đường cơ sở (Baseline ranking — hiện chỉ dựa trên hoa hồng mỗi đơn):")
	for i, item := range result.Ranked {
		fmt.Fprintf(out, "%d. %s | điểm (score)=%.2f\n", i+1, item.Observation.ProductName, item.Score)
	}
	fmt.Fprintf(out, "Trạng thái quyết định (Decision state): %s (%s)\n", result.State, decisionStateExplanation(result.State))
	if len(result.MissingEvidence) == 0 {
		fmt.Fprintln(out, "Bằng chứng còn thiếu (Missing evidence): không có theo yêu cầu của baseline hiện tại; business evidence vẫn có thể chưa đủ")
	} else {
		fmt.Fprintln(out, "Bằng chứng còn thiếu (Missing evidence):")
		for _, issue := range result.MissingEvidence {
			fmt.Fprintf(out, "- %s\n", issue)
		}
	}
	fmt.Fprintln(out, "Authority boundary: real evidence không tự nâng RANK_SCENARIO thành RECOMMEND; output này không phải approval hay execution permission.")
	fmt.Fprintln(out, "Khoảng trống tiếp theo (Next gap): so sánh scenario với Human DecisionPacket và ghi assumption/missing evidence cần đo tiếp.")
	return nil
}

func main() {
	if err := run(os.Args, os.Stdout); err != nil {
		fmt.Fprintf(os.Stderr, "Bot không thể tiếp tục: %v\n", err)
		os.Exit(1)
	}
}
