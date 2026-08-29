package observation

import (
	"encoding/json"
	"fmt"
	"net/url"
	"os"
	"strings"
	"time"
)

const (
	AccessSyntheticFixture = "synthetic_fixture"
	AccessPublicManual     = "public_manual"
	EvidenceSynthetic      = "synthetic"
	EvidenceReal           = "real"
)

// Record is the small, canonical M00 machine-readable observation. Pointer
// numbers preserve the difference between a missing value and an observed 0.
// M01 later hardens schema/normalization and adds history.
type Record struct {
	ID                 string   `json:"observation_id"`
	ProductName        string   `json:"product_name"`
	SourceURL          string   `json:"source_url"`
	ObservedAt         string   `json:"observed_at"`
	AccessMethod       string   `json:"access_method"`
	EvidenceKind       string   `json:"evidence_kind"`
	Price              *float64 `json:"price"`
	Currency           string   `json:"currency"`
	CommissionRate     *float64 `json:"commission_rate"`
	OtherVisibleSignal string   `json:"other_visible_signal,omitempty"`
	MissingFields      []string `json:"missing_fields,omitempty"`
	Notes              string   `json:"notes,omitempty"`
}

func Load(path string) ([]Record, error) {
	data, err := os.ReadFile(path)
	if err != nil {
		return nil, fmt.Errorf("read observations: %w", err)
	}

	var records []Record
	if err := json.Unmarshal(data, &records); err != nil {
		return nil, fmt.Errorf("decode observations: %w", err)
	}
	if len(records) == 0 {
		return nil, fmt.Errorf("decode observations: empty dataset")
	}
	return records, nil
}

// DecisionIssues is the deliberately small M00 evidence gate. It prevents a
// missing number from silently becoming 0 and prevents a sample:// fixture
// from being relabelled as real evidence. Full ingest validation belongs to
// M01; this helper only answers whether a record may enter the first ranking.
func (r Record) DecisionIssues() []string {
	issues := make([]string, 0)
	if strings.TrimSpace(r.ID) == "" {
		issues = append(issues, "missing observation_id")
	}
	if strings.TrimSpace(r.ProductName) == "" {
		issues = append(issues, "missing product_name")
	}
	if strings.TrimSpace(r.SourceURL) == "" {
		issues = append(issues, "missing source_url")
	}
	if _, err := time.Parse(time.RFC3339, r.ObservedAt); err != nil {
		issues = append(issues, "observed_at must be RFC3339")
	}

	switch r.EvidenceKind {
	case EvidenceSynthetic:
		if r.AccessMethod != AccessSyntheticFixture {
			issues = append(issues, "synthetic evidence requires access_method=synthetic_fixture")
		}
		if !strings.HasPrefix(r.SourceURL, "sample://") {
			issues = append(issues, "synthetic evidence requires a sample:// source")
		}
	case EvidenceReal:
		if r.AccessMethod != AccessPublicManual {
			issues = append(issues, "real M00 evidence requires access_method=public_manual")
		}
		parsed, err := url.Parse(r.SourceURL)
		if err != nil || (parsed.Scheme != "http" && parsed.Scheme != "https") || parsed.Host == "" {
			issues = append(issues, "real evidence requires a concrete http(s) source_url")
		}
	default:
		issues = append(issues, "evidence_kind must be synthetic or real")
	}

	if r.Price == nil {
		issues = append(issues, "missing price")
	} else if *r.Price < 0 {
		issues = append(issues, "price must not be negative")
	}
	if strings.TrimSpace(r.Currency) == "" {
		issues = append(issues, "missing currency")
	}
	if r.CommissionRate == nil {
		issues = append(issues, "missing commission_rate")
	} else if *r.CommissionRate < 0 || *r.CommissionRate > 1 {
		issues = append(issues, "commission_rate must be between 0 and 1")
	}
	return issues
}
