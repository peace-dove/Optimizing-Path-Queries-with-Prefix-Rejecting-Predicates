# Exp-8: Label-Count Sensitivity

Tests whether the distinct edge-label count affects P3's on-the-fly (GQL/SW) gain over GU (post-filter) on FinBench-SF10. The transfer edges are re-partitioned into N same-semantic sub-labels `subtransfer1..N` with [`relabel_subtransfer.py`](../datasets/FinBench/relabel_subtransfer.py) (N ∈ {1, 2, 3}); the edge set and the candidate-path count stays fixed, so only the distinct-label count varies. N=1 is the original `transfer` label (Exp-1's Q1). Queries ([`queries/FinBench/labels/`](../queries/FinBench/labels/)) use label alternation `subtransfer1|…|N`; the `isAsc`/SW(2) predicate is unchanged.

## Reproduction

Relabel the transfer edges into N sub-labels:

```bash
python3 datasets/FinBench/relabel_subtransfer.py snapshot/AccountTransferAccount.csv 3 --outdir snapshot
```

Then register `subtransfer1..N` as edge labels in the import config, re-import, and run the Q1-form query with label alternation.

## FinBench-SF10 (ms)

| distinct labels | P3 (ms) | GU (ms) | speedup | change vs N=1 |
| --- | --- | --- | --- | --- |
| 1 (transfer) | 1536.69 | 2181.61 | 1.42× | — |
| 2 (subtransfer1\|2) | 1561.31 | 2218.07 | 1.42× | 1.6% |
| 3 (subtransfer1\|2\|3) | 1565.89 | 2221.43 | 1.42× | 1.9% |
