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
	StateRecommend    State = "RECOMMEND"
	StateGetMoreData  State = "GET_MORE_DATA"
	StateHumanReview  State = "HUMAN_REVIEW"
)

type Result struct {
	State           State
	EvidenceMode    string
	Ranked          []Ranked
	MissingEvidence []string
}

// Baseline ranks by commission per order only. It is intentionally incomplete:
// M00 must expose its assumptions before the learner improves the decision.
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

// Evaluate applies the safe starter states used throughout M00. "Abstain" is
// the behavior family; GET_MORE_DATA and HUMAN_REVIEW are the concrete states.
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
			issues = append(issues, fmt.Sprintf("%s: duplicate observation_id", record.ID))
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
		issues = append(issues, "multiple currencies cannot share one price-based ranking")
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
	case hasReal:
		result.State = StateRecommend
	default:
		result.State = StateRankScenario
	}
	return result
}
