-- script that displays the max temperature of each 
-- state (ordered by State name).
FROM temperatures GROUP BY state ORDER BY state ASC;