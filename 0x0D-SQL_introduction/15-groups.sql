--  lists the number of records with the same score in the table second_table

SELECT score, count(*) AS number
FROM second_table ORDER BY number DESC;