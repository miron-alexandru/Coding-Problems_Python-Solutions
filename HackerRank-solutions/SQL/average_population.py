# Problem Link: https://www.hackerrank.com/challenges/average-population-of-each-continent/problem

# Solution:
SELECT COUNTRY.Continent, FLOOR(AVG(CITY.Population))
FROM CITY
JOIN COUNTRY ON CITY.CountryCode = COUNTRY.Code
GROUP BY COUNTRY.Continent;
