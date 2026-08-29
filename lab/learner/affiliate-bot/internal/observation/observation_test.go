package observation

import (
	"os"
	"path/filepath"
	"testing"
)

func TestLoadRejectsEmptyDataset(t *testing.T) {
	path := filepath.Join(t.TempDir(), "empty.json")
	if err := os.WriteFile(path, []byte("[]"), 0o600); err != nil {
		t.Fatal(err)
	}

	if _, err := Load(path); err == nil {
		t.Fatal("expected empty dataset error")
	}
}

func TestDecisionIssuesKeepMissingDifferentFromObservedZero(t *testing.T) {
	zero := 0.0
	rate := 0.1
	base := Record{
		ID: "A", ProductName: "A", SourceURL: "sample://a",
		ObservedAt: "2026-01-01T00:00:00Z", AccessMethod: AccessSyntheticFixture,
		EvidenceKind: EvidenceSynthetic, Price: &zero, Currency: "TEST", CommissionRate: &rate,
	}
	if issues := base.DecisionIssues(); len(issues) != 0 {
		t.Fatalf("observed zero must not be treated as missing: %v", issues)
	}
	base.Price = nil
	if issues := base.DecisionIssues(); !contains(issues, "missing price") {
		t.Fatalf("expected missing price issue, got %v", issues)
	}
}

func TestDecisionIssuesRejectRelabelledSampleAsReal(t *testing.T) {
	price, rate := 10.0, 0.1
	record := Record{
		ID: "A", ProductName: "A", SourceURL: "sample://a",
		ObservedAt: "2026-01-01T00:00:00Z", AccessMethod: AccessSyntheticFixture,
		EvidenceKind: EvidenceReal, Price: &price, Currency: "TEST", CommissionRate: &rate,
	}
	if len(record.DecisionIssues()) == 0 {
		t.Fatal("expected real-evidence consistency issues")
	}
}

func contains(values []string, want string) bool {
	for _, value := range values {
		if value == want {
			return true
		}
	}
	return false
}
