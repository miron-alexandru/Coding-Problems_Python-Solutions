# Problem Link: https://www.hackerrank.com/challenges/african-cities

# Solution:
SELECT CITY.Name
FROM CITY
JOIN COUNTRY ON CITY.CountryCode = COUNTRY.Code
WHERE COUNTRY.Continent = 'Africa';
