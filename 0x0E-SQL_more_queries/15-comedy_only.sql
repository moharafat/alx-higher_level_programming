-- mport the database dump from hbtn_0d_tvshows to your MySQL server:

SELECT TV.title
FROM tv_shows AS TV
    INNER JOIN tv_show_genres AS S
    ON G.id = S.genre_id

    INNER JOIN tv_shows AS TV
    ON S.show_id = TV.id
    WHERE TV.title = "Dexter"

ORDER BY TV.title;