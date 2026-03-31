# SF ZIP Code Match Report

- Generated: 2026-03-30 04:52:39
- Input file: ../../data/1_derived/3_sf_properties_census_geocoded.csv
- Total rows: 9,352
- `match_type` defines relationship shape: One-to-One vs One-to-Many.
- `zip_match_detail` defines exact ZIP comparison outcome within each shape.
- `flag` is True only for non-match outcomes (One-to-One Did Not Match and One-to-Many Matched No Output).
- All expected variations are shown; missing ones are reported as 0.

## Match Type Counts
| match_type | rows | pct |
| --- | --- | --- |
| One-to-One | 9334 | 99.81 |
| One-to-Many | 18 | 0.19 |

## ZIP Match Detail Counts
| zip_match_detail | rows | pct |
| --- | --- | --- |
| One-to-One Matched | 8937 | 95.56 |
| One-to-One Did Not Match | 42 | 0.45 |
| One-to-Many Matched Exactly One Output | 0 | 0.0 |
| One-to-Many Matched Multiple Outputs | 12 | 0.13 |
| One-to-Many Matched No Output | 6 | 0.06 |
| Geocoder ZIP Missing | 354 | 3.79 |
| Original ZIP Missing | 1 | 0.01 |

## Flag Counts
| flag | flag_detail | rows |
| --- | --- | --- |
| True | One-to-One Did Not Match | 42 |
| True | One-to-Many Matched No Output | 6 |
| False |  | 9304 |

## Match Type x ZIP Detail
| match_type | zip_match_detail | rows |
| --- | --- | --- |
| One-to-One | One-to-One Matched | 8937 |
| One-to-One | One-to-One Did Not Match | 42 |
| One-to-One | Geocoder ZIP Missing | 354 |
| One-to-One | Original ZIP Missing | 1 |
| One-to-Many | One-to-Many Matched Exactly One Output | 0 |
| One-to-Many | One-to-Many Matched Multiple Outputs | 12 |
| One-to-Many | One-to-Many Matched No Output | 6 |
| One-to-Many | Geocoder ZIP Missing | 0 |
| One-to-Many | Original ZIP Missing | 0 |

## Original Geocoder Match x ZIP Detail
| match | zip_match_detail | rows |
| --- | --- | --- |
| (blank) | Geocoder ZIP Missing | 1 |
| Match | One-to-One Matched | 8937 |
| Match | One-to-One Did Not Match | 42 |
| Match | Original ZIP Missing | 1 |
| No_Match | Geocoder ZIP Missing | 353 |
| Tie | One-to-Many Matched Multiple Outputs | 12 |
| Tie | One-to-Many Matched No Output | 6 |

## Sample Flagged Rows (Top 25)
| PropertyId | match | match_type | Address.PostalCode | matched_address | tie_matched_addresses | zip_original | zip_geocoder_all_str | tie_candidate_count | matching_output_count | zip_match_detail | flag | flag_detail | final_lat | final_long | census_tract |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 320469.0 | Match | One-to-One | 94111.0 | 1 THE EMBARCADERO, SAN FRANCISCO, CA, 94107 |  | 94111 | 94107 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 61508.0 |
| 320471.0 | Match | One-to-One | 94111.0 | 3 THE EMBARCADERO, SAN FRANCISCO, CA, 94107 |  | 94111 | 94107 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 61508.0 |
| 322770.0 | Match | One-to-One | 94103.0 | 245 VAN NESS AVE, SAN FRANCISCO, CA, 94102 |  | 94103 | 94102 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 16200.0 |
| 323170.0 | Match | One-to-One | 94133.0 | 2 N POINT ST, SAN FRANCISCO, CA, 94109 |  | 94133 | 94109 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 10101.0 |
| 334971.0 | Match | One-to-One | 94080.0 | 1265 MISSION ST, SAN FRANCISCO, CA, 94103 |  | 94080 | 94103 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 17603.0 |
| 365252.0 | Tie | One-to-Many | 94105.0 | 26 PIER, SAN FRANCISCO, CA, 94111 | 26 PIER, SAN FRANCISCO, CA, 94111 \| 26 PIER, SAN FRANCISCO, CA, 94124 | 94105 | 94111 \| 94124 | 2 | 0 | One-to-Many Matched No Output | True | One-to-Many Matched No Output |  |  | 10500.0 |
| 610198.0 | Match | One-to-One | 94129.0 | 38 KEYES ALY, SAN FRANCISCO, CA, 94133 |  | 94129 | 94133 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 10701.0 |
| 683604.0 | Match | One-to-One | 94129.0 | 9 FUNSTON AVE, SAN FRANCISCO, CA, 94118 |  | 94129 | 94118 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 40200.0 |
| 683606.0 | Match | One-to-One | 94129.0 | 10 FUNSTON AVE, SAN FRANCISCO, CA, 94118 |  | 94129 | 94118 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 40200.0 |
| 704054.0 | Match | One-to-One | 94102.0 | 108 TAYLOR RD, SAN FRANCISCO, CA, 94129 |  | 94102 | 94129 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 60100.0 |
| 744326.0 | Match | One-to-One | 94129.0 | 211 LINCOLN WAY, SAN FRANCISCO, CA, 94122 |  | 94129 | 94122 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 30101.0 |
| 745372.0 | Match | One-to-One | 94129.0 | 1185 MASON ST, SAN FRANCISCO, CA, 94108 |  | 94129 | 94108 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 11200.0 |
| 745373.0 | Match | One-to-One | 94129.0 | 1187 MASON ST, SAN FRANCISCO, CA, 94108 |  | 94129 | 94108 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 11200.0 |
| 760583.0 | Match | One-to-One | 94109.0 | 1000 S VAN NESS AVE, SAN FRANCISCO, CA, 94110 |  | 94109 | 94110 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 20801.0 |
| 768159.0 | Match | One-to-One | 94129.0 | 222 HALLECK ST, SAN FRANCISCO, CA, 94104 |  | 94129 | 94104 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 11700.0 |
| 778285.0 | Match | One-to-One | 94111.0 | 5 THE EMBARCADERO, SAN FRANCISCO, CA, 94107 |  | 94111 | 94107 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 61508.0 |
| 782910.0 | Match | One-to-One | 94129.0 | 7 FUNSTON AVE, SAN FRANCISCO, CA, 94118 |  | 94129 | 94118 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 40200.0 |
| 786231.0 | Match | One-to-One | 94129.0 | 100 MONTGOMERY ST, SAN FRANCISCO, CA, 94104 |  | 94129 | 94104 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 11700.0 |
| 844850.0 | Match | One-to-One | 94129.0 | 215 LINCOLN WAY, SAN FRANCISCO, CA, 94122 |  | 94129 | 94122 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 30101.0 |
| 850617.0 | Match | One-to-One | 94015.0 | 331 WESTLAKE AVE, DALY CITY, CA, 94014 |  | 94015 | 94014 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 600600.0 |
| 1352783.0 | Match | One-to-One | 94105.0 | 3 JACKSON ST, SAN FRANCISCO, CA, 94111 |  | 94105 | 94111 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 10500.0 |
| 1352787.0 | Tie | One-to-Many | 94105.0 | 5 PACIFIC AVE, SAN FRANCISCO, CA, 94111 | 5 PACIFIC AVE, SAN FRANCISCO, CA, 94111 \| 5 PACIFIC AVE, SAN FRANCISCO, CA, 94133 | 94105 | 94111 \| 94133 | 2 | 0 | One-to-Many Matched No Output | True | One-to-Many Matched No Output |  |  | 10500.0 |
| 5580579.0 | Match | One-to-One | 94101.0 | 2381 CHESTNUT ST, SAN FRANCISCO, CA, 94123 |  | 94101 | 94123 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 12801.0 |
| 6331737.0 | Match | One-to-One | 94015.0 | 415 WESTLAKE AVE, DALY CITY, CA, 94014 |  | 94015 | 94014 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 600600.0 |
| 6671033.0 | Match | One-to-One | 94015.0 | 406 WESTLAKE AVE, DALY CITY, CA, 94014 |  | 94015 | 94014 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 600600.0 |

## One-to-Many: Matched Exactly One Output (Top 25)
_No rows to display._

## One-to-Many: Matched Multiple Outputs (Top 25)
| PropertyId | Address.PostalCode | tie_matched_addresses | zip_original | matching_output_count | final_lat | final_long |
| --- | --- | --- | --- | --- | --- | --- |
| 321580.0 | 94124.0 | 1485 BAY SHORE BLVD, SAN FRANCISCO, CA, 94124 \| 1485 BAYSHORE BLVD, SAN FRANCISCO, CA, 94124 | 94124 | 2 | MULTIPLE_MATCHING_OUTPUTS: 37.725535736384 \| 37.725535736384 | MULTIPLE_MATCHING_OUTPUTS: -122.401401989518 \| -122.401401989518 |
| 333689.0 | 94403.0 | 3130 LA SELVA CIR, SAN MATEO, CA, 94403 \| 3130 LA SELVA ST, SAN MATEO, CA, 94403 | 94403 | 2 | MULTIPLE_MATCHING_OUTPUTS: 37.542678745951 \| 37.54307237241 | MULTIPLE_MATCHING_OUTPUTS: -122.284437924233 \| -122.285084558557 |
| 783773.0 | 94401.0 | 256 S EL CAMINO REAL, SAN MATEO, CA, 94401 \| 256 N EL CAMINO REAL, SAN MATEO, CA, 94401 | 94401 | 2 | MULTIPLE_MATCHING_OUTPUTS: 37.563454197511 \| 37.568959419958 | MULTIPLE_MATCHING_OUTPUTS: -122.326559076275 \| -122.333189329068 |
| 845493.0 | 94015.0 | 100 SKYLINE BLVD, DALY CITY, CA, 94015 \| 100 SKYLINE DR, DALY CITY, CA, 94015 | 94015 | 2 | MULTIPLE_MATCHING_OUTPUTS: 37.673925650836 \| 37.691764185401 | MULTIPLE_MATCHING_OUTPUTS: -122.488596769759 \| -122.494884037259 |
| 4318893.0 | 94133.0 | 435 BROADWAY ST, SAN FRANCISCO, CA, 94133 \| 435 BROADWAY, SAN FRANCISCO, CA, 94133 | 94133 | 2 | MULTIPLE_MATCHING_OUTPUTS: 37.798087228536 \| 37.798087228536 | MULTIPLE_MATCHING_OUTPUTS: -122.404443200708 \| -122.404443200708 |
| 4327803.0 | 94005.0 | 88 S HILL DR, BRISBANE, CA, 94005 \| 88 W HILL DR, BRISBANE, CA, 94005 | 94005 | 2 | MULTIPLE_MATCHING_OUTPUTS: 37.686556712518 \| 37.692860513616 | MULTIPLE_MATCHING_OUTPUTS: -122.411619079175 \| -122.421788578945 |
| 4570159.0 | 94401.0 | 313 S SAN MATEO DR, SAN MATEO, CA, 94401 \| 313 N SAN MATEO DR, SAN MATEO, CA, 94401 | 94401 | 2 | MULTIPLE_MATCHING_OUTPUTS: 37.564197193327 \| 37.571051391926 | MULTIPLE_MATCHING_OUTPUTS: -122.323970606746 \| -122.331329802994 |
| 5027545.0 | 94066.0 | 751 SAN BRUNO AVE W, SAN BRUNO, CA, 94066 \| 751 SAN BRUNO AVE E, SAN BRUNO, CA, 94066 | 94066 | 2 | MULTIPLE_MATCHING_OUTPUTS: 37.628528342383 \| 37.630969151044 | MULTIPLE_MATCHING_OUTPUTS: -122.417215794707 \| -122.406114264877 |
| 5034363.0 | 94066.0 | 777 SAN BRUNO AVE W, SAN BRUNO, CA, 94066 \| 777 SAN BRUNO AVE E, SAN BRUNO, CA, 94066 | 94066 | 2 | MULTIPLE_MATCHING_OUTPUTS: 37.628498597917 \| 37.6309735587 | MULTIPLE_MATCHING_OUTPUTS: -122.417293460825 \| -122.405808919857 |
| 5344465.0 | 94066.0 | 675 SAN BRUNO AVE W, SAN BRUNO, CA, 94066 \| 675 SAN BRUNO AVE E, SAN BRUNO, CA, 94066 | 94066 | 2 | MULTIPLE_MATCHING_OUTPUTS: 37.628849658651 \| 37.630955198054 | MULTIPLE_MATCHING_OUTPUTS: -122.416374331022 \| -122.407031937646 |
| 6395899.0 | 94015.0 | 31 SKYLINE BLVD, DALY CITY, CA, 94015 \| 31 SKYLINE DR, DALY CITY, CA, 94015 | 94015 | 2 | MULTIPLE_MATCHING_OUTPUTS: 37.677628487762 \| 37.693853937592 | MULTIPLE_MATCHING_OUTPUTS: -122.48994771527 \| -122.495688149313 |
| 8930622.0 | 94063.0 | 499 SEAPORT BLVD, REDWOOD CITY, CA, 94063 \| 499 SEAPORT CT, REDWOOD CITY, CA, 94063 | 94063 | 2 | MULTIPLE_MATCHING_OUTPUTS: 37.49849564196 \| 37.50297070501 | MULTIPLE_MATCHING_OUTPUTS: -122.212266111685 \| -122.211757491611 |