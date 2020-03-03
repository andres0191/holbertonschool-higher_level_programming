-- script that lists all cities contained in the database hbtn_0d_usa

-- The INNER JOIN keyword selects all rows from both tables as long as
-- there is a match between the columns. If there are records in the "Orders"
-- table that do not have matches in "Customers", these orders will not be shown!
-- https://www.w3schools.com/sql/sql_join_inner.asp
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.states_id = states.id ORDER BY cities.id ASC;