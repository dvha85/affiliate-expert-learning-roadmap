# M02 Go builder profile — golden oracle

`main.go` is a dependency-free Go implementation of exactly the Operator rule
card. It is not a prerequisite for M00 and never publishes, fetches data,
calls AI/tools or writes history.

```bash
cd starter-kits/M02-go-builder
go run main.go ../../evals/cases/m02/valid.json
```

CI compares this output with the Operator profile for every shared fixture.
