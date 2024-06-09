# problem link: https://www.hackerrank.com/challenges/detect-html-tags/problem

# my solution:
import re

n = int(input())
tags = set()

for t in range(n):
    line = input()
    # find all occurrences of HTML tags
    matches = re.findall(r"<\s*(\w+)", line)
    for tag in matches:
        tags.add(tag)

print(";".join(sorted(tags)))
