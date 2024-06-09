# Problem Link: https://www.hackerrank.com/challenges/re-findall-re-finditer/problem


# My Solution:


import re


sol = re.findall(r"[^aiueo]([aiueoAIUEO]{2,})(?=[^aiueo])", input())
if sol:
    for s in sol:
        print(s)
else:
    print(-1)
