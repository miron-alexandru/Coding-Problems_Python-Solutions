# Problem Link: https://www.hackerrank.com/challenges/introduction-to-regex/problem


# My Solution:
import re


def is_float(n):
    pattern = r"^[+-]?\d+\.\d+$|^[+-]?\.\d+$"
    match = re.match(pattern, n)
    return True if match else False


t = int(input())
n_list = [input() for _ in range(t)]

for n in n_list:
    if is_float(n):
        print("True")
    else:
        print("False")
