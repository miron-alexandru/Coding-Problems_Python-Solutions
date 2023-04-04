# problem link: https://www.hackerrank.com/challenges/hex-color-code/problem


# my solution:
import re
n = int(input())
for i in range(n):
    pattern = re.findall(r"(\#[a-f0-9]{3,6})[\;\,\)]{1}", input(), re.I)
    if pattern:
        for k in list(pattern):
            print(k)