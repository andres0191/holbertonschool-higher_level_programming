-- script that lists all cities contained in the database hbtn_0d_usa
-- https://www.w3schools.com/sql/sql_join_inner.asp

SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id;