# Whole US Census Tract Match Report (Batches 001-007)

- Generated: 2026-05-05 01:20:41
- Input batch files: 7
- Total rows: 1,051,219
- Rows resolved to a single census tract: 1,047,897 (99.68%)
- Rows flagged (ambiguous or missing): 3,322 (0.32%)

## Tract Resolution Method Counts
| tract_resolution_method | rows | pct |
| --- | --- | --- |
| One-to-One Primary | 1043837 | 99.3 |
| Tie Resolved via ZIP-Matching Ties | 3746 | 0.36 |
| Tract Ambiguous | 2637 | 0.25 |
| Tract Missing | 685 | 0.07 |
| Tie Resolved via All Ties Unanimous | 314 | 0.03 |

## Tie Rows: Tract Resolution by ZIP Match Detail
Total One-to-Many (tie) rows: 6,697.

- Tie rows whose ZIP-matching ties all share the same tract: **3,746**
- Tie rows where every tie (regardless of ZIP) shares the same tract: **4,045**
- Tie rows resolved to a single tract (final): **4,060**
- Tie rows ambiguous (multiple distinct tracts): **2,637**
- Tie rows missing tract data: **0**

| zip_match_detail | tract_resolution_method | rows |
| --- | --- | --- |
| One-to-Many Matched Exactly One Output | Tie Resolved via ZIP-Matching Ties | 15 |
| One-to-Many Matched Multiple Outputs | Tie Resolved via ZIP-Matching Ties | 3731 |
| One-to-Many Matched Multiple Outputs | Tract Ambiguous | 2238 |
| One-to-Many Matched No Output | Tract Ambiguous | 228 |
| One-to-Many Matched No Output | Tie Resolved via All Ties Unanimous | 78 |
| Original ZIP Missing | Tie Resolved via All Ties Unanimous | 236 |
| Original ZIP Missing | Tract Ambiguous | 171 |