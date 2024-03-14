-- Import the database dump from hbtn_0d_tvshows

SELECT G.name
FROM tv_genres AS G
    INNER JOIN tv_shows AS TV
    ON S.show_id = TV.id
    WHERE TV.title = "Dexter"
    INNER JOIN tv_show_genres AS S
    ON G.id = S.genre_id


ORDER BY G.name;