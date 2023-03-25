# Problem Link: https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem


# My Solution:
import numpy as np
np.set_printoptions(legacy='1.13')

a = input()

arr = np.fromstring(a, sep=' ')
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))