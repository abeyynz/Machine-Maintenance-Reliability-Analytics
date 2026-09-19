# Machine Maintenance & Reliability Analytics

Power BI analytics project exploring machine failures, maintenance strategies, equipment health, and telemetry patterns to support reliability analysis and maintenance decision-making.

### Project Highlights

**100 Machines** · **761 Failure Incidents** · **3,286 Maintenance Records** · **98% Assets with Recorded Failure**

`Power BI` `Power Query` `DAX` `Data Modeling` `Reliability Analytics`

## Project Overview

This project analyzes machine maintenance, failure, and telemetry data to explore equipment reliability and maintenance patterns. The analysis was developed in Power BI using a relational data model connecting machine, maintenance, failure, error, telemetry, date, and component data.

The dashboard provides three analytical views: an operational overview of machine failures and maintenance activities, machine-level health and telemetry analysis, and a deeper assessment of maintenance strategy and reliability patterns.

Beyond dashboard development, the project includes dimensional data modeling, DAX-based KPI development, exploratory analysis, correlation analysis, and data-quality validation to ensure that observed patterns are interpreted appropriately.

## Business Questions

This project was designed to answer the following analytical questions:

- Which machine components and models record the highest number of failure incidents?
- How are maintenance activities distributed between proactive and reactive maintenance?
- Which components show higher reliance on reactive maintenance?
- Is machine age associated with higher failure frequency?
- How do failure incidents and maintenance activities change over time?
- Which components should be prioritized for further reliability investigation?
- Are there data coverage or quality issues that could affect the interpretation of telemetry trends?

## Dataset

This project uses the **Microsoft Azure Predictive Maintenance** dataset available on Kaggle.

The dataset contains operational data from a fleet of machines and is organized into multiple related tables:

- **Machines** — machine ID, model, and age.
- **Telemetry** — hourly sensor readings including voltage, rotation, pressure, and vibration.
- **Failures** — recorded component failure events for each machine.
- **Maintenance** — component replacement and maintenance records.
- **Errors** — machine error events recorded during operation.

The dataset structure enables machine-level, component-level, and time-based analysis by connecting operational telemetry with maintenance and failure history.

**Dataset Source:** [Microsoft Azure Predictive Maintenance — Kaggle](https://www.kaggle.com/datasets/arnabbiswas1/microsoft-azure-predictive-maintenance)

## Data Model

The Power BI data model was structured using dimension and fact-style tables to support consistent filtering and analysis across failures, maintenance, telemetry, and machine information.

### Dimension Tables
- **Machines** - machine identifier, model, and machine age.
- **DateTable** - calendar dimension containing date, month, quarter, year, and year-month attributes.
- **Components** - shared component dimension used to consistently filter both failure and maintenance records.

### Fact Tables
- **Telemetry** - time-series sensor readings including voltage, rotation, pressure, and vibration.
- **Failures** - recorded machine failure events by component.
- **Maintenance** - maintenance activities by machine, component, and maintenance type.
- **Errors** - recorded machine error events.

A dedicated **_Measures** table was also used to organize DAX measures separately from the source tables.

Relationships were configured primarily as one-to-many relationships from the dimension tables to the corresponding fact tables with single-direction filtering.

## Data Preparation

Data preparation and transformation were performed in Power Query and the Power BI data model before visualization.

Key preparation steps included:

- Reviewed the structure and data types of the machine, telemetry, failure, maintenance, and error datasets.
- Standardized date fields to support consistent time-based analysis across multiple tables.
- Created a dedicated **DateTable** containing year, quarter, month, and year-month attributes for time-series analysis.
- Created a shared **Components** dimension to provide consistent component-level filtering across the Failures and Maintenance tables.
- Established one-to-many relationships between dimension and fact tables using machine ID, date, and component keys.
- Created a dedicated **_Measures** table to organize calculated KPIs and analytical measures.
- Validated record coverage before interpreting time-series patterns, including identifying January 2016 as a partial telemetry period.

## DAX Measures

DAX measures were developed to calculate operational KPIs and support deeper reliability analysis.

Key measures include:

- **Total Assets** : number of machines included in the analysis.
- **Failure Incidents** : total recorded failure events.
- **Machines with Failure** : distinct machines with at least one recorded failure.
- **Asset Failure %** : percentage of machines that experienced at least one failure.
- **Total Maintenance** : total recorded maintenance activities.
- **Proactive Maintenance** : maintenance activities classified as proactive.
- **Reactive Maintenance** : maintenance activities classified as reactive.
- **Reactive Maintenance %** : proportion of maintenance activities classified as reactive.
- **Failure per Maintenance** : descriptive ratio of failure incidents to maintenance activities.
- **Age-Failure Correlation** : Pearson correlation between machine age and failure frequency.
- **Maintenance-Failure Correlation** : Pearson correlation between monthly maintenance activity and failure incidents.
- **Avg Voltage, Avg Rotation, Avg Pressure, Avg Vibration** : fleet-level average telemetry measures.
- **Telemetry Records** : record count used to validate telemetry data coverage.

## Dashboard

The dashboard consists of three analytical pages, each designed to address a different aspect of machine reliability and maintenance performance.

### 1. Overview

Provides a high-level view of asset reliability and maintenance activity, including total assets, failure incidents, maintenance volume, asset failure exposure, failure trends, component-level failures, machine model comparisons, and maintenance composition.

![Overview Dashboard](images/dashboard-overview.png)

### 2. Machine Health & Telemetry

Focuses on machine-level condition and sensor behavior. The page combines failure information with voltage, rotation, pressure, and vibration telemetry, supported by a detailed machine-level table for further investigation.

![Machine Health Dashboard](images/dashboard-machine-health.png)

### 3. Maintenance & Reliability

Analyzes maintenance strategy and reliability patterns, including proactive and reactive maintenance, component-level maintenance activity, reactive maintenance rates, and the relationship between maintenance activity and failure incidents.

![Maintenance & Reliability Dashboard](images/dashboard-maintenance-reliability.png)

## Key Findings

- **Failure exposure is widespread.** 98 out of 100 machines (98%) recorded at least one failure during the observed period.

- **Component 2 shows the strongest reliability concern.** It recorded 259 failure incidents (34.0% of all failures), the highest reactive maintenance rate at 30%, and the highest failure-to-maintenance ratio at 30.01%.

- **Maintenance activities are predominantly proactive.** Of 3,286 maintenance records, 2,543 (77.39%) were proactive, while 743 (22.61%) were reactive.

- **Failure activity peaked in January 2015.** January recorded 94 failure incidents, followed by a decline in February to 50. From March to December, monthly failures remained relatively stable at 58–69 incidents.

- **Machine age has a moderate positive association with failure frequency.** The Pearson correlation between machine age and failure incidents was 0.48, indicating that older machines tended to record more failures, although age alone does not explain failure behavior.

- **Maintenance activity and failures showed a weak-to-moderate negative association in 2015.** The monthly Pearson correlation was -0.36. This relationship is descriptive and should not be interpreted as evidence that maintenance activity directly caused the reduction in failures.

- **January 2016 telemetry has incomplete coverage.** Only 700 telemetry records were available compared with approximately 67,200–74,400 records in full months during 2015. January 2016 telemetry changes should therefore not be interpreted as directly comparable full-month trends.

## Recommendations

Based on the analysis, the following actions could support further reliability and maintenance improvement:

- **Prioritize Component 2 for further reliability investigation.** Review its recurring failure modes, maintenance history, and maintenance intervals because it recorded the highest failure count, reactive maintenance rate, and failure-to-maintenance ratio.

- **Incorporate machine age into maintenance prioritization.** Machine age can be considered alongside failure history, component condition, and telemetry indicators when identifying assets that may require closer monitoring.

- **Continue monitoring the balance between proactive and reactive maintenance.** Although proactive maintenance represents 77.39% of maintenance activity, reactive maintenance still accounts for 22.61% and varies across components.

- **Investigate recurring failure patterns at the machine level.** Machines with repeated failure incidents can be reviewed individually to identify recurring component issues and determine whether maintenance schedules require adjustment.

- **Improve telemetry data completeness and coverage validation.** Partial periods should be flagged or excluded from full-month comparisons to prevent incomplete data from being interpreted as operational changes.

## Data Limitations

Several limitations should be considered when interpreting the results:

- **January 2016 contains partial telemetry data.** Only 700 telemetry records are available, substantially fewer than the approximately 67,200–74,400 records observed in full months during 2015. Therefore, January 2016 telemetry values should not be directly compared with full-month periods.

- **Correlation does not imply causation.** The relationships between machine age and failures, as well as maintenance activity and failures, describe statistical associations only and do not establish causal effects.

- **Failure counts do not represent failure severity.** Each recorded failure is treated as an incident, while information such as downtime, repair cost, operational impact, and failure severity is not included in the analysis.

- **Maintenance volume does not directly measure maintenance effectiveness.** The failure-to-maintenance ratio is used as a descriptive indicator and should not be interpreted as a direct measure of maintenance performance.

- **Telemetry is analyzed primarily at an aggregate level.** Additional machine-level thresholds, anomaly detection, or failure-window analysis would be required to determine whether specific sensor patterns precede individual failures.

## Tools & Technologies

- **Power BI Desktop** — dashboard development and interactive data visualization
- **Power Query** — data preparation and transformation
- **DAX** — KPI development, analytical measures, and correlation analysis
- **Data Modeling** — dimensional modeling and relationship design
- **GitHub** — project documentation and version control
