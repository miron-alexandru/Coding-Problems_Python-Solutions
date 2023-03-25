# Problem Link: https://www.hackerrank.com/challenges/weather-observation-station-19/problem

# My Solution:
# Euclidean distance formula
sqrt((x1 - x2)^2 + (y1 - y2)^2)

# Query
SELECT ROUND(SQRT(POW(MAX(lat_n) - MIN(lat_n), 2) + POW(MAX(long_w) - MIN(long_w), 2)), 4) AS distance
FROM station;
