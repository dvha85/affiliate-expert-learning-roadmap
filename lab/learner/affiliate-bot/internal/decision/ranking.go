package decision

import (
	"fmt"
	"sort"

	"github.com/dvha85/affiliate-expert-learning-roadmap/lab/learner/affiliate-bot/internal/observation"
)

type Ranked struct {
	Observation observation.Record
	Score       float64
}

type State string

const (
	StateRankScenario State = "RANK_SCENARIO"
	StateGetMoreData  State = "GET_MORE_DATA"
	StateHumanReview  State = "HUMAN_REVIEW"
)

type Result struct {
	State           State
	EvidenceMode    string
	Ranked          []Ranked
	MissingEvidence []string
}

// Baseline xếp hạng chỉ theo hoa hồng mỗi đơn. Đây là weak scenario của M01,
// không phải business recommendation và không tạo execution permission.
func Baseline(records []observation.Record) []Ranked {
	ranked := make([]Ranked, 0, len(records))
	for _, record := range records {
		if record.Price == nil || record.CommissionRate == nil {
			continue
		}
		ranked = append(ranked, Ranked{
			Observation: record,
			Score:       *record.Price * *record.CommissionRate,
		})
	}
	sort.SliceStable(ranked, func(i, j int) bool {
		if ranked[i].Score == ranked[j].Score {
			return ranked[i].Observation.ID < ranked[j].Observation.ID
		}
		return ranked[i].Score > ranked[j].Score
	})
	return ranked
}

// Evaluate áp dụng safe decision states của deterministic M01 baseline.
// Evidence origin ảnh hưởng provenance, nhưng KHÔNG tự nâng RANK_SCENARIO thành
// RECOMMEND. Thiếu/xung đột evidence phải abstain/review rõ ràng.
func Evaluate(records []observation.Record) Result {
	eligible := make([]observation.Record, 0, len(records))
	issues := make([]string, 0)
	seen := make(map[string]struct{}, len(records))
	currencies := make(map[string]struct{})
	hasReal := false
	hasSynthetic := false
	hasConflict := false

	for _, record := range records {
		if _, exists := seen[record.ID]; exists && record.ID != "" {
			hasConflict = true
			issues = append(issues, fmt.Sprintf("%s: observation_id bị trùng", record.ID))
		}
		seen[record.ID] = struct{}{}

		switch record.EvidenceKind {
		case observation.EvidenceReal:
			hasReal = true
		case observation.EvidenceSynthetic:
			hasSynthetic = true
		}

		recordIssues := record.DecisionIssues()
		if len(recordIssues) > 0 {
			for _, issue := range recordIssues {
				issues = append(issues, fmt.Sprintf("%s: %s", record.ID, issue))
			}
			continue
		}
		currencies[record.Currency] = struct{}{}
		eligible = append(eligible, record)
	}
	if len(currencies) > 1 {
		hasConflict = true
		issues = append(issues, "không thể xếp hạng theo price khi có nhiều currency trong cùng một lần so sánh")
	}

	result := Result{Ranked: Baseline(eligible), MissingEvidence: issues}
	switch {
	case hasReal && hasSynthetic:
		result.EvidenceMode = "mixed"
	case hasReal:
		result.EvidenceMode = observation.EvidenceReal
	case hasSynthetic:
		result.EvidenceMode = observation.EvidenceSynthetic
	default:
		result.EvidenceMode = "unknown"
	}

	switch {
	case hasConflict || (hasReal && hasSynthetic):
		result.State = StateHumanReview
	case len(eligible) == 0 || len(issues) > 0:
		result.State = StateGetMoreData
	default:
		result.State = StateRankScenario
	}
	return result
}
