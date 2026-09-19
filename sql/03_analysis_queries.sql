-- 1. Basic aggregation: maintenance by machine model
SELECT m.model,
       COUNT(*) AS total_maintenance,
       SUM(CASE WHEN mt.maintenance_type = 'Reactive' THEN 1 ELSE 0 END) AS reactive_events,
       ROUND(100.0 * SUM(CASE WHEN mt.maintenance_type = 'Reactive' THEN 1 ELSE 0 END) / COUNT(*), 2) AS reactive_pct
FROM maintenance mt
JOIN machines m ON m.machine_id = mt.machine_id
GROUP BY m.model
ORDER BY total_maintenance DESC;

-- 2. Failure frequency by component
SELECT component, COUNT(*) AS failure_events
FROM failures
GROUP BY component
ORDER BY failure_events DESC;

-- 3. Top 10 failure-prone assets
SELECT m.machine_id, m.model, m.age, COUNT(f.machine_id) AS failure_events
FROM machines m
LEFT JOIN failures f ON f.machine_id = m.machine_id
GROUP BY m.machine_id, m.model, m.age
ORDER BY failure_events DESC, m.machine_id
LIMIT 10;

-- 4. Monthly maintenance vs failure trend
WITH maint_month AS (
    SELECT month, COUNT(*) AS maintenance_events
    FROM maintenance GROUP BY month
), fail_month AS (
    SELECT month, COUNT(*) AS failure_events
    FROM failures GROUP BY month
)
SELECT COALESCE(m.month, f.month) AS month,
       COALESCE(m.maintenance_events, 0) AS maintenance_events,
       COALESCE(f.failure_events, 0) AS failure_events
FROM maint_month m
FULL OUTER JOIN fail_month f ON f.month = m.month
ORDER BY month;

-- 5. Asset operational burden analysis
WITH failure_summary AS (
    SELECT
        machine_id,
        COUNT(*) AS failure_events,
        COUNT(DISTINCT datetime) AS failure_incidents
    FROM failures
    GROUP BY machine_id
),

error_summary AS (
    SELECT
        machine_id,
        COUNT(*) AS error_events
    FROM errors
    GROUP BY machine_id
),

maintenance_summary AS (
    SELECT
        machine_id,
        COUNT(*) AS maintenance_events
    FROM maintenance
    GROUP BY machine_id
),

asset_events AS (
    SELECT
        m.machine_id,
        m.model,
        m.age,
        COALESCE(f.failure_events, 0) AS failure_events,
        COALESCE(f.failure_incidents, 0) AS failure_incidents,
        COALESCE(e.error_events, 0) AS error_events,
        COALESCE(mt.maintenance_events, 0) AS maintenance_events
    FROM machines m

    LEFT JOIN failure_summary f
        ON f.machine_id = m.machine_id

    LEFT JOIN error_summary e
        ON e.machine_id = m.machine_id

    LEFT JOIN maintenance_summary mt
        ON mt.machine_id = m.machine_id
),

ranked AS (
    SELECT
        *,
        DENSE_RANK() OVER (
            ORDER BY failure_events DESC
        ) AS failure_rank,

        DENSE_RANK() OVER (
            ORDER BY error_events DESC
        ) AS error_rank,

        DENSE_RANK() OVER (
            ORDER BY maintenance_events DESC
        ) AS maintenance_rank
    FROM asset_events
)

SELECT *
FROM ranked
ORDER BY
    failure_rank,
    error_rank,
    maintenance_rank,
    machine_id;

-- test 5
SELECT
    machine_id,
    COUNT(*) AS total_rows,
    COUNT(DISTINCT datetime) AS distinct_failure_times
FROM failures
WHERE machine_id IN (17, 22, 98, 99)
GROUP BY machine_id
ORDER BY machine_id;

-- 6. Window function: recorded interval between failures
WITH ordered_failures AS (
    SELECT machine_id, datetime,
           LAG(datetime) OVER (PARTITION BY machine_id ORDER BY datetime) AS previous_failure
    FROM failures
)
SELECT machine_id,
       ROUND(AVG(EXTRACT(EPOCH FROM (datetime - previous_failure)) / 86400.0)::numeric, 2) AS mean_days_between_recorded_failures
FROM ordered_failures
WHERE previous_failure IS NOT NULL
GROUP BY machine_id
ORDER BY mean_days_between_recorded_failures;

-- 7. Window ranking: machines within each model
WITH counts AS (
    SELECT m.machine_id, m.model, COUNT(f.machine_id) AS failure_events
    FROM machines m
    LEFT JOIN failures f ON f.machine_id = m.machine_id
    GROUP BY m.machine_id, m.model
)
SELECT *, DENSE_RANK() OVER (PARTITION BY model ORDER BY failure_events DESC) AS failure_rank_in_model
FROM counts
ORDER BY model, failure_rank_in_model, machine_id;

-- 8. Operational telemetry by model
SELECT m.model,
       ROUND(AVG(t.volt)::numeric, 2) AS avg_volt,
       ROUND(AVG(t.rotate)::numeric, 2) AS avg_rotate,
       ROUND(AVG(t.pressure)::numeric, 2) AS avg_pressure,
       ROUND(AVG(t.vibration)::numeric, 2) AS avg_vibration
FROM telemetry t
JOIN machines m ON m.machine_id = t.machine_id
GROUP BY m.model
ORDER BY m.model;

