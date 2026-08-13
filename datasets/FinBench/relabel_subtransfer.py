import argparse
import os
import random
import sys


def main() -> None:
    ap = argparse.ArgumentParser(description="Split transfer edges into N distinct sub-labels subtransfer1..N.")
    ap.add_argument("input", help="AccountTransferAccount.csv (label=transfer)")
    ap.add_argument("n", type=int, help="number of distinct sub-labels N (>=1)")
    ap.add_argument("--outdir", default=".",
                    help="output directory for subtransfer_i.csv (default: cwd)")
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()
    if args.n < 1:
        sys.exit("N must be >= 1")

    rng = random.Random(args.seed)
    with open(args.input, "r", encoding="utf-8") as f:
        header = f.readline()
        rows = f.readlines()

    buckets = [[] for _ in range(args.n)]
    for r in rows:
        buckets[rng.randrange(args.n)].append(r)

    os.makedirs(args.outdir, exist_ok=True)
    total = 0
    for i, b in enumerate(buckets, 1):
        out = os.path.join(args.outdir, f"subtransfer{i}.csv")
        with open(out, "w", encoding="utf-8") as o:
            o.write(header)
            o.writelines(b)
        total += len(b)
        print(f"subtransfer{i}: {len(b)} edges -> {out}")
    print(f"# total {total} edges across {args.n} sub-labels (edge set unchanged)")


if __name__ == "__main__":
    main()
