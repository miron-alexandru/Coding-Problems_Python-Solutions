# Problem Link: https://www.hackerrank.com/challenges/30-regex-patterns/problem


# My Solution:
import re

n = int(input())
names = []

for i in range(n):
    name, email = input().split()
    if re.search(r'@gmail\.com$', email):
        names.append(name)

for name in sorted(names):
    print(name)
