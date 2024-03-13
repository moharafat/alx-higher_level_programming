-- Import the database dump from hbtn_0d_tvshows to your MySQL server

SELECT G.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres AS G
    INNER JOIN tv_show_genres AS TV
    ON G.id = TV.genre_id
    GROUP BY G.name
ORDER BY number_of_shows DESC;