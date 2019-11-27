-- Comments:
-- Script that lists all databases of your MySQL server
SELECT tv_genres.name AS name FROM tv_show_genres
INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
INNER JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_shows.title = 'Dexter'
ORDER BY name ASC;