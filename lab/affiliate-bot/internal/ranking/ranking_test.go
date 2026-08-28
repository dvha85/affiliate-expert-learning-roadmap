package ranking

import (
	"testing"

	"github.com/dvha85/affiliate-expert-learning-roadmap/lab/affiliate-bot/internal/product"
)

func TestExpectedValueCanChangeTopProduct(t *testing.T) {
	products := []product.Product{
		{ID: "A", Name: "A", Price: 20, CommissionRate: 0.30, ConversionPotential: 0.02},
		{ID: "B", Name: "B", Price: 80, CommissionRate: 0.12, ConversionPotential: 0.08},
	}
	commission := ByCommissionRate(products)
	ev := ByExpectedValue(products)
	if commission[0].Product.ID != "A" {
		t.Fatalf("expected commission-only top A, got %s", commission[0].Product.ID)
	}
	if ev[0].Product.ID != "B" {
		t.Fatalf("expected EV top B, got %s", ev[0].Product.ID)
	}
}

func TestRankingTieBreakIsDeterministic(t *testing.T) {
	products := []product.Product{
		{ID: "B", Name: "B", Price: 10, CommissionRate: 0.10, ConversionPotential: 0.10},
		{ID: "A", Name: "A", Price: 10, CommissionRate: 0.10, ConversionPotential: 0.10},
	}
	got := ByExpectedValue(products)
	if got[0].Product.ID != "A" {
		t.Fatalf("expected ID tie-break A first, got %s", got[0].Product.ID)
	}
}
