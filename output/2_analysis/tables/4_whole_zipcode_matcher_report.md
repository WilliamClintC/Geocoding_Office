# Whole ZIP Code Match Report (Batches 001-011)

- Generated: 2026-03-31 05:17:23
- Input files: 11 batch files
- Total rows: 1,051,219
- Aggregation scope: all whole batches 001-011 combined.
- `flag` is True only for non-match outcomes (One-to-One Did Not Match and One-to-Many Matched No Output).

## Match Type Counts
| match_type | rows | pct |
| --- | --- | --- |
| One-to-One | 1044522 | 99.36 |
| One-to-Many | 6697 | 0.64 |

## ZIP Match Detail Counts
| zip_match_detail | rows | pct |
| --- | --- | --- |
| One-to-One Matched | 886635 | 84.34 |
| One-to-One Did Not Match | 6977 | 0.66 |
| One-to-Many Matched Exactly One Output | 15 | 0.0 |
| One-to-Many Matched Multiple Outputs | 5969 | 0.57 |
| One-to-Many Matched No Output | 306 | 0.03 |
| Geocoder ZIP Missing | 67721 | 6.44 |
| Original ZIP Missing | 83596 | 7.95 |

## Flag Counts
| flag | flag_detail | rows |
| --- | --- | --- |
| True | One-to-One Did Not Match | 6977 |
| True | One-to-Many Matched No Output | 306 |
| False |  | 1043936 |

## Match Type x ZIP Detail
| match_type | zip_match_detail | rows |
| --- | --- | --- |
| One-to-One | One-to-One Matched | 886635 |
| One-to-One | One-to-One Did Not Match | 6977 |
| One-to-One | Geocoder ZIP Missing | 67721 |
| One-to-One | Original ZIP Missing | 83189 |
| One-to-Many | One-to-Many Matched Exactly One Output | 15 |
| One-to-Many | One-to-Many Matched Multiple Outputs | 5969 |
| One-to-Many | One-to-Many Matched No Output | 306 |
| One-to-Many | Geocoder ZIP Missing | 0 |
| One-to-Many | Original ZIP Missing | 407 |

## Original Geocoder Match x ZIP Detail
| match | zip_match_detail | rows |
| --- | --- | --- |
| (blank) | Geocoder ZIP Missing | 657 |
| (blank) | Original ZIP Missing | 28 |
| Match | One-to-One Matched | 886635 |
| Match | Original ZIP Missing | 76870 |
| Match | One-to-One Did Not Match | 6977 |
| No_Match | Geocoder ZIP Missing | 67064 |
| No_Match | Original ZIP Missing | 6291 |
| Tie | One-to-Many Matched Multiple Outputs | 5969 |
| Tie | Original ZIP Missing | 407 |
| Tie | One-to-Many Matched No Output | 306 |
| Tie | One-to-Many Matched Exactly One Output | 15 |

## Sample Flagged Rows (Top 25)
| PropertyId | source_batch | match | match_type | Address.PostalCode | matched_address | tie_matched_addresses | zip_original | zip_geocoder_all_str | tie_candidate_count | matching_output_count | zip_match_detail | flag | flag_detail | final_lat | final_long | census_tract |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 441136.0 | 001 | Match | One-to-One | 30326.0 | 945 E PACES FERRY RD NE, ATLANTA, GA, 30305 |  | 30326 | 30305 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 9606.0 |
| 7340375.0 | 001 | Match | One-to-One | 30518.0 | 2851 BUFORD DR, BUFORD, GA, 30519 |  | 30518 | 30519 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 50611.0 |
| 10942609.0 | 001 | Tie | One-to-Many | 30094.0 | 4461 STATE RTE 20, CONYERS, GA, 30012 | 4461 STATE RTE 20, CONYERS, GA, 30012 \| 4461 STATE RTE 20, CONYERS, GA, 30013 | 30094 | 30012 \| 30013 | 2 | 0 | One-to-Many Matched No Output | True | One-to-Many Matched No Output |  |  | 60103.0 |
| 8369380.0 | 001 | Match | One-to-One | 31702.0 | 1305 EVELYN AVE, ALBANY, GA, 31705 |  | 31702 | 31705 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 10302.0 |
| 8337462.0 | 001 | Match | One-to-One | 31901.0 | 2100 COMER AVE, COLUMBUS, GA, 31904 |  | 31901 | 31904 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 11100.0 |
| 443444.0 | 001 | Tie | One-to-Many | 30309.0 | 1492 PIEDMONT AVE NE, ATLANTA, GA, 30303 | 1492 PIEDMONT AVE NE, ATLANTA, GA, 30303 \| 1492 PIEDMONT AVE NE, ATLANTA, GA, 30324 | 30309 | 30303 \| 30324 | 2 | 0 | One-to-Many Matched No Output | True | One-to-Many Matched No Output |  |  | 2802.0 |
| 816448.0 | 001 | Match | One-to-One | 30310.0 | 660 UNIVERSITY AVE, ATLANTA, GA, 30315 |  | 30310 | 30315 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 6300.0 |
| 7376306.0 | 001 | Match | One-to-One | 30312.0 | 540 CENTRAL AVE, ATLANTA, GA, 30354 |  | 30312 | 30354 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 10801.0 |
| 618098.0 | 001 | Match | One-to-One | 30329.0 | 1600 E CLIFTON RD NE, ATLANTA, GA, 30307 |  | 30329 | 30307 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 22403.0 |
| 1299460.0 | 001 | Match | One-to-One | 30311.0 | 798 CASCADE RD, ATLANTA, GA, 30310 |  | 30311 | 30310 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 6000.0 |
| 441488.0 | 001 | Match | One-to-One | 30344.0 | 3800 N CAMP CREEK PKWY SW, ATLANTA, GA, 30331 |  | 30344 | 30331 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 7711.0 |
| 799407.0 | 001 | Match | One-to-One | 30363.0 | 171 17TH ST NW, ATLANTA, GA, 30309 |  | 30363 | 30309 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 501.0 |
| 443135.0 | 001 | Match | One-to-One | 30309.0 | 67 PEACHTREE PARK DR NE, ATLANTA, GA, 30305 |  | 30309 | 30305 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 9106.0 |
| 438770.0 | 001 | Match | One-to-One | 30319.0 | 1934 N DRUID HILLS RD NE, ATLANTA, GA, 30329 |  | 30319 | 30329 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 21417.0 |
| 4147018.0 | 001 | Match | One-to-One | 30318.0 | 1311A FULTON INDUSTRIAL BLVD NW, ATLANTA, GA, 30336 |  | 30318 | 30336 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 8202.0 |
| 441818.0 | 001 | Tie | One-to-Many | 30023.0 | 11350 OLD ROSWELL RD, ALPHARETTA, GA, 30004 | 11350 OLD ROSWELL RD, ALPHARETTA, GA, 30004 \| 11350 OLD ROSWELL RD, ALPHARETTA, GA, 30009 | 30023 | 30004 \| 30009 | 2 | 0 | One-to-Many Matched No Output | True | One-to-Many Matched No Output |  |  | 11647.0 |
| 6355918.0 | 001 | Match | One-to-One | 30301.0 | 2450 PIEDMONT RD NE, ATLANTA, GA, 30324 |  | 30301 | 30324 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 9405.0 |
| 693603.0 | 001 | Match | One-to-One | 30120.0 | 970 JOE FRANK HARRIS PKWY, CARTERSVILLE, GA, 30121 |  | 30120 | 30121 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 960403.0 |
| 440884.0 | 001 | Match | One-to-One | 30331.0 | 2945 HOGAN RD, ATLANTA, GA, 30344 |  | 30331 | 30344 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 11301.0 |
| 5024371.0 | 001 | Match | One-to-One | 30013.0 | 2203 STATE RTE 20, CONYERS, GA, 30012 |  | 30013 | 30012 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 60101.0 |
| 443386.0 | 001 | Match | One-to-One | 30308.0 | 699 PONCE DE LEON MANOR NE, ATLANTA, GA, 30307 |  | 30308 | 30307 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 22403.0 |
| 5392936.0 | 001 | Match | One-to-One | 30345.0 | 4300 BUFORD HWY NE, ATLANTA, GA, 30341 |  | 30345 | 30341 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 21204.0 |
| 7655724.0 | 001 | Match | One-to-One | 30310.0 | 565 NORTHSIDE DR SW, ATLANTA, GA, 30313 |  | 30310 | 30313 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 3600.0 |
| 443085.0 | 001 | Match | One-to-One | 30318.0 | 1224 COLLIER ST NW, ATLANTA, GA, 30314 |  | 30318 | 30314 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 8400.0 |
| 443416.0 | 001 | Match | One-to-One | 30349.0 | 4504 WASHINGTON RD, ATLANTA, GA, 30344 |  | 30349 | 30344 | 0 | 0 | One-to-One Did Not Match | True | One-to-One Did Not Match |  |  | 11306.0 |