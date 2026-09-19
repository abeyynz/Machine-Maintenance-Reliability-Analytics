# Power BI Dashboard

This folder contains the final Power BI dashboard developed for the Machine Maintenance & Reliability Analytics project.

## Files

- `maintenance_dashboard.pbix` — final interactive Power BI report.
- `power_bi_measures.dax` — documentation of the DAX measures used in the analysis.

## Data Model

The dashboard uses a dimensional data model connecting machine, date, and component dimensions with operational fact tables.

### Dimension Tables

- **Machines** — machine ID, model, and age.
- **DateTable** — date, month, quarter, year, and year-month attributes.
- **Components** — shared component dimension for consistent filtering across failure and maintenance data.

### Fact Tables

- **Telemetry** — voltage, rotation, pressure, and vibration sensor readings.
- **Failures** — recorded component failure incidents.
- **Maintenance** — proactive and reactive maintenance activities.
- **Errors** — recorded machine error events.

Relationships are primarily configured as one-to-many relationships with single-direction filtering from dimensions to fact tables.

## Dashboard Pages

### 1. Overview

Provides a high-level view of machine reliability and maintenance activity.

Key elements include:

- Total Assets
- Failure Incidents
- Total Maintenance
- Asset Failure %
- Monthly failure trend
- Proactive vs reactive maintenance
- Failures by component
- Failures by machine model
- Average voltage, rotation, pressure, and vibration

### 2. Machine Health & Telemetry

Provides machine-level investigation of equipment condition and sensor behavior.

Key elements include:

- Machine ID filtering
- Failure incidents by component
- Failure incidents by machine model
- Vibration trend
- Pressure trend
- Rotation trend
- Voltage trend
- Machine-level health and maintenance detail table

### 3. Maintenance & Reliability

Focuses on maintenance strategy and reliability patterns.

Key elements include:

- Total Maintenance
- Proactive Maintenance
- Reactive Maintenance
- Reactive Maintenance %
- Maintenance trend
- Maintenance by component
- Reactive Maintenance % by component
- Failure vs maintenance trend
- Maintenance strategy by component

## Key DAX Measures

The dashboard includes measures for:

- Failure and maintenance KPIs
- Asset failure exposure
- Proactive and reactive maintenance
- Failure-to-maintenance ratio
- Machine age and failure correlation
- Monthly maintenance and failure correlation
- Average telemetry measurements
- Telemetry record coverage

See [`power_bi_measures.dax`](power_bi_measures.dax) for the documented DAX measures.

## Data Coverage Note

January 2016 contains only 700 telemetry records, compared with approximately 67,200–74,400 records in full months during 2015. January 2016 telemetry values should therefore not be interpreted as directly comparable full-month trends.

For the complete analytical workflow, findings, recommendations, and data limitations, see the [main project README](../README.md).