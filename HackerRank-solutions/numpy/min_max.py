# Problem Link: https://www.hackerrank.com/challenges/np-min-and-max/problem


# My Solution:
import numpy as np

n, m = map(int, input().split())

matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

print(np.max(np.min(matrix, axis=1)))
