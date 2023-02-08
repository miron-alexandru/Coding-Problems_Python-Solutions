# Problem Link: https://www.hackerrank.com/challenges/np-shape-reshape/problem


# My solution: 
import numpy as np

nums = list(map(int, input().split()))
arr = np.array(nums)
print(np.reshape(arr, (3, 3)))
