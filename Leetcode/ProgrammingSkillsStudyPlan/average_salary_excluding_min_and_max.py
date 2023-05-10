# problem link: https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary


# my solutions:
class Solution:
    def average(self, salary: List[int]) -> float:
        # init min and max salary
        min_salary = min(salary)
        max_salary = max(salary)
        # calculate total salary without min and maxt salary
        total = sum(salary) - min_salary - max_salary
        # calculate the average salary
        return round(total / (len(salary) - 2), 5)


# 2
class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = min(salary)
        max_salary = max(salary)
        total = 0
        for i in salary:
            total += i
        average = (total - min_salary - max_salary) / (len(salary) - 2)
        return round(average, 5)
