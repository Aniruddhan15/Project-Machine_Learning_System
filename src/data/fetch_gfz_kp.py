"""Download raw GFZ Kp index data and store as Parquet."""
import pandas as pd
import requests
from pathlib import Path

RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)
BASE_URL = "https://kp.gfz.de/app/json/"

def fetch_range(start: str, end: str) -> pd.DataFrame:
    params = {"start": start, "end": end, "index": "Kp", "status": "def"}
    resp = requests.get(BASE_URL, params=params, timeout=60)
    resp.raise_for_status()
    data = resp.json()
    return pd.DataFrame({
        "timestamp": pd.to_datetime(data["datetime"]),
        "kp": data["Kp"],
        "status": data.get("status", [None] * len(data["Kp"])),
    })

def main(start_year: int, end_year: int):
    frames = []
    for yr in range(start_year, end_year + 1):
        print(f"Fetching GFZ Kp {yr}...")
        frames.append(fetch_range(f"{yr}-01-01T00:00:00Z", f"{yr}-12-31T23:59:59Z"))
    full = pd.concat(frames, ignore_index=True)
    out_path = RAW_DIR / "gfz_kp_raw.parquet"
    full.to_parquet(out_path, index=False)
    print(f"Wrote {len(full):,} rows to {out_path}")

if __name__ == "__main__":
    main(start_year=2000, end_year=2025)