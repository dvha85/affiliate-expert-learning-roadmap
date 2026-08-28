package store

import (
	"fmt"
	"sync"
	"time"

	"github.com/dvha85/affiliate-expert-learning-roadmap/lab/affiliate-bot/internal/product"
)

type Snapshot struct {
	Product    product.Product
	CapturedAt time.Time
}

type Repository interface {
	SaveSnapshot(Snapshot) error
	ListSnapshots(productID string) []Snapshot
}

type MemoryRepository struct {
	mu   sync.RWMutex
	data map[string][]Snapshot
}

func NewMemoryRepository() *MemoryRepository {
	return &MemoryRepository{data: make(map[string][]Snapshot)}
}

func (r *MemoryRepository) SaveSnapshot(s Snapshot) error {
	if err := s.Product.Validate(); err != nil {
		return fmt.Errorf("invalid snapshot product: %w", err)
	}
	if s.CapturedAt.IsZero() {
		return fmt.Errorf("captured_at is required")
	}
	r.mu.Lock()
	defer r.mu.Unlock()
	copyProduct := s.Product
	r.data[s.Product.ID] = append(r.data[s.Product.ID], Snapshot{Product: copyProduct, CapturedAt: s.CapturedAt})
	return nil
}

func (r *MemoryRepository) ListSnapshots(productID string) []Snapshot {
	r.mu.RLock()
	defer r.mu.RUnlock()
	items := r.data[productID]
	out := make([]Snapshot, len(items))
	copy(out, items)
	return out
}
