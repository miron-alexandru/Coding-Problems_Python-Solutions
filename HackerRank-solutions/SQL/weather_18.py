# Problem Link: https://www.hackerrank.com/challenges/weather-observation-station-18/problem

# My Solution:
SELECT ROUND(ABS(MIN(lat_n) - MAX(lat_n)) + ABS(MIN(long_w) - MAX(long_w)), 4) AS distance
FROM station;
