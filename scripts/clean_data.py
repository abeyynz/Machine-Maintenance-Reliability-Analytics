from pathlib import Path
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "processed"
OUT.mkdir(parents=True, exist_ok=True)

files = {
    "telemetry": "PdM_telemetry.csv",
    "errors": "PdM_errors.csv",
    "maintenance": "PdM_maint.csv",
    "failures": "PdM_failures.csv",
    "machines": "PdM_machines.csv",
}

dfs = {k: pd.read_csv(RAW / v) for k, v in files.items()}
quality = []
for name, df in dfs.items():
    quality.append({
        "table": name,
        "rows_raw": len(df),
        "columns": len(df.columns),
        "duplicate_rows_raw": int(df.duplicated().sum()),
        "missing_cells_raw": int(df.isna().sum().sum()),
    })

# Standardize headers without inventing source fields.
for name, df in dfs.items():
    df.columns = [c.strip() for c in df.columns]
    if "machineID" in df.columns:
        df["machineID"] = pd.to_numeric(df["machineID"], errors="raise").astype("int64")

for name in ["telemetry", "errors", "maintenance", "failures"]:
    dfs[name]["datetime"] = pd.to_datetime(dfs[name]["datetime"], errors="coerce")
    if dfs[name]["datetime"].isna().any():
        raise ValueError(f"Invalid datetime values found in {name}; inspect before proceeding.")

# Trim categorical text.
for name, cols in {
    "machines": ["model"], "errors": ["errorID"],
    "maintenance": ["comp"], "failures": ["failure"]
}.items():
    for col in cols:
        dfs[name][col] = dfs[name][col].astype(str).str.strip()

# Remove only exact duplicate rows; keep an audit trail in the report.
for name in dfs:
    dfs[name] = dfs[name].drop_duplicates().copy()

# Validate machine references.
valid_ids = set(dfs["machines"]["machineID"])
for name in ["telemetry", "errors", "maintenance", "failures"]:
    orphan = ~dfs[name]["machineID"].isin(valid_ids)
    if orphan.any():
        raise ValueError(f"{name} contains {int(orphan.sum())} orphan machine IDs.")

# Maintenance type is derived from dataset documentation: failures are breakdown-driven
# component replacements and are a subset of maintenance history.
maint = dfs["maintenance"].rename(columns={"comp": "component"})
fail = dfs["failures"].rename(columns={"failure": "component"})
reactive_keys = fail[["datetime", "machineID", "component"]].drop_duplicates().assign(is_failure=1)
maint = maint.merge(reactive_keys, on=["datetime", "machineID", "component"], how="left")
maint["maintenance_type"] = np.where(maint["is_failure"].eq(1), "Reactive", "Proactive")
maint = maint.drop(columns="is_failure")

# Calendar helper columns for BI/SQL.
for df in [maint, fail, dfs["errors"], dfs["telemetry"]]:
    df["date"] = df["datetime"].dt.date
    df["month"] = df["datetime"].dt.to_period("M").astype(str)
    df["year"] = df["datetime"].dt.year

# Asset summary.
machines = dfs["machines"].copy()
maintenance_agg = maint.groupby("machineID").agg(
    maintenance_events=("component", "size"),
    reactive_events=("maintenance_type", lambda s: (s == "Reactive").sum()),
    proactive_events=("maintenance_type", lambda s: (s == "Proactive").sum()),
).reset_index()
failure_agg = fail.groupby("machineID").size().rename("failure_events").reset_index()
error_agg = dfs["errors"].groupby("machineID").size().rename("error_events").reset_index()
asset_summary = machines.merge(maintenance_agg, on="machineID", how="left") \
    .merge(failure_agg, on="machineID", how="left") \
    .merge(error_agg, on="machineID", how="left")
for c in ["maintenance_events", "reactive_events", "proactive_events", "failure_events", "error_events"]:
    asset_summary[c] = asset_summary[c].fillna(0).astype(int)
asset_summary["reactive_rate"] = np.where(asset_summary["maintenance_events"] > 0,
    asset_summary["reactive_events"] / asset_summary["maintenance_events"], 0.0)

# Repeat-failure interval (descriptive proxy, NOT true MTBF).
f_sorted = fail.sort_values(["machineID", "datetime"]).copy()
f_sorted["days_since_previous_failure"] = f_sorted.groupby("machineID")["datetime"].diff().dt.total_seconds() / 86400
interval = f_sorted.groupby("machineID")["days_since_previous_failure"].mean().rename("mean_days_between_recorded_failures").reset_index()
asset_summary = asset_summary.merge(interval, on="machineID", how="left")

monthly_maint = maint.groupby("month").size().rename("maintenance_events")
monthly_fail = fail.groupby("month").size().rename("failure_events")
monthly_err = dfs["errors"].groupby("month").size().rename("error_events")
monthly_summary = pd.concat([monthly_maint, monthly_fail, monthly_err], axis=1).fillna(0).astype(int).reset_index()

# Final audit.
for item in quality:
    name = item["table"]
    final_df = maint if name == "maintenance" else fail if name == "failures" else dfs[name]
    item["rows_clean"] = len(final_df)
    item["duplicate_rows_clean"] = int(final_df.duplicated().sum())
    item["missing_cells_clean"] = int(final_df.isna().sum().sum())

pd.DataFrame(quality).to_csv(OUT / "data_quality_report.csv", index=False)
machines.to_csv(OUT / "machines_clean.csv", index=False)
maint.to_csv(OUT / "maintenance_clean.csv", index=False)
fail.to_csv(OUT / "failures_clean.csv", index=False)
dfs["errors"].to_csv(OUT / "errors_clean.csv", index=False)
dfs["telemetry"].to_csv(OUT / "telemetry_clean.csv", index=False)
asset_summary.to_csv(OUT / "asset_summary.csv", index=False)
monthly_summary.to_csv(OUT / "monthly_summary.csv", index=False)
print("Cleaning complete. Processed files saved to data/processed/.")
