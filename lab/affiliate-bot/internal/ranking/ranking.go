package ranking

import (
	"sort"

	"github.com/dvha85/affiliate-expert-learning-roadmap/lab/affiliate-bot/internal/product"
)

type Ranked struct {
	Product product.Product
	Score   float64
}

func ByCommissionRate(products []product.Product) []Ranked {
	return rank(products, func(p product.Product) float64 { return p.CommissionRate })
}

func ByExpectedValue(products []product.Product) []Ranked {
	return rank(products, func(p product.Product) float64 {
		return p.Price * p.CommissionRate * p.ConversionPotential
	})
}

func rank(products []product.Product, score func(product.Product) float64) []Ranked {
	out := make([]Ranked, 0, len(products))
	for _, p := range products {
		out = append(out, Ranked{Product: p, Score: score(p)})
	}
	sort.SliceStable(out, func(i, j int) bool {
		if out[i].Score == out[j].Score {
			return out[i].Product.ID < out[j].Product.ID
		}
		return out[i].Score > out[j].Score
	})
	return out
}
