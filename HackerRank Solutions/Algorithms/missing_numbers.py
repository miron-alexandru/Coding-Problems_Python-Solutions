# Problem Link: https://www.hackerrank.com/challenges/missing-numbers/problem


# My Solution:
from collections import Counter


def missingNumbers(arr, brr):
    return sorted((Counter(brr) - Counter(arr)).keys())
