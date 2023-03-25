# Problem Link: https://www.hackerrank.com/challenges/np-zeros-and-ones/problem


# My Solution:
import numpy as np

n = tuple(map(int, input().split()))

print(np.zeros(n, dtype=np.int))
print(np.ones(n, dtype=np.int))
