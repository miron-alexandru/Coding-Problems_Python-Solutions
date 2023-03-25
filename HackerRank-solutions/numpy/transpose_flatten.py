# Problem Link: https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem


# My Solution:
import numpy as np

n, m = map(int, input().split())

a = np.zeros((n, m), dtype=int)
for i in range(n):
    a[i] = np.fromstring(input(), sep=' ')

print(np.transpose(a))
print(a.flatten())