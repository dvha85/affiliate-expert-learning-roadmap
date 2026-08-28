package ingest

import (
	"strings"
	"testing"
)

func TestProductsJSONValid(t *testing.T) {
	input := `[{"id":"p1","name":"Product","price":10,"commission_rate":0.1,"conversion_potential":0.2}]`
	products, err := ProductsJSON(strings.NewReader(input))
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if len(products) != 1 || products[0].ID != "p1" {
		t.Fatalf("unexpected products: %#v", products)
	}
}

func TestProductsJSONMalformed(t *testing.T) {
	if _, err := ProductsJSON(strings.NewReader(`[{`)); err == nil {
		t.Fatal("expected malformed JSON error")
	}
}

func TestProductsJSONRejectsInvalidProduct(t *testing.T) {
	input := `[{"id":"","name":"Product","price":10,"commission_rate":0.1,"conversion_potential":0.2}]`
	if _, err := ProductsJSON(strings.NewReader(input)); err == nil {
		t.Fatal("expected validation error")
	}
}

func TestProductsJSONRejectsUnknownField(t *testing.T) {
	input := `[{"id":"p1","name":"Product","price":10,"commission_rate":0.1,"conversion_potential":0.2,"unexpected":true}]`
	if _, err := ProductsJSON(strings.NewReader(input)); err == nil {
		t.Fatal("expected unknown-field error")
	}
}

func TestProductsJSONRejectsTrailingJSONValue(t *testing.T) {
	input := `[{"id":"p1","name":"Product","price":10,"commission_rate":0.1,"conversion_potential":0.2}] {"extra":true}`
	if _, err := ProductsJSON(strings.NewReader(input)); err == nil {
		t.Fatal("expected trailing JSON error")
	}
}

func TestProductsJSONRejectsTrailingGarbage(t *testing.T) {
	input := `[{"id":"p1","name":"Product","price":10,"commission_rate":0.1,"conversion_potential":0.2}] trailing`
	if _, err := ProductsJSON(strings.NewReader(input)); err == nil {
		t.Fatal("expected trailing content error")
	}
}
