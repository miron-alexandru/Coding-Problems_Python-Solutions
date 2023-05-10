# Problem Link: https://www.hackerrank.com/challenges/one-week-preparation-kit-lonely-integer/problem


# My Solution:
from collections import Counter


def lonelyinteger(a):
    counts = Counter(a)
    for i in counts:
        if counts[i] == 1:
            return i
