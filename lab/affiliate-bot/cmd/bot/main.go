package main

import (
	"fmt"
	"log"
	"os"

	"github.com/dvha85/affiliate-expert-learning-roadmap/lab/affiliate-bot/internal/ingest"
	"github.com/dvha85/affiliate-expert-learning-roadmap/lab/affiliate-bot/internal/ranking"
)

func main() {
	path := "data/sample-products.json"
	if len(os.Args) > 1 {
		path = os.Args[1]
	}

	f, err := os.Open(path)
	if err != nil {
		log.Fatalf("open product data: %v", err)
	}
	defer f.Close()

	products, err := ingest.ProductsJSON(f)
	if err != nil {
		log.Fatalf("ingest product data: %v", err)
	}

	fmt.Printf("Affiliate Bot starting...\n")
	fmt.Printf("Loaded products: %d\n", len(products))

	fmt.Println("\nCommission-only ranking:")
	for i, item := range ranking.ByCommissionRate(products) {
		fmt.Printf("%d. %s score=%.4f\n", i+1, item.Product.Name, item.Score)
	}

	fmt.Println("\nExpected-value ranking:")
	for i, item := range ranking.ByExpectedValue(products) {
		fmt.Printf("%d. %s score=%.4f\n", i+1, item.Product.Name, item.Score)
	}

	fmt.Println("\nBot status: OK")
}
