"""Download raw NASA OMNI2 hourly data and store as Parquet."""
import pandas as pd
import requests
from pathlib import Path

OMNI2_COLUMNS = [
    "year", "doy", "hour", "bartels_rotation", "imf_id", "plasma_id",
    "imf_n_pts", "plasma_n_pts", "b_mag_avg", "b_vec_mag", "b_lat_angle",
    "b_lon_angle", "bx_gse_gsm", "by_gse", "bz_gse", "by_gsm", "bz_gsm",
    "sigma_b_mag", "sigma_b_vec", "sigma_bx", "sigma_by", "sigma_bz",
    "proton_temp", "proton_density", "flow_speed", "flow_lon", "flow_lat",
    "na_np_ratio", "flow_pressure", "sigma_t", "sigma_n", "sigma_v",
    "sigma_phi_v", "sigma_theta_v", "sigma_na_np", "e_field", "plasma_beta",
    "alfven_mach", "kp_x10", "sunspot_r", "dst", "ae",
    "proton_flux_1mev", "proton_flux_2mev", "proton_flux_4mev",
    "proton_flux_10mev", "proton_flux_30mev", "proton_flux_60mev",
    "flag", "ap_index", "f107", "pc_index", "al", "au", "magnetosonic_mach",
]

RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

def fetch_year(year: int) -> pd.DataFrame:
    url = f"https://spdf.gsfc.nasa.gov/pub/data/omni/low_res_omni/omni2_{year}.dat"
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    lines = resp.text.strip().split("\n")
    rows = [line.split() for line in lines]
    df = pd.DataFrame(rows, columns=OMNI2_COLUMNS)
    return df.apply(pd.to_numeric)

def build_timestamp(df: pd.DataFrame) -> pd.Series:
    base = pd.to_datetime(df["year"].astype(str), format="%Y")
    return base + pd.to_timedelta(df["doy"] - 1, unit="D") + pd.to_timedelta(df["hour"], unit="h")

def main(start_year: int, end_year: int):
    frames = []
    for yr in range(start_year, end_year + 1):
        print(f"Fetching OMNI2 {yr}...")
        frames.append(fetch_year(yr))
    full = pd.concat(frames, ignore_index=True)
    full["timestamp"] = build_timestamp(full)
    out_path = RAW_DIR / "omni2_raw.parquet"
    full.to_parquet(out_path, index=False)
    print(f"Wrote {len(full):,} rows to {out_path}")

if __name__ == "__main__":
    main(start_year=2000, end_year=2025)