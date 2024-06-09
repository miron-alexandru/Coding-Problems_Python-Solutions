# Problem Link: https://www.hackerrank.com/challenges/weather-observation-station-20/problem


# Solution:
SELECT ROUND(st.lat_n, 4)
FROM station AS st
WHERE (SELECT COUNT(lat_n) FROM station WHERE lat_n < st.lat_n) = (SELECT COUNT(lat_n) FROM station WHERE lat_n > st.lat_n);