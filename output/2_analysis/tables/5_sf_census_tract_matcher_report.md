# SF Census Tract Match Report

- Generated: 2026-05-05 01:12:57
- Input file: ../../data/1_derived/4_sf_zipcode_matcher.csv
- Output file: ../../data/1_derived/5_sf_census_tract_matcher.csv
- Total rows: 9,352
- Rows resolved to a single census tract: 8,985 (96.08%)
- Rows flagged (ambiguous or missing): 367 (3.92%)

## Tract Resolution Method Counts
| tract_resolution_method | rows | pct |
| --- | --- | --- |
| One-to-One Primary | 8980 | 96.02 |
| Tract Missing | 354 | 3.79 |
| Tract Ambiguous | 13 | 0.14 |
| Tie Resolved via ZIP-Matching Ties | 5 | 0.05 |

## Tie Rows: Tract Resolution by ZIP Match Detail
Total One-to-Many (tie) rows: 18.

- Tie rows whose ZIP-matching ties all share the same tract: **5**
- Tie rows where every tie (regardless of ZIP) shares the same tract: **5**
- Tie rows resolved to a single tract (final): **5**
- Tie rows ambiguous (multiple distinct tracts): **13**
- Tie rows missing tract data: **0**

| zip_match_detail | tract_resolution_method | rows |
| --- | --- | --- |
| One-to-Many Matched Multiple Outputs | Tract Ambiguous | 7 |
| One-to-Many Matched Multiple Outputs | Tie Resolved via ZIP-Matching Ties | 5 |
| One-to-Many Matched No Output | Tract Ambiguous | 6 |

## All Tie Rows (Detail)
| PropertyId | Address.PostalCode | matched_address | tie_matched_addresses | tie_geoids | primary_tract | tie_tracts_all_str | tie_tracts_zip_str | tie_tract_unique_count_all | tie_tract_unique_count_zip | tract_consistent_in_zip_matches | tract_consistent_in_all_ties | tract_resolution_method | final_census_tract |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 321580.0 | 94124.0 | 1485 BAY SHORE BLVD, SAN FRANCISCO, CA, 94124 | 1485 BAY SHORE BLVD, SAN FRANCISCO, CA, 94124 \| 1485 BAYSHORE BLVD, SAN FRANCISCO, CA, 94124 | 060750233002003 \| 060750233002003 | 023300 | 023300 \| 023300 | 023300 \| 023300 | 1 | 1 | True | True | Tie Resolved via ZIP-Matching Ties | 023300 |
| 333689.0 | 94403.0 | 3130 LA SELVA CIR, SAN MATEO, CA, 94403 | 3130 LA SELVA CIR, SAN MATEO, CA, 94403 \| 3130 LA SELVA ST, SAN MATEO, CA, 94403 | 060816084003008 \| 060816084003001 | 608400 | 608400 \| 608400 | 608400 \| 608400 | 1 | 1 | True | True | Tie Resolved via ZIP-Matching Ties | 608400 |
| 365252.0 | 94105.0 | 26 PIER, SAN FRANCISCO, CA, 94111 | 26 PIER, SAN FRANCISCO, CA, 94111 \| 26 PIER, SAN FRANCISCO, CA, 94124 | 060750105002002 \| 060759809001017 | 010500 | 010500 \| 980900 |  | 2 | 0 |  | False | Tract Ambiguous |  |
| 783773.0 | 94401.0 | 256 S EL CAMINO REAL, SAN MATEO, CA, 94401 | 256 S EL CAMINO REAL, SAN MATEO, CA, 94401 \| 256 N EL CAMINO REAL, SAN MATEO, CA, 94401 | 060816064005002 \| 060816059022004 | 606400 | 606400 \| 605902 | 606400 \| 605902 | 2 | 2 | False | False | Tract Ambiguous |  |
| 845493.0 | 94015.0 | 100 SKYLINE BLVD, DALY CITY, CA, 94015 | 100 SKYLINE BLVD, DALY CITY, CA, 94015 \| 100 SKYLINE DR, DALY CITY, CA, 94015 | 060816015011000 \| 060816010004000 | 601501 | 601501 \| 601000 | 601501 \| 601000 | 2 | 2 | False | False | Tract Ambiguous |  |
| 1352787.0 | 94105.0 | 5 PACIFIC AVE, SAN FRANCISCO, CA, 94111 | 5 PACIFIC AVE, SAN FRANCISCO, CA, 94111 \| 5 PACIFIC AVE, SAN FRANCISCO, CA, 94133 | 060750105002006 \| 060750108002001 | 010500 | 010500 \| 010800 |  | 2 | 0 |  | False | Tract Ambiguous |  |
| 4318893.0 | 94133.0 | 435 BROADWAY ST, SAN FRANCISCO, CA, 94133 | 435 BROADWAY ST, SAN FRANCISCO, CA, 94133 \| 435 BROADWAY, SAN FRANCISCO, CA, 94133 | 060750106002006 \| 060750106002006 | 010600 | 010600 \| 010600 | 010600 \| 010600 | 1 | 1 | True | True | Tie Resolved via ZIP-Matching Ties | 010600 |
| 4327803.0 | 94005.0 | 88 S HILL DR, BRISBANE, CA, 94005 | 88 S HILL DR, BRISBANE, CA, 94005 \| 88 W HILL DR, BRISBANE, CA, 94005 | 060816001002017 \| 060816001002013 | 600100 | 600100 \| 600100 | 600100 \| 600100 | 1 | 1 | True | True | Tie Resolved via ZIP-Matching Ties | 600100 |
| 4570159.0 | 94401.0 | 313 S SAN MATEO DR, SAN MATEO, CA, 94401 | 313 S SAN MATEO DR, SAN MATEO, CA, 94401 \| 313 N SAN MATEO DR, SAN MATEO, CA, 94401 | 060816063003022 \| 060816059021003 | 606300 | 606300 \| 605902 | 606300 \| 605902 | 2 | 2 | False | False | Tract Ambiguous |  |
| 5027545.0 | 94066.0 | 751 SAN BRUNO AVE W, SAN BRUNO, CA, 94066 | 751 SAN BRUNO AVE W, SAN BRUNO, CA, 94066 \| 751 SAN BRUNO AVE E, SAN BRUNO, CA, 94066 | 060816040001002 \| 060816042001004 | 604000 | 604000 \| 604200 | 604000 \| 604200 | 2 | 2 | False | False | Tract Ambiguous |  |
| 5034363.0 | 94066.0 | 777 SAN BRUNO AVE W, SAN BRUNO, CA, 94066 | 777 SAN BRUNO AVE W, SAN BRUNO, CA, 94066 \| 777 SAN BRUNO AVE E, SAN BRUNO, CA, 94066 | 060816040001002 \| 060816042001004 | 604000 | 604000 \| 604200 | 604000 \| 604200 | 2 | 2 | False | False | Tract Ambiguous |  |
| 5344465.0 | 94066.0 | 675 SAN BRUNO AVE W, SAN BRUNO, CA, 94066 | 675 SAN BRUNO AVE W, SAN BRUNO, CA, 94066 \| 675 SAN BRUNO AVE E, SAN BRUNO, CA, 94066 | 060816041042006 \| 060816042001014 | 604104 | 604104 \| 604200 | 604104 \| 604200 | 2 | 2 | False | False | Tract Ambiguous |  |
| 6395899.0 | 94015.0 | 31 SKYLINE BLVD, DALY CITY, CA, 94015 | 31 SKYLINE BLVD, DALY CITY, CA, 94015 \| 31 SKYLINE DR, DALY CITY, CA, 94015 | 060816015011000 \| 060816010001000 | 601501 | 601501 \| 601000 | 601501 \| 601000 | 2 | 2 | False | False | Tract Ambiguous |  |
| 8919922.0 | 94107.0 | 70 PIER, SAN FRANCISCO, CA, 94111 | 70 PIER, SAN FRANCISCO, CA, 94111 \| 70 PIER, SAN FRANCISCO, CA, 94124 | 060750105002002 \| 060759809001017 | 010500 | 010500 \| 980900 |  | 2 | 0 |  | False | Tract Ambiguous |  |
| 8919951.0 | 94107.0 | 70 PIER, SAN FRANCISCO, CA, 94111 | 70 PIER, SAN FRANCISCO, CA, 94111 \| 70 PIER, SAN FRANCISCO, CA, 94124 | 060750105002002 \| 060759809001017 | 010500 | 010500 \| 980900 |  | 2 | 0 |  | False | Tract Ambiguous |  |
| 8920002.0 | 94107.0 | 70 PIER, SAN FRANCISCO, CA, 94111 | 70 PIER, SAN FRANCISCO, CA, 94111 \| 70 PIER, SAN FRANCISCO, CA, 94124 | 060750105002002 \| 060759809001017 | 010500 | 010500 \| 980900 |  | 2 | 0 |  | False | Tract Ambiguous |  |
| 8930622.0 | 94063.0 | 499 SEAPORT BLVD, REDWOOD CITY, CA, 94063 | 499 SEAPORT BLVD, REDWOOD CITY, CA, 94063 \| 499 SEAPORT CT, REDWOOD CITY, CA, 94063 | 060816103021005 \| 060816103021005 | 610302 | 610302 \| 610302 | 610302 \| 610302 | 1 | 1 | True | True | Tie Resolved via ZIP-Matching Ties | 610302 |
| 9506693.0 | 94107.0 | 70 PIER, SAN FRANCISCO, CA, 94111 | 70 PIER, SAN FRANCISCO, CA, 94111 \| 70 PIER, SAN FRANCISCO, CA, 94124 | 060750105002002 \| 060759809001017 | 010500 | 010500 \| 980900 |  | 2 | 0 |  | False | Tract Ambiguous |  |