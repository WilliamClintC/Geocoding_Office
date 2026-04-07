# Geocoding Office

## Overview

This project geocodes commercial real estate lease records from CoStar using the U.S. Census Bureau Batch Geocoder API. The pipeline extracts and standardizes property addresses, submits them to the Census API to obtain latitude/longitude, census tract, and FIPS codes, then validates results via ZIP code matching.

The pipeline was developed on a San Francisco pilot (9,352 properties, ~96% match rate) before scaling to the full U.S. dataset (1,051,219 properties, ~92.3% strict match rate).

## Structure

This project follows the directory conventions from Franklin Qian's RA Manual
(itself based on Gentzkow & Shapiro's *Code and Data for the Social Sciences*).

The top-level folders are `source/`, `data/`, `output/`, and `temp/`.
Each mirrors the three pipeline stages: `raw/`, `derived/`, and `analysis/`.

```
Geocoding_Office/
├── source/                          All code scripts (.do  .R  .py  .ipynb)
│   ├── 0_raw/                       Extract geographic identifiers from raw data
│   │   ├── 1_SF_Geo_Identifier_Extraction.ipynb
│   │   └── 1_Whole_Geo_Identifier_Extraction.ipynb
│   │
│   ├── 1_derived/                   Standardize addresses and geocode
│   │   ├── 1_SF_Geo_Standardizer.ipynb
│   │   ├── 1_Whole_Geo_Standardizer.ipynb
│   │   ├── 2_SF_Census_Geocoder.ipynb
│   │   ├── 2_Whole_Census_Geocoder.ipynb
│   │   ├── 3_SF_Zipcode_Matcher.ipynb
│   │   ├── 3_Whole_Zipcode_Matcher.ipynb
│   │   └── 4_SF_Tie_Breaker_Zipcode.ipynb
│   │
│   ├── 2_analysis/                  Match-rate analysis, tables, figures
│   │   ├── 1_SF_Census_Geocoder_Analysis.ipynb
│   │   ├── 1_Whole_Census_Geocoder_Analysis.ipynb
│   │   ├── 2_SF_Census_Geocoder_Tie_Analysis.ipynb
│   │   └── 2_Whole_Matched_Export.ipynb
│   │
│   └── lib/                         Shared helpers
│
├── data/                            All data files (never edited by hand)
│   ├── 0_raw/
│   │   ├── CoStar_Whole.csv         Raw CoStar lease records (~1.05M properties, 235 cols)
│   │   └── Census Shapefiles/       56 Census tract boundary shapefiles (year 2000)
│   │
│   └── 1_derived/
│       ├── 1_*_properties_for_geocoding_*.csv          Extracted identifiers
│       ├── 2_*_properties_for_geocoding_standardized_*.csv  Standardized addresses
│       ├── 3_*_properties_census_geocoded_*.csv         Census API results
│       ├── 4_*_zipcode_matcher_*.csv                    ZIP validation results
│       └── 5_whole_matched_final.csv                    Final consolidated dataset
│
├── output/                          All non-data outputs
│   └── 2_analysis/
│       ├── tables/                  Match-rate summaries (.csv, .md)
│       └── figures/                 State-level maps and ZIP validation charts
│
├── temp/                            Temporary intermediate files
│
├── docs/
│   ├── weekly_reports/              Quarto progress reports (PDF + .qmd source)
│   └── codebooks/                   CoStar data dictionary, task brief, variable list
│
├── run_all.py                       Master script – runs entire pipeline
├── requirements.txt                 Python package list
└── install.R                        R package list (run once to install)
```

### File naming convention

Scripts and derived data files use a **numeric prefix** indicating pipeline step, followed by a descriptive name in Title_Case. SF refers to the San Francisco pilot; Whole refers to the full U.S. dataset.

| Step | What                              | Example                                          |
|------|-----------------------------------|--------------------------------------------------|
| 1    | Geographic identifier extraction  | `1_Whole_Geo_Identifier_Extraction.ipynb`        |
| 2    | Address standardization           | `2_whole_properties_for_geocoding_standardized_001.csv` |
| 3    | Census geocoding                  | `3_whole_properties_census_geocoded_001.csv`     |
| 4    | ZIP code validation               | `4_whole_zipcode_matcher_001.csv`                |
| 5    | Final merged output               | `5_whole_matched_final.csv`                      |

Large datasets are split into numbered batches (`_001`, `_002`, …) to respect Census API limits.

## Pipeline

```
CoStar_Whole.csv
      │
      ▼  source/0_raw/
  1. Extract geographic identifiers (address, city, state, ZIP)
      │
      ▼  source/1_derived/
  2. Standardize addresses
     (uppercase · remove punctuation · abbreviate street types · collapse address ranges)
      │
      ▼
  3. Census Bureau Batch Geocoder
     → lat/lon, census tract, FIPS code
     → 92.32% strict match rate (U.S.); 96% (SF pilot)
      │
      ▼
  4. ZIP code validation
     (compare input ZIP vs. Census-returned ZIP to flag mismatches)
      │
      ▼  source/2_analysis/
  5. Match-rate analysis + export final dataset
     → output/2_analysis/tables/   (state, county, match-type summaries)
     → output/2_analysis/figures/  (state heatmap, ZIP validation charts)
     → data/1_derived/5_whole_matched_final.csv
```

## Replication

**Run the full pipeline** from the project root:
```bash
python run_all.py
```

**Run a single stage:**
```bash
python run_all.py --stage 0    # 0_raw  – extraction
python run_all.py --stage 1    # 1_derived – standardization + geocoding
python run_all.py --stage 2    # 2_analysis
python run_all.py --dry-run    # print commands without executing
```

`run_all.py` dispatches each script by file extension:

| Extension | Executor |
|-----------|----------|
| `.ipynb`  | `jupyter nbconvert --execute --inplace <file>` |

Scripts prefixed with `_` are treated as templates and skipped automatically.

## Data Sources

| Dataset | Source | Notes |
|---------|--------|-------|
| CoStar lease records | CoStar Group | ~1.05M U.S. commercial properties; 235 columns. See `docs/codebooks/csgp_cs_variable.pdf` |
| Census Batch Geocoder | U.S. Census Bureau | Free batch API; returns lat/lon, tract, FIPS |

## Weekly Reports (Quarto)

Weekly reports are written in Quarto (`.qmd`) and compiled to PDF.

| Item      | Location                                                    |
|-----------|-------------------------------------------------------------|
| Template  | `docs/weekly_reports/report_template.qmd`                   |
| Reports   | `docs/weekly_reports/YYYY-MM-DD_Task-<N>-<description>.qmd` |
| PDFs      | Committed alongside the `.qmd` source                       |

Date-first naming (`YYYY-MM-DD_...`) ensures VS Code sorts reports newest-to-oldest automatically.

**Compile a report:**
```bash
quarto render docs/weekly_reports/YYYY-MM-DD_Task-N-description.qmd
```

Path references inside `.qmd` files use relative paths from `docs/weekly_reports/`:
- `../../data/1_derived/` for processed data
- `../../output/2_analysis/figures/` for figures
- `../../output/2_analysis/tables/` for tables

---

## Python Environment

| Item            | Value                              |
|-----------------|------------------------------------|
| Python version  | 3.13.5                             |
| Package list    | `requirements.txt`                 |
| Virtual env     | `.venv/` (gitignored)              |

**Setup:**
```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

When you add or update a package, pin it in `requirements.txt` (`pip freeze` the specific package, not the whole environment). Record any version upgrades in your commit message so collaborators know to re-install.

---

## Notes
- Raw data in `data/0_raw/` is **read-only**; never edit those files.
- All files in `data/1_derived/` and `output/` are produced by code and can be deleted and regenerated by rerunning `run_all.py`.
- `temp/` files are committed; clean them up manually when no longer needed.
- **Always use relative paths.** Never hard-code an absolute path in any script (`.py`, `.ipynb`).
- **Working directory** for all scripts is the **project root**. `run_all.py` enforces this automatically via `os.chdir(ROOT)`.
- `run_all.py` writes a date-stamped master log to `output/run_all_<YYYYMMDD_HHMMSS>.log`.
