# Open Payments Database (CMS Sunshine Act)

A clean, queryable DuckDB database of **every industry payment to physicians,
non-physician practitioners, and teaching hospitals** disclosed under the
Physician Payments Sunshine Act — program years 2013 through 2025.

**172.5M rows**: 148.8M general payments, 11.0M research payments (plus a
10.7M-row principal-investigator long table), 54k ownership interests, 1.7M
covered-recipient profiles, 162k deleted-record tombstones.

## Quick Start (Remote Query)

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

Or with the [datapond](https://pypi.org/project/datapond/) package:
`datapond.connect('openpayments')`.

## The headline join: Open Payments x Medicare utilization

Both this database and [cms-medicare](https://huggingface.co/datasets/Nason/cms-medicare-database)
key providers by NPI, so industry payments join directly to what the same
clinicians bill Medicare:

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
payments but rarely bill Part B. The unmatched remainder is real population
structure (Part B is fee-for-service only; Medicare Advantage-only,
non-billing, and retired providers don't appear), not a key mismatch.

## Tables

| Table | Rows | Description |
|-------|------|-------------|
| `general_payments` | 148.8M | Non-research payments (meals, consulting, royalties, travel...), PY2013-2025 |
| `research_payments` | 11.0M | Research payments, wide form with up to 5 PI column groups |
| `research_payment_investigators` | 10.7M | Long form: one row per (research record, PI slot 1-5) |
| `ownership_payments` | 54k | Physician ownership/investment interests |
| `covered_recipients` | 1.7M | Profile supplement: one row per covered recipient, with NPI |
| `deleted_records` | 162k | Record IDs removed between publications (PY2016+) |

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
   lists tombstoned record IDs per publication; PY2013-2015 never had such
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

## Provenance

Every detail row carries `program_year` and `source_file`. File inventory
(including the frozen archive publication stamps) is pinned in
`sources.yaml`; per-era column mappings in `crosswalk_openpayments.csv`.

## Build from Source

```bash
uv run --with duckdb --with pyyaml python build_database.py   # ~75GB raw cache, ~20 min load
uv run --with duckdb --with pandas --with huggingface_hub python publish_to_hf.py --token hf_YOUR_TOKEN
```

The build is idempotent: re-running skips already-loaded program years.
Annual refresh: update `sources.yaml` publication stamps after each June
publication (January for the refresh), delete the affected years' rows, and
re-run.

## License

Build code: MIT. Underlying data: public domain (U.S. government records).
