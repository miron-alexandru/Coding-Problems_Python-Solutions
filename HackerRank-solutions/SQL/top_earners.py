# Problem Link: https://www.hackerrank.com/challenges/earnings-of-employees


# Solution:
SELECT 
    MAX(MONTHS*SALARY) AS MAX_TOTAL_EARNINGS,
    COUNT(*) AS EMPLOYEES_WITH_MAX_EARNINGS
FROM EMPLOYEE
WHERE MONTHS*SALARY = (
    SELECT MAX(MONTHS*SALARY) FROM EMPLOYEE
);
