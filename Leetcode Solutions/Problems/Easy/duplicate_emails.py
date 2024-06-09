# problem link: https://leetcode.com/problems/duplicate-emails/


# my solution:

SELECT email FROM Person
GROUP BY email
HAVING COUNT(*) > 1;
