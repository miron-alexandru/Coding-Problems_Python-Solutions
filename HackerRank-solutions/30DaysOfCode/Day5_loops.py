# Problem Link: https://www.hackerrank.com/challenges/30-loops/problem


# My Solution:

n = int(input())

print("\n".join([f"{n} x {i} = {n*i}" for i in range(1, 11)]))
