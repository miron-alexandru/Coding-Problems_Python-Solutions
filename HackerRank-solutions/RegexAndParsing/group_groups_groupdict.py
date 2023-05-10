# Problem Link: https://www.hackerrank.com/challenges/re-group-groups/problem


# My solution:
import re

pat = re.compile(r"([a-zA-Z0-9])\1")
match = pat.search(input())

if match:
    print(match.group(1))
else:
    print(-1)
