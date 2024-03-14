-- import the database dump from hbtn_0d_tvshows to your MySQL server:

SELECT TV.title, G.name
FROM tv_shows AS TV
    LEFT JOIN tv_show_genres AS S
    ON TV.id = S.show_id

    LEFT JOIN tv_genres AS G
    ON S.genre_id = G.id


ORDER BY TV.title, G.name;