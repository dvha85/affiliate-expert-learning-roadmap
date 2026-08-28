package ingest

import (
	"encoding/json"
	"fmt"
	"io"

	"github.com/dvha85/affiliate-expert-learning-roadmap/lab/affiliate-bot/internal/product"
)

func ProductsJSON(r io.Reader) ([]product.Product, error) {
	var products []product.Product
	dec := json.NewDecoder(r)
	dec.DisallowUnknownFields()
	if err := dec.Decode(&products); err != nil {
		return nil, fmt.Errorf("decode products: %w", err)
	}

	var trailing any
	if err := dec.Decode(&trailing); err != io.EOF {
		if err == nil {
			return nil, fmt.Errorf("decode products: trailing JSON content is not allowed")
		}
		return nil, fmt.Errorf("decode products: trailing content: %w", err)
	}

	for i, p := range products {
		if err := p.Validate(); err != nil {
			return nil, fmt.Errorf("product[%d]: %w", i, err)
		}
	}
	return products, nil
}
