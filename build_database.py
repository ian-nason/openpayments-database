"""Build openpayments.duckdb from CMS Open Payments bulk files.

Pipeline: sources.yaml -> data/raw/ (cached ZIPs + CSVs) ->
crosswalk_openpayments.csv (per-era mappings from build_crosswalk.py) ->
typed canonical tables -> research_payment_investigators long table ->
_metadata/_columns/DICTIONARY.md -> validation.

Program years 2013-2025. Archived years (2013-2018) load from the frozen
ZIPs; 2016+ already carry the modern layout (CMS retrofitted it in the
final archive republications), so only PY2013-2015 flow through rename
rules.
"""
import argparse
import csv
import re
import shutil
import sys
import time
import zipfile
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import duckdb
import yaml

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DEFAULT_OUTPUT = "openpayments.duckdb"
RAW = Path("data/raw")
EXTRACTED = Path("data/extracted")

KIND_TABLE = {"GNRL": "general_payments", "RSRCH": "research_payments",
              "OWNRSHP": "ownership_payments"}

DATE_COLS_RE = re.compile(r"(^date_of_payment$|_date$)")
MONEY_COLS = {
    "total_amount_of_payment_usdollars",
    "total_amount_invested_usdollars",
    "value_of_interest_usdollars",
}
INT_COLS = {"number_of_payments_included_in_total_amount", "program_year"}

TABLE_DESCRIPTIONS = {
    "general_payments": "General (non-research) payments and transfers of value "
                        "to covered recipients, PY2013-2025",
    "research_payments": "Research payments (wide form, up to 5 principal "
                         "investigators per record), PY2013-2025",
    "research_payment_investigators": "Long form of research-payment principal "
                                      "investigators: one row per (record, PI slot)",
    "ownership_payments": "Physician ownership and investment interests, PY2013-2025",
    "covered_recipients": "Covered Recipient Profile Supplement: one row per "
                          "physician/NPP profile with NPI",
    "deleted_records": "Record IDs deleted between publications (PY2016+; "
                       "earlier years never had these files)",
}


def canonical_type(col: str) -> str:
    if col in MONEY_COLS:
        return "DECIMAL(14,2)"
    if col in INT_COLS:
        return "INTEGER"
    if DATE_COLS_RE.search(col):
        return "DATE"
    return "VARCHAR"


def cast_expr(src: str, col: str) -> str:
    q = f'"{src}"'
    t = canonical_type(col)
    if t == "DATE":
        return (f"COALESCE(TRY_STRPTIME({q}, '%m/%d/%Y')::DATE, "
                f"TRY_CAST({q} AS DATE))")
    if t.startswith("DECIMAL"):
        return f"TRY_CAST(NULLIF(TRIM({q}), '') AS {t})"
    if t == "INTEGER":
        return f"TRY_CAST({q} AS INTEGER)"
    return f"NULLIF(TRIM({q}), '')"


def extract_archives(sources: dict) -> None:
    EXTRACTED.mkdir(parents=True, exist_ok=True)
    for year, url in sources["archived_zips"].items():
        zpath = RAW / url.rsplit("/", 1)[-1]
        with zipfile.ZipFile(zpath) as zf:
            for name in zf.namelist():
                if not name.lower().endswith(".csv"):
                    continue
                dest = EXTRACTED / Path(name).name
                if dest.exists() and dest.stat().st_size > 0:
                    continue
                # Stream: whole-member reads of multi-GB files can take the
                # machine down before the OOM killer reacts.
                with zf.open(name) as src, open(dest, "wb") as out:
                    shutil.copyfileobj(src, out, 1024 * 1024 * 16)
                print(f"  extracted {dest.name}", flush=True)


def inventory(sources: dict) -> dict[str, list[tuple[int, Path]]]:
    """kind -> [(program_year, csv_path)] across archive + current files."""
    files = defaultdict(list)
    for d in (EXTRACTED, RAW):
        for p in d.glob("OP_DTL_*.csv"):
            m = re.match(r"OP_DTL_(GNRL|RSRCH|OWNRSHP)_PGYR(20\d\d)_", p.name)
            if m:
                files[m.group(1)].append((int(m.group(2)), p))
    for kind in files:
        files[kind].sort()
    return files


def load_crosswalk() -> dict[tuple[str, str], dict[str, str]]:
    cw = defaultdict(dict)
    for r in csv.DictReader(open("crosswalk_openpayments.csv")):
        if r["kind"] != "drop":
            cw[(r["table"], r["era"])][r["source_column"]] = r["canonical_column"]
    return cw


def era_of_year(y: int) -> str:
    return "2013" if y <= 2014 else ("2015" if y == 2015 else "2016")


def load_detail_tables(con, files, cw):
    counts = {}
    for kind, table in KIND_TABLE.items():
        canon = sorted({c for (t, _), m in cw.items() if t == table
                        for c in m.values()})
        cols_sql = ", ".join(f'"{c}" {canonical_type(c)}' for c in canon)
        con.execute(f"""
            CREATE TABLE IF NOT EXISTS {table} (
                {cols_sql}, source_file VARCHAR
            )
        """)
        # Idempotent resume: skip program years already loaded.
        have_years = {
            r[0] for r in con.execute(
                f"SELECT DISTINCT program_year FROM {table}"
            ).fetchall()
        }
        total = 0
        for year, path in files[kind]:
            if year in have_years:
                print(f"  {table} PY{year}: already loaded, skipping", flush=True)
                continue
            mapping = cw[(table, era_of_year(year))]
            header = con.execute(f"""
                SELECT * FROM read_csv('{path}', header=true, all_varchar=true,
                                       sample_size=1) LIMIT 0
            """).description
            have = {d[0] for d in header}
            by_canon = {mapping[s]: s for s in have if s in mapping}
            exprs = []
            for c in canon:
                if c == "program_year":
                    exprs.append(f"{year} AS program_year")
                elif c in by_canon:
                    exprs.append(f'{cast_expr(by_canon[c], c)} AS "{c}"')
                else:
                    exprs.append(f'NULL AS "{c}"')
            def insert_sql(extra: str) -> str:
                return f"""
                    INSERT INTO {table}
                    SELECT {", ".join(exprs)}, '{path.name}' AS source_file
                    FROM read_csv('{path}', header=true, all_varchar=true,
                                  ignore_errors=true, null_padding=true,
                                  max_line_size=10485760{extra})
                """
            try:
                con.execute(insert_sql(""))
            except duckdb.Error:
                # The parallel scanner rejects null_padding when the file has
                # quoted newlines; retry single-threaded (same fix as FEC).
                con.execute(
                    f"DELETE FROM {table} WHERE program_year = {year}"
                )
                con.execute(insert_sql(", parallel=false"))
            n = con.execute(
                f"SELECT COUNT(*) FROM {table} WHERE program_year = {year}"
            ).fetchone()[0]
            total += n
            print(f"  {table} PY{year}: {n:,} rows", flush=True)
        counts[table] = total
    return counts


def build_investigators(con) -> int:
    pi_cols = [
        "profile_id", "npi", "first_name", "middle_name", "last_name",
        "name_suffix", "city", "state", "country",
        "primary_type_1", "specialty_1",
    ]
    selects = []
    for i in range(1, 6):
        cols = ", ".join(
            f'"principal_investigator_{i}_{c}" AS pi_{c}' for c in pi_cols
        )
        selects.append(f"""
            SELECT record_id, program_year, {i} AS pi_position, {cols}
            FROM research_payments
            WHERE COALESCE("principal_investigator_{i}_npi",
                           "principal_investigator_{i}_profile_id",
                           "principal_investigator_{i}_last_name") IS NOT NULL
        """)
    con.execute(f"""
        CREATE OR REPLACE TABLE research_payment_investigators AS
        {" UNION ALL ".join(selects)}
    """)
    return con.execute(
        "SELECT COUNT(*) FROM research_payment_investigators"
    ).fetchone()[0]


def load_simple_tables(con, sources):
    prfl = RAW / sources["profile_supplement"].rsplit("/", 1)[-1]
    con.execute(f"""
        CREATE OR REPLACE TABLE covered_recipients AS
        SELECT * FROM read_csv('{prfl}', header=true, all_varchar=true,
                               ignore_errors=true, null_padding=true)
    """)
    # snake_case + keep NPI etc. VARCHAR
    for (old,) in con.execute(
        "SELECT column_name FROM information_schema.columns "
        "WHERE table_name = 'covered_recipients'"
    ).fetchall():
        new = re.sub(r"[^a-z0-9]+", "_", old.lower()).strip("_")
        if new != old:
            con.execute(
                f'ALTER TABLE covered_recipients RENAME COLUMN "{old}" TO "{new}"'
            )

    paths = []
    for d in (EXTRACTED, RAW):
        paths += list(d.glob("OP_REMOVED_DELETED_*.csv"))
    seen, uniq = set(), []
    for p in paths:
        if p.name not in seen:
            seen.add(p.name)
            uniq.append(p)
    con.execute("""
        CREATE OR REPLACE TABLE deleted_records (
            change_type VARCHAR, program_year INTEGER,
            payment_type VARCHAR, record_id VARCHAR, source_file VARCHAR
        )
    """)
    for p in uniq:
        con.execute(f"""
            INSERT INTO deleted_records
            SELECT "Change_Type", TRY_CAST("Program_Year" AS INTEGER),
                   "Payment_Type", "Record_ID", '{p.name}'
            FROM read_csv('{p}', header=true, all_varchar=true)
        """)
    n = con.execute("SELECT COUNT(*) FROM deleted_records").fetchone()[0]
    print(f"  deleted_records: {n:,} rows from {len(uniq)} files")


def build_metadata(con):
    con.execute("""
        CREATE OR REPLACE TABLE _metadata (
            table_name VARCHAR, description VARCHAR, row_count BIGINT,
            column_count INTEGER, data_sources VARCHAR, date_range VARCHAR,
            built_at TIMESTAMP
        )
    """)
    now = datetime.now().isoformat()
    for tbl, desc in TABLE_DESCRIPTIONS.items():
        rc = con.execute(f"SELECT COUNT(*) FROM {tbl}").fetchone()[0]
        cc = len(con.execute(f"SELECT * FROM {tbl} LIMIT 0").description)
        try:
            yr = con.execute(
                f"SELECT MIN(program_year), MAX(program_year) FROM {tbl}"
            ).fetchone()
            dr = f"PY{yr[0]} to PY{yr[1]}"
        except Exception:
            dr = "all years"
        con.execute(
            "INSERT INTO _metadata VALUES (?, ?, ?, ?, ?, ?, ?)",
            [tbl, desc, rc, cc,
             "CMS Open Payments June 2026 publication + frozen archives "
             "(openpaymentsdata.cms.gov)", dr, now],
        )


def build_columns_table(con):
    con.execute("DROP TABLE IF EXISTS _columns")
    con.execute("""
        CREATE TABLE _columns (
            table_name VARCHAR, column_name VARCHAR, data_type VARCHAR,
            null_pct DOUBLE, example_value VARCHAR
        )
    """)
    for tbl in TABLE_DESCRIPTIONS:
        cols = con.execute(
            "SELECT column_name, data_type FROM information_schema.columns "
            "WHERE table_name = ? ORDER BY ordinal_position", [tbl],
        ).fetchall()
        # one scan per table: null counts and examples for every column
        aggs = []
        for c, _ in cols:
            aggs.append(f'COUNT(*) FILTER (WHERE "{c}" IS NULL)')
            aggs.append(f'MIN(CAST("{c}" AS VARCHAR)) FILTER (WHERE "{c}" IS NOT NULL)')
        stats = con.execute(
            f"SELECT COUNT(*), {', '.join(aggs)} FROM {tbl}"
        ).fetchone()
        total = stats[0] or 1
        for i, (c, dt) in enumerate(cols):
            nulls, example = stats[1 + 2 * i], stats[2 + 2 * i]
            con.execute(
                "INSERT INTO _columns VALUES (?, ?, ?, ?, ?)",
                [tbl, c, dt, round(100.0 * nulls / total, 1),
                 (example or "")[:80]],
            )


def export_dictionary(con, out: Path):
    lines = [
        "# openpayments Data Dictionary", "",
        "Built from the CMS Open Payments June 2026 publication and the "
        "frozen archive ZIPs (PY2013-2018). Authoritative column semantics: "
        "the CMS Open Payments Methodology & Data Dictionary, "
        "https://www.cms.gov/OpenPayments/Downloads/OpenPaymentsDataDictionary.pdf", "",
        "Per-era source-column mappings (including which columns exist only "
        "pre-2016 or only 2021+) are in crosswalk_openpayments.csv in the "
        "build repo.", "",
    ]
    for tbl, desc in TABLE_DESCRIPTIONS.items():
        rc = con.execute(
            "SELECT row_count FROM _metadata WHERE table_name = ?", [tbl]
        ).fetchone()[0]
        lines += [f"## {tbl}", "", f"{desc}. {rc:,} rows.", "",
                  "| Column | Type | Null % | Example |",
                  "|--------|------|--------|---------|"]
        for c, dt, np, ex in con.execute(
            "SELECT column_name, data_type, null_pct, example_value "
            "FROM _columns WHERE table_name = ?", [tbl],
        ).fetchall():
            lines.append(f"| `{c}` | {dt} | {np}% | {(ex or '').replace('|', '/')} |")
        lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"  Exported {out}")


def run_validation(con):
    print("\n" + "=" * 60 + "\nVALIDATION\n" + "=" * 60)
    print("\n  Total general-payment dollars by program year:")
    for y, n, amt in con.execute("""
        SELECT program_year, COUNT(*), ROUND(SUM(total_amount_of_payment_usdollars) / 1e9, 2)
        FROM general_payments GROUP BY 1 ORDER BY 1
    """).fetchall():
        print(f"    PY{y}: {n:,} rows, ${amt}B")
    print("\n  All-category dollars, latest year:")
    for tbl, col in [("general_payments", "total_amount_of_payment_usdollars"),
                     ("research_payments", "total_amount_of_payment_usdollars"),
                     ("ownership_payments", "total_amount_invested_usdollars")]:
        r = con.execute(f"""
            SELECT ROUND(SUM({col}) / 1e9, 2) FROM {tbl}
            WHERE program_year = (SELECT MAX(program_year) FROM {tbl})
        """).fetchone()[0]
        print(f"    {tbl}: ${r}B")
    print("\n  Top manufacturers by general-payment dollars, PY2024:")
    for m, amt in con.execute("""
        SELECT applicable_manufacturer_or_applicable_gpo_making_payment_name,
               ROUND(SUM(total_amount_of_payment_usdollars) / 1e6, 1)
        FROM general_payments WHERE program_year = 2024
        GROUP BY 1 ORDER BY 2 DESC LIMIT 8
    """).fetchall():
        print(f"    {m}: ${amt}M")
    print("\n  Nature of payment distribution, PY2024:")
    for nat, n in con.execute("""
        SELECT nature_of_payment_or_transfer_of_value, COUNT(*)
        FROM general_payments WHERE program_year = 2024
        GROUP BY 1 ORDER BY 2 DESC LIMIT 6
    """).fetchall():
        print(f"    {nat}: {n:,}")
    print("\n  NPI coverage in covered_recipients:")
    r = con.execute("""
        SELECT COUNT(*), COUNT(covered_recipient_npi) FROM covered_recipients
    """).fetchone()
    print(f"    {r[1]:,} of {r[0]:,} profiles have an NPI")
    total = con.execute("SELECT SUM(row_count) FROM _metadata").fetchone()[0]
    print(f"\n  Total rows: {total:,}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--output", type=Path, default=Path(DEFAULT_OUTPUT))
    args = p.parse_args()
    t0 = time.time()

    sources = yaml.safe_load(open("sources.yaml"))
    print("[1/6] Extracting archived ZIPs")
    extract_archives(sources)
    files = inventory(sources)
    for k, v in files.items():
        print(f"  {k}: {len(v)} files, years {v[0][0]}-{v[-1][0]}")

    # No unlink: the build is idempotent and resumes into an existing file
    # (already-loaded program years are skipped).
    con = duckdb.connect(str(args.output))
    con.execute("SET preserve_insertion_order = false")
    con.execute(f"SET temp_directory = '{args.output.resolve()}.tmp'")
    con.execute("SET memory_limit = '8GB'")

    print("\n[2/6] Loading detail tables")
    cw = load_crosswalk()
    load_detail_tables(con, files, cw)

    print("\n[3/6] Building research_payment_investigators")
    n = build_investigators(con)
    print(f"  {n:,} investigator rows")

    print("\n[4/6] Loading covered_recipients and deleted_records")
    load_simple_tables(con, sources)

    print("\n[5/6] Metadata, columns, dictionary")
    build_metadata(con)
    build_columns_table(con)
    export_dictionary(con, Path("DICTIONARY.md"))

    print("\n[6/6] Validation")
    con.execute("CHECKPOINT")
    run_validation(con)
    con.close()
    print(f"\nBUILD DONE in {(time.time() - t0) / 60:.1f} min")


if __name__ == "__main__":
    main()
