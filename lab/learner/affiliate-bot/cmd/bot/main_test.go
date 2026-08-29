package main

import (
	"bytes"
	"strings"
	"testing"
)

func TestDataPathUsesOptionalArgument(t *testing.T) {
	if got := dataPath([]string{"bot"}); got != "data/m00-observations.json" {
		t.Fatalf("unexpected default path: %q", got)
	}
	if got := dataPath([]string{"bot", "custom.json"}); got != "custom.json" {
		t.Fatalf("unexpected custom path: %q", got)
	}
}

func TestRunShowsSafeStarterState(t *testing.T) {
	var out bytes.Buffer
	if err := run([]string{"bot", "../../data/m00-observations.json"}, &out); err != nil {
		t.Fatal(err)
	}
	for _, want := range []string{"Bot version: pre-v0.1", "Evidence kind: synthetic", "Decision state: RANK_SCENARIO", "Missing evidence: none"} {
		if !strings.Contains(out.String(), want) {
			t.Fatalf("output missing %q:\n%s", want, out.String())
		}
	}
}
