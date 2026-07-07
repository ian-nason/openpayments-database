"""Publish openpayments.duckdb to the Nason/openpayments-database HF dataset."""
import argparse
import sys
from pathlib import Path

import duckdb
from huggingface_hub import HfApi, create_repo


def generate_dataset_card(db_path: str) -> str:
    con = duckdb.connect(db_path, read_only=True)
    metadata = con.sql(
        "SELECT table_name, description, row_count, column_count, date_range "
        "FROM _metadata ORDER BY row_count DESC"
    ).fetchdf()
    con.close()

    table_rows = "\n".join(
        f"| `{r['table_name']}` | {r['description']} | {r['row_count']:,} "
        f"| {r['column_count']} | {r['date_range']} |"
        for _, r in metadata.iterrows()
    )
    total_rows = int(metadata["row_count"].sum())

    return f"""---
license: mit
task_categories:
  - tabular-classification
  - tabular-regression
tags:
  - healthcare
  - medicare
  - open-payments
  - sunshine-act
  - pharma
  - conflicts-of-interest
pretty_name: CMS Open Payments (Sunshine Act) Database
size_categories:
  - 100M<n<1B
---

# Open Payments Database (CMS Sunshine Act)

Every disclosed industry payment to physicians, non-physician practitioners,
and teaching hospitals, program years 2013-2025, as a single queryable
DuckDB database. **{total_rows:,} rows.**

| Table | Description | Rows | Cols | Coverage |
|-------|-------------|------|------|----------|
{table_rows}

## Query it remotely

```sql
INSTALL httpfs; LOAD httpfs;
ATTACH 'https://huggingface.co/datasets/Nason/openpayments-database/resolve/main/openpayments.duckdb'
    AS op (READ_ONLY);

SELECT applicable_manufacturer_or_applicable_gpo_making_payment_name AS maker,
       ROUND(SUM(total_amount_of_payment_usdollars) / 1e6, 1) AS millions
FROM op.general_payments
WHERE program_year = 2024
GROUP BY 1 ORDER BY 2 DESC LIMIT 10;
```

Joins to the `cms-medicare` datapond database on NPI — see the GitHub README
for the worked Open Payments x Medicare utilization example and measured
join rates.

Or with the datapond package: `pip install datapond`, then
`datapond.connect('openpayments')`.

Build pipeline, per-era column crosswalks, and full documentation:
https://github.com/ian-nason/openpayments-database
"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", type=Path, default=Path("openpayments.duckdb"))
    parser.add_argument("--repo", default="Nason/openpayments-database")
    parser.add_argument("--token", help="HF token (or set HF_TOKEN env var)")
    args = parser.parse_args()

    if not args.db.exists():
        print(f"Error: {args.db} not found")
        sys.exit(1)

    api = HfApi(token=args.token)
    create_repo(args.repo, repo_type="dataset", exist_ok=True, token=args.token)

    card = generate_dataset_card(str(args.db))
    changelog = Path(__file__).parent / "CHANGELOG.md"
    if changelog.exists():
        card += "\n\n" + changelog.read_text()

    api.upload_file(path_or_fileobj=card.encode(), path_in_repo="README.md",
                    repo_id=args.repo, repo_type="dataset")
    size_gb = args.db.stat().st_size / (1024 ** 3)
    print(f"Uploading {args.db} ({size_gb:.1f} GB)...")
    api.upload_file(path_or_fileobj=str(args.db), path_in_repo="openpayments.duckdb",
                    repo_id=args.repo, repo_type="dataset")
    print(f"\nUploaded to https://huggingface.co/datasets/{args.repo}")
    print("\nUsers can now query remotely:\n"
          f"  ATTACH 'https://huggingface.co/datasets/{args.repo}/resolve/main/openpayments.duckdb'"
          " AS op (READ_ONLY);")


if __name__ == "__main__":
    main()
