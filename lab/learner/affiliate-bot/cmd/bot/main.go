package main

import (
	"fmt"
	"io"
	"os"

	"github.com/dvha85/affiliate-expert-learning-roadmap/lab/learner/affiliate-bot/internal/decision"
	"github.com/dvha85/affiliate-expert-learning-roadmap/lab/learner/affiliate-bot/internal/observation"
)

func dataPath(args []string) string {
	if len(args) > 1 {
		return args[1]
	}
	return "data/m00-observations.json"
}

func run(args []string, out io.Writer) error {
	records, err := observation.Load(dataPath(args))
	if err != nil {
		return err
	}
	result := decision.Evaluate(records)

	fmt.Fprintln(out, "Affiliate Bot starting...")
	fmt.Fprintln(out, "Bot version: pre-v0.1")
	fmt.Fprintf(out, "Evidence kind: %s\n", result.EvidenceMode)
	fmt.Fprintf(out, "Observations loaded: %d\n", len(records))
	fmt.Fprintln(out, "Baseline ranking (commission per order only):")
	for i, item := range result.Ranked {
		fmt.Fprintf(out, "%d. %s | score=%.2f\n", i+1, item.Observation.ProductName, item.Score)
	}
	fmt.Fprintf(out, "Decision state: %s\n", result.State)
	if len(result.MissingEvidence) == 0 {
		fmt.Fprintln(out, "Missing evidence: none")
	} else {
		fmt.Fprintln(out, "Missing evidence:")
		for _, issue := range result.MissingEvidence {
			fmt.Fprintf(out, "- %s\n", issue)
		}
	}
	fmt.Fprintln(out, "Next gap: save human ranking first, then compare reasons and weakest assumptions.")
	return nil
}

func main() {
	if err := run(os.Args, os.Stdout); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}
