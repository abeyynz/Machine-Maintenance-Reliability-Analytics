from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"
IMG = ROOT / "images"
IMG.mkdir(exist_ok=True)

maint = pd.read_csv(DATA / "maintenance_clean.csv", parse_dates=["datetime"])
fail = pd.read_csv(DATA / "failures_clean.csv", parse_dates=["datetime"])
machines = pd.read_csv(DATA / "machines_clean.csv")
assets = pd.read_csv(DATA / "asset_summary.csv")
monthly = pd.read_csv(DATA / "monthly_summary.csv")

# 1. Maintenance type
ax = maint["maintenance_type"].value_counts().plot(kind="bar", title="Maintenance Events by Type")
ax.set_xlabel("Maintenance type"); ax.set_ylabel("Events")
plt.tight_layout(); plt.savefig(IMG / "maintenance_type.png", dpi=160); plt.close()

# 2. Failure component
ax = fail["component"].value_counts().plot(kind="bar", title="Failures by Component")
ax.set_xlabel("Component"); ax.set_ylabel("Failures")
plt.tight_layout(); plt.savefig(IMG / "failures_by_component.png", dpi=160); plt.close()

# 3. Monthly trends
monthly.plot(x="month", y=["maintenance_events", "failure_events"], kind="line", marker="o", title="Monthly Maintenance and Failures")
plt.xticks(rotation=45, ha="right"); plt.tight_layout(); plt.savefig(IMG / "monthly_trend.png", dpi=160); plt.close()

# 4. Machine age vs failures
ax = assets.plot.scatter(x="age", y="failure_events", title="Machine Age vs Failure Events")
ax.set_xlabel("Machine age (years)"); ax.set_ylabel("Failure events")
plt.tight_layout(); plt.savefig(IMG / "age_vs_failures.png", dpi=160); plt.close()

# 5. Top assets
assets.nlargest(10, "failure_events").sort_values("failure_events").plot.barh(x="machineID", y="failure_events", title="Top 10 Assets by Failure Events", legend=False)
plt.xlabel("Failure events"); plt.tight_layout(); plt.savefig(IMG / "top_failure_assets.png", dpi=160); plt.close()

print("EDA charts saved to images/.")
