# Problem Link: https://www.hackerrank.com/challenges/maximize-it/problem


# My Solution:
from itertools import product as prod

k, m = map(int, input().split())
lists = [list(map(int, input().split()))[1:] for _ in range(k)]

max_val = 0
for combination in prod(*lists):
    value = sum(x ** 2 for x in combination) % m
    max_val = max(max_val, value)

print(max_val)
