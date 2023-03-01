# Problem Link: https://www.hackerrank.com/challenges/compress-the-string/problem


# My Solution:

from itertools import groupby

s = str(input())

for c, group in groupby(s):
    print(f"({len(list(group))}, {c})", end=" ")
