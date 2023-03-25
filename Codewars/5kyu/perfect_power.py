# Problem Link: https://www.codewars.com/kata/54d4c8b08776e4ad92000835

# My Solution:
import math

def isPP(n):
    if n < 2:
        return None
    for b in range(2, int(math.log2(n))+1):
        a = int(round(n ** (1/b)))
        if a ** b == n:
            return [a, b]
    return None
    