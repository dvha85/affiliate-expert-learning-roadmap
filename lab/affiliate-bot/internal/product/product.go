package product

import "fmt"

type Product struct {
	ID                  string  `json:"id"`
	Name                string  `json:"name"`
	Price               float64 `json:"price"`
	CommissionRate      float64 `json:"commission_rate"`
	ConversionPotential float64 `json:"conversion_potential"`
}

func (p Product) Validate() error {
	if p.ID == "" {
		return fmt.Errorf("product id is required")
	}
	if p.Name == "" {
		return fmt.Errorf("product name is required")
	}
	if p.Price < 0 {
		return fmt.Errorf("product price cannot be negative")
	}
	if p.CommissionRate < 0 || p.CommissionRate > 1 {
		return fmt.Errorf("commission_rate must be between 0 and 1")
	}
	if p.ConversionPotential < 0 || p.ConversionPotential > 1 {
		return fmt.Errorf("conversion_potential must be between 0 and 1")
	}
	return nil
}
