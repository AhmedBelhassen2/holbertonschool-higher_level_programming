-- lists all the cities of California that can be found
SELECT id, name FROM cities WHERE cities.state_id = 1 ORDER BY cities.id ASC;
