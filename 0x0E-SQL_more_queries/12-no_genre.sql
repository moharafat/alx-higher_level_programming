-- Import the database dump from hbtn_0d_tvshows to your MySQL server:

SELECT TV.title, G.genre_id
FROM tv_shows AS TV
    LEFT JOIN tv_show_genres AS G
    ON TV.id = G.show_id
    WHERE G.genre_id IS NULL
ORDER BY TV.title, G.genre_id;