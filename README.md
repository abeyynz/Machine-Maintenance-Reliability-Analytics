# Building Maintenance & Operations Performance Analysis

A portfolio case study that demonstrates an end-to-end analytics workflow: **Excel data audit -> Python/Pandas cleaning -> EDA -> PostgreSQL analysis -> Power BI dashboard -> business interpretation**.

> **Data integrity note:** the original case-study idea included maintenance cost and downtime. The selected public dataset does not contain cost, downtime, location, technician, or work-order status. Those fields are **not fabricated**. The KPI scope is adapted to maintenance, failures, errors, machine characteristics and operational telemetry.

## Business problem
Management wants to understand which assets are generating the most maintenance and failure activity, whether maintenance is mainly proactive or reactive, which components fail most often, how reliability patterns change over time, and which machines deserve closer investigation.

## Dataset
This project uses the **Microsoft Azure Predictive Maintenance** benchmark dataset, distributed as five related tables: telemetry, errors, maintenance, failures and machine metadata. The dataset documentation explains that maintenance records capture component replacements and that failures are breakdown-driven replacements contained within maintenance history.

Source/documentation: https://www.kaggle.com/datasets/arnabbiswas1/microsoft-azure-predictive-maintenance

Original download endpoints are encoded in `scripts/download_data.py`.

## Repository structure
```text
building-maintenance-analysis/
├── data/
│   ├── raw/
│   └── processed/
├── dashboard/
│   ├── README.md
│   └── power_bi_measures.dax
├── docs/
│   ├── POWER_BI_GUIDE_ID.md
│   └── SETUP_GUIDE_ID.md
├── excel/
│   └── maintenance_data_audit.xlsx
├── images/
├── notebooks/
│   └── exploratory_analysis.ipynb
├── scripts/
│   ├── download_data.py
│   ├── clean_data.py
│   └── run_eda.py
├── sql/
│   ├── 01_schema_postgresql.sql
│   ├── 02_load_postgresql.sql
│   └── 03_analysis_queries.sql
├── requirements.txt
└── README.md
```

## Cleaning workflow
The project checks missing values, exact duplicates, datetime parsing, data types, category consistency and referential integrity. Sensor outliers are inspected rather than automatically deleted. A maintenance record is classified as **Reactive** only when machine, timestamp and component exactly match a confirmed failure record; otherwise it is **Proactive**. This rule follows the source dataset's documented relationship rather than inventing a label.

## Analysis coverage
Python covers KPI summaries, maintenance mix, failure composition, top failure-prone assets, machine age vs failure frequency, monthly trends and recorded intervals between failures. SQL progresses from `JOIN`, `GROUP BY` and `CASE WHEN` to CTEs and window functions. Power BI is designed as three pages: **Executive Overview**, **Asset Performance**, and **Operational Signals**.

## KPI definitions
Available KPIs include Total Maintenance Events, Total Failure Events, Unique Assets, Reactive Maintenance Rate, Proactive Maintenance Rate, Failures per Asset and Mean Days Between Recorded Failures. The last metric is explicitly **not labeled MTBF** because machine operating hours are unavailable.

## Run locally
See `docs/SETUP_GUIDE_ID.md` for a Windows step-by-step guide. The short version is:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python scripts\download_data.py
python scripts\clean_data.py
python scripts\run_eda.py
jupyter notebook
```

## Power BI
The repository includes the data model, dashboard layout, DAX measures and a click-by-click build guide. The final `.pbix` must be saved from Power BI Desktop as `dashboard/maintenance_dashboard.pbix`, because PBIX is a proprietary Power BI Desktop binary.

## Skills demonstrated
**Excel · Python · Pandas · Matplotlib · PostgreSQL · SQL · Power BI · DAX · Data Cleaning · EDA · Data Modeling · Data Visualization · Business Analysis**

## Portfolio talking point
A key part of this project is analytical judgment: when desired KPIs are unsupported by the source, the analysis changes scope instead of manufacturing data. That makes the case study more defensible in interviews and closer to real analyst work.
