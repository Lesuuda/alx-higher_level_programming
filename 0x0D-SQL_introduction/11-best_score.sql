-- lists all records of score above 10 in descending order
SELECT `score`, `name` FROM `second_table`
WHERE `score` >= 10 ORDER BY `score` DESC;
