# Problem Link: https://www.hackerrank.com/challenges/grading/problem


# My Solution:
import math


def gradingStudents(grades):
    rounded_grades = []
    for grade in grades:
        if grade < 38:
            rounded_grades.append(grade)
        elif grade % 5 > 2:
            rounded_grades.append(math.ceil(grade/5)*5)
        else:
            rounded_grades.append(grade)
    return rounded_grades