# problem link: https://leetcode.com/problems/employees-earning-more-than-their-managers/


# my solution:

SELECT em.name AS Employee
FROM Employee em
JOIN Employee ma ON em.managerId = ma.id
WHERE em.salary > ma.salary;
