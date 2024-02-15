-- Selects the 'name' column from the 'tv_genres' table
SELECT name
-- Joins the 'tv_genres' table with the 'tv_show_genres' table using a LEFT JOIN
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- Joins the result with the 'tv_shows' table using another LEFT JOIN
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
-- Filters the result to only include rows where the show title is 'Dexter'
WHERE tv_shows.title = 'Dexter'
-- Groups the result by the 'name' column (genres)
GROUP BY name
-- Orders the result in ascending order based on the 'name' column
ORDER BY name ASC;

