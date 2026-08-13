import argparse
import os
import sys


def sample_edges(in_path: str, p: float, out_path: str, seed: int) -> None:
    if not (p > 0.0):
        sys.exit(f"p must be > 0, got {p}")

    import random
    rng = random.Random(seed)
    base = int(p)
    frac = p - base

    with open(in_path, "r", encoding="utf-8") as fin, open(
        out_path, "w", encoding="utf-8"
    ) as fout:
        header = fin.readline()
        if not header:
            sys.exit(f"empty input file: {in_path}")
        fout.write(header)

        total = emitted = 0
        for line in fin:
            total += 1
            for _ in range(base):
                fout.write(line)
                emitted += 1
            if frac > 0.0 and rng.random() < frac:
                fout.write(line)
                emitted += 1

    actual_p = emitted / total if total else 0.0
    print(
        f"emitted {emitted}/{total} edges ({actual_p:.4f}, target p={p}) "
        f"-> {out_path}"
    )


def main() -> None:
    ap = argparse.ArgumentParser(description="Row-sample FinBench transfer edges at ratio p; p > 1 samples with replacement.")
    ap.add_argument("input", help="path to AccountTransferAccount.csv")
    ap.add_argument("p", type=float, help="sampling ratio > 0; p > 1 samples with replacement")
    ap.add_argument(
        "--out",
        default=None,
        help="output path (default: <dir>/<base>_p<NN>.csv)",
    )
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    if args.out is None:
        d, b = os.path.split(args.input)
        pct = int(round(args.p * 100))
        base, ext = os.path.splitext(b)
        args.out = os.path.join(d, f"{base}_p{pct}{ext}")

    sample_edges(args.input, args.p, args.out, args.seed)


if __name__ == "__main__":
    main()