-- Comments:
-- Script that lists all databases of your MySQL server
SELECT id, name FROM cities WHERE state_id IN (SELECT id FROM states WHERE id = 1);