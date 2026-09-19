# Raw Data

This folder contains the original source files from the **Microsoft Azure Predictive Maintenance** dataset available on Kaggle.

## Source

[Microsoft Azure Predictive Maintenance — Kaggle](https://www.kaggle.com/datasets/arnabbiswas1/microsoft-azure-predictive-maintenance)

Expected source files:

- `PdM_telemetry.csv`
- `PdM_errors.csv`
- `PdM_maint.csv`
- `PdM_failures.csv`
- `PdM_machines.csv`

The source files are kept unchanged before the data cleaning and transformation process.

## Large File Note

`PdM_telemetry.csv` is not included in this repository because of its file size (~76 MB). It can be downloaded directly from the Kaggle dataset linked above.

The remaining smaller source files are included to make the project structure and workflow easier to inspect.

> Note: `scripts/download_data.py` was created to support dataset retrieval, but the source dataset used in this project was ultimately downloaded manually from Kaggle.