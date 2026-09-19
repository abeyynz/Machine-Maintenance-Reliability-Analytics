from pathlib import Path
from urllib.request import urlretrieve

BASE = "https://azuremlsampleexperiments.blob.core.windows.net/datasets"
FILES = ["PdM_telemetry.csv", "PdM_errors.csv", "PdM_maint.csv", "PdM_failures.csv", "PdM_machines.csv"]
OUT = Path(__file__).resolve().parents[1] / "data" / "raw"
OUT.mkdir(parents=True, exist_ok=True)

for name in FILES:
    target = OUT / name
    print(f"Downloading {name} ...")
    urlretrieve(f"{BASE}/{name}", target)
    print(f"Saved -> {target}")
print("Done.")
