-- Comments:
-- Script that lists all records of the table second_table
SELECT DISTINCT state, MAX(value) as max_temp FROM temperatures GROUP BY state ORDER BY state ASC;
