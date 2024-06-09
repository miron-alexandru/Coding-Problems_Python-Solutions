# Problem Link: https://www.hackerrank.com/challenges/np-sum-and-prod/problem


# My Solution:
import numpy as np

n, m = map(int, input().split())

matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

print(np.product(np.sum(matrix, axis=0)))
