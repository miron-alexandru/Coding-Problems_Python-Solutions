# Problem link: https://www.hackerrank.com/challenges/incorrect-regex/problem

import re

# My Solution:
import re


def valid_regex(pattern):
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False


t = int(input().strip())
for i in range(t):
    pattern = input().strip()
    result = valid_regex(pattern)
    print(result)
