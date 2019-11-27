-- Comments:
-- Script that lists all databases of your MySQL server
SELECT cities.id AS id, cities.name AS name, states.name AS name
FROM states, cities
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;