-- Comments:
-- Script that lists all databases of your MySQL server
SELECT cities.id AS id, cities.name AS name, states.name AS name
FROM hbtn_0d_usa.states
INNER JOIN cities;
