package main

import "fmt"

func statusLines() []string {
	return []string{
		"Affiliate Bot starting...",
		"Bot version: v0.0",
		"Bot status: OK",
	}
}

func main() {
	for _, line := range statusLines() {
		fmt.Println(line)
	}
}
