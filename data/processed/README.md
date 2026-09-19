# Processed Data

This folder contains cleaned and analytical datasets generated during the data preparation workflow.

The processing workflow is implemented in:

`../../scripts/clean_data.py`

## Generated Files

- `machines_clean.csv` — cleaned machine information.
- `maintenance_clean.csv` — cleaned maintenance records.
- `failures_clean.csv` — cleaned failure records.
- `errors_clean.csv` — cleaned machine error records.
- `telemetry_clean.csv` — cleaned telemetry measurements.
- `asset_summary.csv` — machine-level analytical summary.
- `monthly_summary.csv` — aggregated monthly maintenance and failure metrics.
- `data_quality_report.csv` — data-quality validation output.

## Large File Note

`telemetry_clean.csv` is not included in this repository because of its file size (~96 MB). It can be reproduced from the source telemetry dataset using the project's data preparation workflow.

The remaining processed datasets are included for inspection and reproducibility.