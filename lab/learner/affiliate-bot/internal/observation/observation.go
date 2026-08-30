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

// Record là observation (bản ghi quan sát) machine-readable tối giản của M00.
// Con trỏ số giữ khác biệt giữa giá trị thiếu và giá trị 0 được quan sát thật.
// M01 sẽ siết schema/normalization và bổ sung history.
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
		return nil, fmt.Errorf("không đọc được file observations: %w", err)
	}

	var records []Record
	if err := json.Unmarshal(data, &records); err != nil {
		return nil, fmt.Errorf("không giải mã được observations JSON: %w", err)
	}
	if len(records) == 0 {
		return nil, fmt.Errorf("không giải mã được observations JSON: tập dữ liệu rỗng")
	}
	return records, nil
}

// DecisionIssues là evidence gate (cổng bằng chứng) nhỏ có chủ đích ở M00.
// Nó ngăn số liệu thiếu âm thầm biến thành 0 và ngăn fixture sample:// bị đổi nhãn
// thành real evidence. Validation đầy đủ thuộc M01; helper này chỉ quyết định record
// có được đi vào phép xếp hạng đầu tiên hay không.
func (r Record) DecisionIssues() []string {
	issues := make([]string, 0)
	if strings.TrimSpace(r.ID) == "" {
		issues = append(issues, "thiếu observation_id")
	}
	if strings.TrimSpace(r.ProductName) == "" {
		issues = append(issues, "thiếu product_name")
	}
	if strings.TrimSpace(r.SourceURL) == "" {
		issues = append(issues, "thiếu source_url")
	}
	if _, err := time.Parse(time.RFC3339, r.ObservedAt); err != nil {
		issues = append(issues, "observed_at phải theo định dạng RFC3339")
	}

	switch r.EvidenceKind {
	case EvidenceSynthetic:
		if r.AccessMethod != AccessSyntheticFixture {
			issues = append(issues, "bằng chứng synthetic yêu cầu access_method=synthetic_fixture")
		}
		if !strings.HasPrefix(r.SourceURL, "sample://") {
			issues = append(issues, "bằng chứng synthetic yêu cầu source_url dạng sample://")
		}
	case EvidenceReal:
		if r.AccessMethod != AccessPublicManual {
			issues = append(issues, "bằng chứng real ở M00 yêu cầu access_method=public_manual")
		}
		parsed, err := url.Parse(r.SourceURL)
		if err != nil || (parsed.Scheme != "http" && parsed.Scheme != "https") || parsed.Host == "" {
			issues = append(issues, "bằng chứng real yêu cầu source_url http(s) cụ thể")
		}
	default:
		issues = append(issues, "evidence_kind phải là synthetic hoặc real")
	}

	if r.Price == nil {
		issues = append(issues, "thiếu price")
	} else if *r.Price < 0 {
		issues = append(issues, "price không được âm")
	}
	if strings.TrimSpace(r.Currency) == "" {
		issues = append(issues, "thiếu currency")
	}
	if r.CommissionRate == nil {
		issues = append(issues, "thiếu commission_rate")
	} else if *r.CommissionRate < 0 || *r.CommissionRate > 1 {
		issues = append(issues, "commission_rate phải nằm trong khoảng 0 đến 1")
	}
	return issues
}
