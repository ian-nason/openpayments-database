# Changelog

## 2026-07-07 — Initial release

- Program years 2013-2025 from the June 2026 publication plus the frozen
  archive ZIPs (2013-2018 at their final republications).
- 172.5M rows: general_payments 148.8M, research_payments 11.0M (+10.7M-row
  investigators long table), ownership_payments 54k, covered_recipients
  1.7M, deleted_records 162k.
- Typed columns (DECIMAL money, DATE dates, VARCHAR identifiers); per-era
  column crosswalk checked into the repo (Physician_* -> Covered_Recipient_*
  renames for 2013-2015; pre-2016 product columns kept era-specific).
- Validated against CMS published magnitudes (PY2025: $3.9B general +
  $9.5B research + $0.2B ownership) and recognizable top manufacturers.
- Cross-database NPI join to cms-medicare measured and documented (61.6%
  of PY2023 recipients; 63-83% for physician specialties; dentists ~0%
  as expected — they don't bill Medicare Part B).
