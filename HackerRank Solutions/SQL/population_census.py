# Problem Link: https://www.hackerrank.com/challenges/asian-population/problem


# My Solution:
SELECT SUM(CITY.Population)
FROM CITY
JOIN COUNTRY ON CITY.CountryCode = COUNTRY.Code
WHERE COUNTRY.Continent = 'Asia';