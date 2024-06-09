# Problem Link: https://www.hackerrank.com/challenges/draw-the-triangle-2/problem


# My Solution:
SET @num:=0; 
SELECT REPEAT('* ', @num:= @num + 1) 
FROM INFORMATION_SCHEMA.TABLES
WHERE @num < 20;