package decision

import (
	"testing"

	"github.com/dvha85/affiliate-expert-learning-roadmap/lab/learner/affiliate-bot/internal/observation"
)

func TestBaselineRanksByCommissionPerOrderThenID(t *testing.T) {
	price100, price50, price20 := 100.0, 50.0, 20.0
	rate10, rate20 := 0.1, 0.2
	records := []observation.Record{
		{ID: "B", Price: &price100, Currency: "TEST", CommissionRate: &rate10},
		{ID: "A", Price: &price50, Currency: "TEST", CommissionRate: &rate20},
		{ID: "C", Price: &price20, Currency: "TEST", CommissionRate: &rate10},
	}

	got := Baseline(records)
	if got[0].Observation.ID != "A" || got[1].Observation.ID != "B" {
		t.Fatalf("expected deterministic A/B tie order, got %s/%s", got[0].Observation.ID, got[1].Observation.ID)
	}
}

func TestEvaluateUsesConcreteSafeStates(t *testing.T) {
	price, rate := 10.0, 0.1
	synthetic := observation.Record{
		ID: "A", ProductName: "A", SourceURL: "sample://a",
		ObservedAt: "2026-01-01T00:00:00Z", AccessMethod: observation.AccessSyntheticFixture,
		EvidenceKind: observation.EvidenceSynthetic, Price: &price, Currency: "TEST", CommissionRate: &rate,
	}
	if got := Evaluate([]observation.Record{synthetic}).State; got != StateRankScenario {
		t.Fatalf("expected scenario state, got %s", got)
	}

	missing := synthetic
	missing.Price = nil
	if got := Evaluate([]observation.Record{missing}).State; got != StateGetMoreData {
		t.Fatalf("expected get-more-data state, got %s", got)
	}

	duplicate := synthetic
	if got := Evaluate([]observation.Record{synthetic, duplicate}).State; got != StateHumanReview {
		t.Fatalf("expected human-review state, got %s", got)
	}

	// This is a unit-test schema case, not Reality evidence.
	real := synthetic
	real.SourceURL = "https://example.test/product-a"
	real.AccessMethod = observation.AccessPublicManual
	real.EvidenceKind = observation.EvidenceReal
	real.Currency = "VND"
	result := Evaluate([]observation.Record{real})
	if result.State != StateRecommend || result.EvidenceMode != observation.EvidenceReal {
		t.Fatalf("expected real/recommend result, got mode=%s state=%s", result.EvidenceMode, result.State)
	}

	otherCurrency := synthetic
	otherCurrency.ID = "B"
	otherCurrency.Currency = "OTHER"
	if got := Evaluate([]observation.Record{synthetic, otherCurrency}).State; got != StateHumanReview {
		t.Fatalf("expected mixed-currency human review, got %s", got)
	}
}
