-- SQL script that lists all records of the table second_table
-- of the database in my MySQL server
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
