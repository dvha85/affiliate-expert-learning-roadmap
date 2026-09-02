package main

import (
	"encoding/json"
	"fmt"
	"os"
	"sort"
)

const formulaVersion = "m02-price-times-commission-v0.1"

type Observation struct {
	SubjectID      string   `json:"subject_id"`
	ObservationID  string   `json:"observation_id"`
	SourceURL      string   `json:"source_url"`
	ObservedAt     string   `json:"observed_at"`
	EvidenceKind   string   `json:"evidence_kind"`
	Price          *float64 `json:"price"`
	Currency       string   `json:"currency"`
	CommissionRate *float64 `json:"commission_rate"`
	IdentityKey    string   `json:"identity_key"`
}

type Ranked struct {
	SubjectID string  `json:"subject_id"`
	Score     float64 `json:"score"`
}

type Result struct {
	FormulaVersion   string   `json:"formula_version"`
	AIOrToolCalled   bool     `json:"ai_or_tool_called"`
	Action           any      `json:"action"`
	EvidenceKinds    []string `json:"evidence_kinds"`
	RecommendedState string   `json:"recommended_state"`
	Reason           string   `json:"reason"`
	MissingEvidence  []string `json:"missing_evidence"`
	Ranking          []Ranked `json:"ranking"`
}

func result(state, reason string, kinds map[string]bool, missing []string, ranking []Ranked) Result {
	kindList := make([]string, 0, len(kinds))
	for kind := range kinds {
		kindList = append(kindList, kind)
	}
	sort.Strings(kindList)
	sort.Strings(missing)
	if ranking == nil {
		ranking = []Ranked{}
	}
	if missing == nil {
		missing = []string{}
	}
	return Result{formulaVersion, false, nil, kindList, state, reason, missing, ranking}
}

func evaluate(rows []Observation) Result {
	kinds := map[string]bool{}
	seen := map[string]bool{}
	identities := map[string]string{}
	currencies := map[string]bool{}
	missing := []string{}
	ranking := []Ranked{}
	for index, row := range rows {
		subject := row.SubjectID
		if subject == "" {
			subject = fmt.Sprintf("row-%d", index+1)
		}
		kinds[row.EvidenceKind] = true
		if row.ObservationID != "" && seen[row.ObservationID] {
			return result("HUMAN_REVIEW", "Duplicate observation_id requires human review.", kinds, []string{row.ObservationID + ": duplicate observation_id"}, nil)
		}
		seen[row.ObservationID] = true
		identity := row.IdentityKey
		if identity == "" {
			identity = subject
		}
		if previous, ok := identities[subject]; ok && previous != identity {
			return result("HUMAN_REVIEW", "Identity conflict requires human review.", kinds, []string{subject + ": conflicting identity_key"}, nil)
		}
		identities[subject] = identity
		fields := []string{}
		if row.SubjectID == "" {
			fields = append(fields, "subject_id")
		}
		if row.ObservationID == "" {
			fields = append(fields, "observation_id")
		}
		if row.SourceURL == "" {
			fields = append(fields, "source_url")
		}
		if row.ObservedAt == "" {
			fields = append(fields, "observed_at")
		}
		if row.Price == nil {
			fields = append(fields, "price")
		}
		if row.Currency == "" {
			fields = append(fields, "currency")
		}
		if row.CommissionRate == nil {
			fields = append(fields, "commission_rate")
		}
		if len(fields) > 0 {
			missing = append(missing, subject+": "+join(fields))
			continue
		}
		if row.EvidenceKind != "real" && row.EvidenceKind != "synthetic" {
			missing = append(missing, subject+": evidence_kind real or synthetic")
			continue
		}
		currencies[row.Currency] = true
		ranking = append(ranking, Ranked{subject, *row.Price * *row.CommissionRate})
	}
	if len(missing) > 0 {
		return result("GET_MORE_DATA", "Required evidence is missing or invalid; no ranking is emitted.", kinds, missing, nil)
	}
	if len(currencies) > 1 {
		return result("HUMAN_REVIEW", "Mixed currency requires human review.", kinds, []string{"currency: mixed comparison scope"}, nil)
	}
	sort.Slice(ranking, func(i, j int) bool {
		if ranking[i].Score == ranking[j].Score {
			return ranking[i].SubjectID < ranking[j].SubjectID
		}
		return ranking[i].Score > ranking[j].Score
	})
	return result("RANK_SCENARIO", "Deterministic price × commission_rate scenario; not execution permission.", kinds, nil, ranking)
}

func join(values []string) string {
	result := ""
	for index, value := range values {
		if index > 0 {
			result += ", "
		}
		result += value
	}
	return result
}

func main() {
	if len(os.Args) != 2 {
		fmt.Fprintln(os.Stderr, "usage: go run main.go observations.json")
		os.Exit(2)
	}
	data, err := os.ReadFile(os.Args[1])
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(2)
	}
	var rows []Observation
	if err := json.Unmarshal(data, &rows); err != nil {
		fmt.Fprintln(os.Stderr, "observations JSON must be a list:", err)
		os.Exit(2)
	}
	output, _ := json.Marshal(evaluate(rows))
	fmt.Println(string(output))
}
