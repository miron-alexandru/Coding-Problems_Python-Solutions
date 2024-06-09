# Problem Link: https://www.hackerrank.com/challenges/re-start-re-end/problem


# My solution:
import re

s = input("Enter the string s: ")
k = input("Enter the string k: ")

matches = list(re.finditer(k, s))
if matches:
    for m in matches:
        start, end = m.start(), m.start() + len(k) - 1
        print((start, end))
else:
    print((-1, -1))
