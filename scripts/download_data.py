from pathlib import Path
from urllib.request import urlretrieve
from urllib.error import URLError, HTTPError

BASE_URL = "https://azuremlsampleexperiments.blob.core.windows.net/datasets"

FILES = [
    "PdM_telemetry.csv",
    "PdM_errors.csv",
    "PdM_maint.csv",
    "PdM_failures.csv",
    "PdM_machines.csv",
]

OUTPUT_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def download_dataset():
    for filename in FILES:
        target = OUTPUT_DIR / filename
        url = f"{BASE_URL}/{filename}"

        if target.exists():
            print(f"Skipping {filename} - file already exists.")
            continue

        print(f"Downloading {filename}...")

        try:
            urlretrieve(url, target)
            print(f"Saved -> {target}")

        except (HTTPError, URLError) as error:
            print(f"Failed to download {filename}: {error}")
            print(
                "Download the Microsoft Azure Predictive Maintenance "
                "dataset manually from Kaggle and place the CSV files "
                "inside data/raw/."
            )
            return

    print("Dataset download process completed.")


if __name__ == "__main__":
    download_dataset()