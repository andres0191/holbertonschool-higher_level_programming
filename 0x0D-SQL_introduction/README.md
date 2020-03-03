# SQL

- ** SQL: ** Structured Query Language is an open source database management software that helps users store, organize, and retrieve data. It is a very powerful program with a lot of flexibility—this tutorial will provide the simplest introduction to MySQL.

Some of the most inportant SQL Commands:
```
AND|OR - AND combines two or more conditions for a single query. 
ALTER TABLE - ALTER TABLE allows you to add or remove columns from a table
AS (alias) - AS allows you to rename a column or table to a more convenient alias (a correlation name) without changing the original names in the database.
ALTER DATABASE - modifies a database
BETWEEN - BETWEEN operator filters the results and returns only the ones that fit the specified range. You can describe the value of this operator using dates, numbers, or text.
CREATE DATABASE - When you need to create a new database, use the CREATE DATABASE statement. You must have admin rights to do that.
CREATE TABLE - creates a new table
CREATE INDEX - creates an index (search key)
CREATE VIEW
DELETE - deletes data from a database
DROP INDEX - deletes an index
DROP TABLE - deletes a table
GRANT - GRANT command is for giving users the access to a database.
REVOKE - REVOKE command is for taking away users' permisions.
COMMIT - COMMIT command is for saving every transaction to the database.
ROLLBACK - ROLLBACK command is for undoing transactions which are not saved to the database.
SAVEPOINT - SAVEPOINT command is for returning a transaction to a specific point without affecting the whole transaction.
DROP DATABASE - DROP DATABASE is one of the riskiest statements that should be used with extra caution. In SQL, drop means delete – and DROP DATABASE deletes the whole specified database together with all its parameters and data.
DROP INDEX - DROP INDEX will delete the index you specify. The syntax of this statement varies based on the DB system used.
DROP TABLE- DROP TABLE statement deletes the whole table with its column parameters and datatype settings. If you want to remove only the contents of the rows but keep the table itself, use another statement – TRUNCATE TABLE.
EXISTS - EXISTS operator allows you to check whether a record exists by writing a subquery. If the record is found, the result is displayed based on the statement you use this operator with. You can use it with SELECT, UPDATE, INSERT, and DELETE.
GROUP BY - Combine GROUP BY with SELECT statement in order to arrange identical data (rows with the same value) into groups (summarizing rows).
HAVING - HAVING specifies that you need to filter the results to only the rows that fulfill the described condition.

It performs the same action as the WHERE clause. The difference is that HAVING is used only for aggregate functions as WHERE doesn't work with them.
IN - The IN operator includes multiple values into the WHERE clause.
INSERT INTO - inserts new data into a database
INNER JOIN - INNER JOIN combines rows from different tables.
LEFT JOIN - LEFT JOIN retrieves records from the left table that match records in the right table. Some databases have a slightly different statement for this – LEFT OUTER JOIN.
RIGHT JOIN - RIGHT JOIN retrieves records from the right table that match records in the left table. Some databases call this statement differently – RIGHT OUTER JOIN.
FULL JOIN - FULL JOIN returns all the records that match either in left or right tables.
LIKE - Combine LIKE with the WHERE clause for finding specific patterns in columns.
ORDER BY - ORDER BY sets the order (ascending by default) of result records.
SELECT - SELECT is one of the main SQL statements. It selects data from a database and returns the table of results, called the result-set.
SELECT *  - SELECT used with an asterisk * operator selects all data records from a specified table.
SELECT DISTINCT - SELECT DISTINCT returns only the data that is distinct, and does not include duplicate entries.
SELECT INTO - SELECT INTO statement selects specified data in a table and copies it to another table.
SELECT TOP - SELECT TOP specifies the maximum number or percentage of data entries to return in a result-set.
TRUNCATE TABLE - TRUNCATE TABLE removes data entries from a table in a database, but keeps the table, its datatype and column parameters.
UNION - You can combine multiple result-sets using the UNION operator with two or more SELECT statements.
UNION ALL - UNION ALL is used to combine two or more result-sets and keep all the duplicate data entries.
UPDATE - UPDATE statement is used with the WHERE clause to update data in the table.
WHERE - WHERE clause specifies your query to filter only the results that satisfy your set condition.

WHERE doesn't work with the aggregate functions, for that purpose, use HAVING instead.
```
More info [link] (https://www.bitdegree.org/learn/sql-commands-list#andor)
