# Problem Link: https://www.hackerrank.com/challenges/np-mean-var-and-std/problem


# My Solution:
import numpy as np

n, m = map(int, input().split())

matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

print(np.mean(matrix, axis=1))
print(np.var(matrix, axis=0))
print(np.round(np.std(matrix), 11))
