from pathlib import Path
import csv


def clear_csv_entries_keep_header(csv_path: Path) -> None:
    """Remove all data rows from a CSV while keeping the header row."""
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found: {csv_path}")

    with csv_path.open("r", newline="", encoding="utf-8-sig") as infile:
        reader = csv.reader(infile)
        header = next(reader, None)

    if header is None:
        # File is empty; nothing to clear.
        return

    with csv_path.open("w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)


if __name__ == "__main__":
    repo_root = Path(__file__).resolve().parents[1]
    target_csv = repo_root / "data" / "1_derived" / "3_sf_properties_census_geocoded.csv"
    clear_csv_entries_keep_header(target_csv)
    print(f"Cleared all data rows and kept header in: {target_csv}")
