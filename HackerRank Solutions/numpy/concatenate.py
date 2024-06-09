# Problem Link: https://www.hackerrank.com/challenges/np-concatenate/problem


# My Solution:
import numpy as np

n, m, p = map(int, input().split())

a = np.zeros((n, p), dtype=np.int)
for i in range(n):
    a[i] = np.fromstring(input(), sep=" ")

b = np.zeros((m, p), dtype=np.int)
for i in range(m):
    b[i] = np.fromstring(input(), sep=" ")

c = np.concatenate((a, b), axis=0)

print(c)
