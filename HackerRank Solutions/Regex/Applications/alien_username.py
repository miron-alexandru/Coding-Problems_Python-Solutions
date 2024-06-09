# problem link: https://www.hackerrank.com/challenges/alien-username/problem

# my solution:

import re

n = int(input())
for i in range(n):
    s = input().strip()
    if re.match(r"^[_.]\d+[a-zA-Z]*_?$", s):
        print("VALID")
    else:
        print("INVALID")
