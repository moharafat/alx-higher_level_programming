-- Import the database dump from hbtn_0d_tvshows

SELECT TV.title, G.genre_id
FROM tv_shows AS TV
    INNER JOIN tv_show_genres AS G
    ON TV.id = G.show_id
ORDER BY TV.title, G.genre_id;