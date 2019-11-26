-- Comments:
-- Script that lists all records of the table second_table
SELECT DISTINCT state, value as max_temp FROM temperatures ORDER BY max_temp DESC LIMIT 3;
