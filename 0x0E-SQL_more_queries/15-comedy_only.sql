-- mport the database dump from hbtn_0d_tvshows to your MySQL server:

SELECT TV.title
FROM tv_shows AS TV
    INNER JOIN tv_show_genres AS S
    ON TV.id = S.show_id

    INNER JOIN tv_genres AS G
    ON G.id = S.genre_id
    WHERE G.name = "Comedy"

ORDER BY TV.title;