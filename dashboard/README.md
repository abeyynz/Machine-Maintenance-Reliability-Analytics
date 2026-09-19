# Power BI dashboard build

A `.pbix` file is not included because PBIX is a proprietary Power BI Desktop binary and cannot be reliably generated outside Power BI Desktop. Everything needed to build it is included here.

## Import these processed CSVs
- `machines_clean.csv`
- `maintenance_clean.csv`
- `failures_clean.csv`
- `errors_clean.csv`
- `telemetry_clean.csv`

## Relationships
Create one-to-many relationships from `machines[machineID]` to the `machineID` column in each event table. Use single-direction filtering from `machines` to events.

## Measures
Copy the measures from `power_bi_measures.dax`.

## Pages
1. **Executive Overview**: KPI cards (Total Maintenance, Total Failures, Unique Assets, Reactive Rate, Proactive Rate), monthly maintenance/failure line chart, failures by model bar chart.
2. **Asset Performance**: top assets by failures, model/component matrix, age-vs-failures scatter, slicers for model and machineID.
3. **Operational Signals**: telemetry trend, errors by errorID, machine-level table combining errors/failures/maintenance.

Use `docs/POWER_BI_GUIDE_ID.md` for exact click-by-click instructions.
