-- Import the database dump from hbtn_0d_tvshows

SELECT G.name
FROM tv_genres AS G


    INNER JOIN tv_shows AS TV
    ON S.show_id = TV.id
    WHERE TV.title = "Dexter"

ORDER BY G.name;