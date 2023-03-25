# Problem Link: https://www.hackerrank.com/challenges/weather-observation-station-15/problem


# Solution:
SELECT ROUND(LONG_W, 4)
FROM STATION
WHERE LAT_N < 137.2345
ORDER BY LAT_N DESC
LIMIT 1;
