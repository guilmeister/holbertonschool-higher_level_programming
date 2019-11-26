-- Comments:
-- Script that lists all records of the table second_table
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
