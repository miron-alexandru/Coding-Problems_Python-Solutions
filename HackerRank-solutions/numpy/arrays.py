# Problem Link: https://www.hackerrank.com/challenges/np-arrays/problem


# My solution: 
import numpy

def arrays(arr):
    arr = numpy.array(arr, float).flip
    res = numpy.flip(arr)
    return res
    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)