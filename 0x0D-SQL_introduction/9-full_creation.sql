-- creates a table second_table in the database hbtn_0c_0
-- and add multiples rows.

CREATE TABLE IF NOT EXISTS second_table (
    id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    score INT NOT NULL
    );

insert into second_table VALUES
(1, "John", 10),
(2, "Alex", 3),
(3, "Bob", 14),
(4, "George", 8);