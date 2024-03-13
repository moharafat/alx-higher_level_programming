-- Import the database dump of hbtn_0d_tvshows

SELECT TV.title, G.genre_id
FROM tv_shows AS TV
    LEFT JOIN tv_show_genres AS G
    ON TV.id = G.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;