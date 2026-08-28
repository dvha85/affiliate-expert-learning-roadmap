package store

import (
	"testing"
	"time"

	"github.com/dvha85/affiliate-expert-learning-roadmap/lab/affiliate-bot/internal/product"
)

func TestMemoryRepositoryKeepsSnapshotHistory(t *testing.T) {
	r := NewMemoryRepository()
	p := product.Product{ID: "p1", Name: "P1", Price: 10, CommissionRate: 0.1, ConversionPotential: 0.2}
	t1 := time.Unix(100, 0).UTC()
	if err := r.SaveSnapshot(Snapshot{Product: p, CapturedAt: t1}); err != nil {
		t.Fatal(err)
	}
	p.Price = 99
	items := r.ListSnapshots("p1")
	if len(items) != 1 {
		t.Fatalf("expected 1 snapshot, got %d", len(items))
	}
	if items[0].Product.Price != 10 {
		t.Fatalf("history mutated: got %.2f", items[0].Product.Price)
	}
}

func TestMemoryRepositoryRejectsZeroCapturedAt(t *testing.T) {
	r := NewMemoryRepository()
	p := product.Product{ID: "p1", Name: "P1", Price: 10, CommissionRate: 0.1, ConversionPotential: 0.2}
	if err := r.SaveSnapshot(Snapshot{Product: p}); err == nil {
		t.Fatal("expected captured_at validation error")
	}
}
