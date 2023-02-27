# Problem Link: https://www.hackerrank.com/challenges/draw-the-triangle-1/problem


# My Solution:
SET @num:=21; 
SELECT REPEAT('* ', @num:= @num - 1) 
FROM INFORMATION_SCHEMA.TABLES
WHERE @num > 0
ORDER BY @num DESC;
