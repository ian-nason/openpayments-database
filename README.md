# Open Payments Database (CMS Sunshine Act)

Industry payments and financial relationships disclosed under the Physician Payments Sunshine Act and reported to Centers for Medicare & Medicaid Services (CMS) Open Payments for program years 2013–2025. Explore general and research payments, ownership records, recipients and reporting companies. Start with the payment table that matches the question: investigator associations, recipient profiles and deletion records have different units and must not be added as extra payments. Royalties can dominate payment rankings, and a research investigator association does not assign the full payment amount to that individual. Non-physician practitioner coverage begins in 2021.

<a id="quick-start"></a>

## Start querying

Preview reported 2024 general-payment records above $1 million. General payments can include royalties.

The result shows `record_id` (payment record identifier), `program_year`, and `total_amount_of_payment_usdollars` (U.S. dollars).

Choose R or Python. Install datapond once: use `install.packages("datapond")` in R, or run `python -m pip install datapond` in a terminal.

### R

```r
library(datapond)
con <- dp_connect("openpayments")
tryCatch({
  DBI::dbExecute(con, "SET threads=1")
  DBI::dbExecute(con, "SET memory_limit='128MiB'")
  DBI::dbExecute(con, "SET max_temp_directory_size='0B'")
  print(DBI::dbGetQuery(con, "SELECT record_id,program_year,total_amount_of_payment_usdollars FROM general_payments WHERE program_year=2024 AND total_amount_of_payment_usdollars>1000000 LIMIT 5"))
}, finally = dp_disconnect(con))
```

### Python

```python
import datapond
con = datapond.connect('openpayments')
try:
    con.execute("SET threads=1")
    con.execute("SET memory_limit='128MiB'")
    con.execute("SET max_temp_directory_size='0B'")
    print(con.execute("""SELECT record_id,program_year,total_amount_of_payment_usdollars FROM general_payments WHERE program_year=2024 AND total_amount_of_payment_usdollars>1000000 LIMIT 5""").fetchall())
finally:
    con.close()
```

Queries run on your computer and read the byte ranges they need. A small result can still require a large scan. These examples limit DuckDB to one thread and a 128 MiB buffer pool with disk spill disabled; that is not a limit on the entire R or Python process. Larger analyses may need more memory or a local download with enough disk space.

<a id="additional-dataset-notes"></a>

<a id="tables"></a>

## Tables and record units

**172.5M rows** across payments, investigator associations, ownership interests, recipient profiles and records identifying entries removed from later publications. Recipients include physicians, non-physician practitioners (NPPs) and teaching hospitals. PY means program year, NPI means National Provider Identifier, and PI means principal investigator.

| Table | Rows | Description |
|-------|------|-------------|
| `general_payments` | 148.8M | Non-research payments (meals, consulting, royalties, travel...), PY2013-2025 |
| `research_payments` | 11.0M | Research payments, one payment row with up to five PI column groups |
| `research_payment_investigators` | 10.7M | One row for each payment–investigator association (research record and PI position 1–5) |
| `ownership_payments` | 54k | Physician ownership/investment interests |
| `covered_recipients` | 1.7M | Profile supplement: one row per covered recipient, with NPI |
| `deleted_records` | 162k | Record IDs removed between publications (PY2016+) |

Research-investigator association rows do not assign the full payment amount to each investigator. Most research dollars go to institutions; use the association table for linkage, not individual dollar attribution.

<a id="coverage-fields-and-sources"></a>

See the [data dictionary](https://github.com/ian-nason/openpayments-database/blob/main/DICTIONARY.md) for column definitions.

## Researcher caveats — read before publishing numbers

1. **PY2013-2014 general payments have no NPI column** (source design; NPI
   arrived in PY2015). Bridge via `covered_recipient_profile_id` ->
   `covered_recipients.covered_recipient_profile_id`, which carries NPI.
2. **Non-physician practitioners are covered recipients only from PY2021.**
   The modern column layout (retrofitted by CMS onto 2016+ archives) carries
   the NPP columns everywhere, but NPP rows exist only from 2021 — recipient
   counts jump at that break for real coverage reasons.
3. **Product columns break at PY2016.** 2013-2015 used separate drug[1-5] /
   device[1-5] name+NDC slots; 2016+ uses unified product groups with type
   indicators. Both forms are kept as-is (no synthesized values); product
   analyses spanning the break must handle both (see the crosswalk).
4. **Research dollars concentrate in entities, not the named PIs.** Most
   research payments go to institutions; the PI columns identify associated
   investigators, not recipients of the money. Use
   `research_payment_investigators` for trial-linkage work, not dollar
   attribution.
5. **Royalties skew manufacturer rankings.** A single royalty relationship
   (e.g. vaccine or device royalties) can put one maker atop the dollar
   rankings while meals dominate row counts (14.2M of PY2024's 15.5M general
   rows are Food and Beverage).
6. **Disputed and deleted records.** `dispute_status_for_publication` marks
   recipient-disputed rows (kept, as CMS publishes them). `deleted_records`
   identifies record IDs removed from later publications; PY2013-2015 never had such
   files, and PY2025 has none yet (first publication).
7. **Archived years are frozen** at their final January republication
   (2013: Jan 2021 ... 2018: Jan 2026); current years (2019-2025) refresh
   each January/June. A record's `change_type` column marks its status in
   the publication it came from.
8. **NPI is VARCHAR everywhere** — never cast to numbers (leading-zero
   discipline; also applies to NDC codes and ZIPs).

Authoritative column semantics: the [CMS Open Payments Methodology & Data
Dictionary](https://www.cms.gov/OpenPayments/Downloads/OpenPaymentsDataDictionary.pdf),
cited throughout DICTIONARY.md.

<a id="advanced-access-quick-start-remote-query"></a>

## More example queries

```sql
INSTALL httpfs;
LOAD httpfs;
ATTACH 'https://huggingface.co/datasets/Nason/openpayments-database/resolve/main/openpayments.duckdb' AS op (READ_ONLY);

-- Top manufacturers by general-payment dollars, PY2024
SELECT applicable_manufacturer_or_applicable_gpo_making_payment_name AS maker,
       ROUND(SUM(total_amount_of_payment_usdollars) / 1e6, 1) AS millions
FROM op.general_payments
WHERE program_year = 2024
GROUP BY 1 ORDER BY 2 DESC LIMIT 10;
```

<a id="the-headline-join-open-payments-x-medicare-utilization"></a>

## Compare industry payments with Medicare payments

Both this database and [cms-medicare](https://huggingface.co/datasets/Nason/cms-medicare-database)
key providers by NPI, so industry payments join directly to what the same
clinicians bill in the published Medicare Part B fee-for-service summaries.
This join does not cover Medicare Advantage, Part A or Part D:

```sql
ATTACH 'https://huggingface.co/datasets/Nason/openpayments-database/resolve/main/openpayments.duckdb' AS op (READ_ONLY);
ATTACH 'https://huggingface.co/datasets/Nason/cms-medicare-database/resolve/main/cms_medicare.duckdb' AS cms (READ_ONLY);

-- Industry money vs Medicare payments per internist, 2023
WITH pay AS (
    SELECT covered_recipient_npi AS npi,
           SUM(total_amount_of_payment_usdollars) AS industry_dollars
    FROM op.general_payments
    WHERE program_year = 2023 AND covered_recipient_npi IS NOT NULL
    GROUP BY 1
)
SELECT s.Rndrng_NPI, s.Rndrng_Prvdr_Last_Org_Name,
       p.industry_dollars, s.Tot_Mdcr_Pymt_Amt AS medicare_payments
FROM cms.physician_summary s
JOIN pay p ON s.Rndrng_NPI = p.npi
WHERE s.year = 2023 AND s.Rndrng_Prvdr_Type = 'Internal Medicine'
ORDER BY p.industry_dollars DESC LIMIT 20;
```

**Measured join rates (2023):** 61.6% of PY2023 general-payment recipients
with an NPI appear among 2023 Medicare Part B billers; physician specialties
match at 63-83% (nurse anesthetists 83%, internal medicine 67%, family
medicine 64%) while **dentists match at ~0.1%** — they receive industry
payments but rarely bill Part B. Population differences can explain unmatched
records: the Medicare data cover fee-for-service Part B, and Medicare
Advantage-only, non-billing or retired providers may be absent. These rates do
not rule out identifier problems among individual unmatched records.

## Other ways to connect

Or with the [datapond](https://pypi.org/project/datapond/) package:
`datapond.connect('openpayments')`.

## Sources and maintenance

### Source and license reference

See the [data dictionary](https://github.com/ian-nason/openpayments-database/blob/main/DICTIONARY.md) for column definitions and the [CMS Open Payments (openpaymentsdata.cms.gov)](https://openpaymentsdata.cms.gov/datasets) for the source. License: Public domain.

### Provenance

Every detail row carries `program_year` and `source_file`. File inventory
(including the frozen archive publication stamps) is pinned in
`sources.yaml`; per-era column mappings in `crosswalk_openpayments.csv`.

### Build from Source

```bash
uv run --with duckdb --with pyyaml python build_database.py   # ~75GB raw cache, ~20 min load
uv run --with duckdb --with pandas --with huggingface_hub python publish_to_hf.py --token hf_YOUR_TOKEN
```

The build is idempotent: re-running skips already-loaded program years.
Annual refresh: update `sources.yaml` publication stamps after each June
publication (January for the refresh), delete the affected years' rows, and
re-run.

### License

Build code: MIT. Underlying data: public domain (U.S. government records).
