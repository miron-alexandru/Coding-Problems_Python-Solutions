# Problem Link: https://www.hackerrank.com/challenges/np-dot-and-cross/problem


# My Solution:
import numpy as np

n = int(input())

a = np.zeros((n, n), dtype=int)
for i in range(n):
    a[i] = np.fromstring(input(), dtype=int, sep=' ')

b = np.zeros((n, n), dtype=int)
for i in range(n):
    b[i] = np.fromstring(input(), dtype=int, sep=' ')
    
print(np.dot(a, b))
