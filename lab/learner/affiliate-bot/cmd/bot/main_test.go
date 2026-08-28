package main

import "testing"

func TestStatusLinesContainV00AndOK(t *testing.T) {
	lines := statusLines()
	if len(lines) != 3 {
		t.Fatalf("expected 3 status lines, got %d", len(lines))
	}
	if lines[1] != "Bot version: v0.0" {
		t.Fatalf("unexpected version line: %q", lines[1])
	}
	if lines[2] != "Bot status: OK" {
		t.Fatalf("unexpected status line: %q", lines[2])
	}
}
