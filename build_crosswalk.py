"""Generate crosswalk_openpayments.csv from headers_op.json.

Three source eras per detail table (verified against the June 2026
publication and the frozen archive ZIPs):
  era 2013: PY2013-2014  (original layout; GNRL has NO NPI column)
  era 2015: PY2015       (transitional; NPI added)
  era 2016: PY2016-2025  (modern layout, byte-identical headers all 10 years
                          — CMS retrofitted the PY2021 NPP columns onto
                          2016-2018 in their final archive republications)

Canonical names are the snake_cased modern headers. Old-era recipient
identity columns are true renames (Physician_* -> Covered_Recipient_*).
Old-era product columns (separate drug[1-5]/device[1-5] slots) are NOT
mappable 1:1 onto the modern unified product groups and are kept as
era-specific passthrough columns rather than synthesizing values.
"""
import csv
import json
import re

H = json.load(open("headers_op.json"))

TABLES = {"GNRL": "general_payments", "RSRCH": "research_payments",
          "OWNRSHP": "ownership_payments"}


def era_of(fkey: str) -> str:
    m = re.search(r"PGYR(20\d\d)", fkey.split("::")[-1])
    y = int(m.group(1))
    return "2013" if y <= 2014 else ("2015" if y == 2015 else "2016")


def snake(c: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", c.lower()).strip("_")


SPECIAL = {
    "Physician_Primary_Type": "Covered_Recipient_Primary_Type_1",
    "Physician_Specialty": "Covered_Recipient_Specialty_1",
    "Product_Indicator": "Related_Product_Indicator",
    # RSRCH old era: single-slot context of research
    "Name_of_Associated_Covered_Drug_or_Biological": None,  # placeholder, unused
}


def map_column(src: str, current: set[str]) -> tuple[str | None, str]:
    """Return (canonical, note) for an old-era source column."""
    if src in current:
        return snake(src), ""
    if src in SPECIAL and SPECIAL[src]:
        return snake(SPECIAL[src]), "renamed"
    swapped = src.replace("Physician_", "Covered_Recipient_")
    if swapped in current:
        return snake(swapped), "Physician_ prefix rename"
    # Old single-valued PI type/specialty map to the modern _1 slot
    # (Principal_Investigator_N_Primary_Type -> ..._Primary_Type_1)
    m = re.match(r"^(Principal_Investigator_\d_(?:Primary_Type|Specialty))$", src)
    if m and f"{src}_1" in current:
        return snake(f"{src}_1"), "single-valued -> slot 1 rename"
    return None, ""


rows = []
unmatched_report = {}
for kind, table in TABLES.items():
    files = {k: v for k, v in H.items() if f"_{kind}_" in k}
    current = None
    for k, v in files.items():
        if era_of(k) == "2016":
            current = v
            break
    cur_set = set(current)
    for era in ("2013", "2015", "2016"):
        era_files = [k for k in files if era_of(k) == era]
        if not era_files:
            continue
        cols = files[era_files[0]]
        for c in cols:
            if era == "2016":
                rows.append((table, era, c, snake(c), "core", ""))
                continue
            canonical, note = map_column(c, cur_set)
            if canonical:
                rows.append((table, era, c, canonical, "core", note))
            else:
                rows.append((table, era, c, snake(c), "passthrough",
                             "era-specific column (pre-2016 layout)"))
                unmatched_report.setdefault(f"{table}/{era}", []).append(c)

# deleted records + profile supplement: single uniform layouts
for k, v in H.items():
    if "REMOVED_DELETED" in k and "::" not in k and "2024" in k:
        for c in v:
            rows.append(("deleted_records", "all", c, snake(c), "core", ""))
    if "CVRD_RCPNT_PRFL" in k:
        for c in v:
            rows.append(("covered_recipients", "all", c, snake(c), "core", ""))

with open("crosswalk_openpayments.csv", "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["table", "era", "source_column", "canonical_column", "kind", "note"])
    w.writerows(rows)

for k, v in unmatched_report.items():
    print(f"{k}: {len(v)} era-specific passthrough columns")
    print("   ", v[:12], "..." if len(v) > 12 else "")
for table in set(TABLES.values()):
    canon = {r[3] for r in rows if r[0] == table}
    print(f"{table}: {len(canon)} canonical columns")
