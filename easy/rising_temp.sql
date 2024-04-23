/*
You have Weather column with
id int
recordDate date
temperature int

Write a solution to find all Id with higher temperature compared to its 
previous dates(yesterday)
*/

SELECT w.id
FROM Weather w 
JOIN Weather w_prev on w.recordDate = DATE_ADD(w_prev.recordDate, INTERVAL 1 DAY)
WHERE w.temperature > w_prev.temperature;
