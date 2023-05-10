# Problem Link: https://www.hackerrank.com/challenges/np-array-mathematics/problem


# My Solution:
import numpy as np

n, m = map(int, input().split())

a = np.zeros((n, m), dtype=int)
for i in range(n):
    a[i] = np.fromstring(input(), dtype=int, sep=" ")

b = np.zeros((n, m), dtype=int)
for i in range(n):
    b[i] = np.fromstring(input(), dtype=int, sep=" ")


print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a**b)
