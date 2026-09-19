SELECT 'machines' AS table_name, COUNT(*) AS total_rows
FROM machines

UNION ALL

SELECT 'maintenance', COUNT(*)
FROM maintenance

UNION ALL

SELECT 'failures', COUNT(*)
FROM failures

UNION ALL

SELECT 'errors', COUNT(*)
FROM errors

UNION ALL

SELECT 'telemetry', COUNT(*)
FROM telemetry;