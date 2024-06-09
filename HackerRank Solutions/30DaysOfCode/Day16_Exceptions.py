# Problem Link: https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem


# My Solution:
S = input()

try:
    print(int(S))
except ValueError as ve:
    print("Bad String")
