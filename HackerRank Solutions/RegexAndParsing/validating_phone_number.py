# problem link: https://www.hackerrank.com/challenges/validating-the-phone-number/problem

# my solution:
import re

n = int(input())

for i in range(n):
    number = input().strip()
    if re.match(r"[789]\d{9}$", number):
        print("YES")
    else:
        print("NO")
