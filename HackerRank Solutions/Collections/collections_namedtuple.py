# Problem link: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem


# My solution:

from collections import namedtuple


n = int(input().strip())
columns = input().strip().split()
Student = namedtuple("Student", " ".join(columns))
students = [Student(*input().strip().split()) for _ in range(n)]
average = sum(float(getattr(student, "MARKS")) for student in students) / n

print("{:.2f}".format(average))
