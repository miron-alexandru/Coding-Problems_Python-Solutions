# Problem Link: https://www.hackerrank.com/challenges/np-inner-and-outer/problem


# My Solution:
import numpy as np

a = np.fromstring(input(), dtype=int, sep=" ")
b = np.fromstring(input(), dtype=int, sep=" ")


print(np.inner(a, b))
print(np.outer(a, b))
