# Exp-8: Selectivity Sensitivity

Sweeps a `sum_lt($\theta$)` PRP predicate on `transfer.amount` over 1–3 hop transfer chains on FinBench-SF10, comparing P3 with GU. The threshold $\theta$ is varied so the filter ratio spans ~0% (zero pruning) to ~90%. Query templates are in [`queries/FinBench/selectivity/`](../queries/FinBench/selectivity/).

## FinBench-SF10 (ms)

| $\theta$ | filter ratio | P3 (ms) | GU (ms) | speedup |
| --- | --- | --- | --- | --- |
| 50M | 0% | 2450.87 | 2401.85 | 0.98× |
| 17M | 25% | 1950.18 | 2398.73 | 1.23× |
| 14M | 48% | 1703.61 | 2403.16 | 1.41× |
| 9.5M | 75% | 1444.36 | 2397.64 | 1.66× |
| 6M | 90% | 1364.82 | 2402.48 | 1.76× |
