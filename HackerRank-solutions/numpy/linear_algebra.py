# problem link: https://www.hackerrank.com/challenges/np-linear-algebra/problem


# my solution:
import numpy as np

n = int(input())
a = []
for i in range(n):
    row = input().split()
    a.append([float(x) for x in row])

det = np.linalg.det(a)
print(round(det, 2))