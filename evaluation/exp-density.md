# Exp-8: Density Sensitivity

Varies the average transfer out-degree on FinBench-SF10 by row-sampling the transfer edges with [`edge_sample.py`](../datasets/FinBench/edge_sample.py) (p ∈ {0.25, 0.5, 1.0, 2.0}) and re-importing under the same scale factor: the persisted SF10 graph is overwritten in place, so the existing Q1 benchmark is reused unchanged.
Vertex tables and all other edges (signIn, own, deposit, ...) stay fixed, so only the transfer density varies. P3 (GQL/SW, on-the-fly) vs GU (post-filter). The default query is Q1 (1–3 hop transfer chains); a 1–4 hop variant is also reported.

## Reproduction

Run on a converted FinBench-SF10 snapshot. For each p ∈ {2.0, 1.0, 0.5, 0.25}:

```bash
python3 datasets/FinBench/edge_sample.py snapshot/AccountTransferAccount.orig.csv 0.5 \
    --out snapshot/AccountTransferAccount.csv
```

## FinBench-SF10, 1–3 hop (ms)

| p | transfer out-degree | P3 (ms) | GU (ms) | speedup |
| --- | --- | --- | --- | --- |
| 0.25 | 0.97 | 512.43 | 603.18 | 1.18× |
| 0.5  | 1.94 | 631.27 | 821.84 | 1.30× |
| 1.0  | 3.88 | 1536.69 | 2181.61 | 1.42× |
| 2.0  | 7.76 | 4328.52 | 6829.07 | 1.58× |

## FinBench-SF10, 1–4 hop (ms)

Query: Q1 with `{1,3}` widened to `{1,4}`; all else unchanged.

| p | transfer out-degree | P3 (ms) | GU (ms) | speedup |
| --- | --- | --- | --- | --- |
| 0.25 | 0.97 | 574 | 701 | 1.22× |
| 0.5  | 1.94 | 883 | 1229 | 1.39× |
| 1.0  | 3.88 | 2925 | 4526 | 1.55× |
| 2.0  | 7.76 | 11512 | 19854 | 1.72× |
