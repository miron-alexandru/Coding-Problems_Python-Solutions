# Problem Link: https://www.hackerrank.com/challenges/30-review-loop/problem


# My Solution:
t = int(input())

for i in range(t):
    s = str(input())
    print(s[0::2] + " " + s[1::2])
