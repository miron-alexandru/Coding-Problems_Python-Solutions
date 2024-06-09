# Problem Link: https://www.hackerrank.com/challenges/py-collections-deque/problem


# My solution:
from collections import deque

n = int(input())
d = deque()

for op in range(n):
    line = input().strip().split()
    op = line[0]
    args = line[1:]
    if op == "append":
        d.append(int(args[0]))
    elif op == "appendleft":
        d.appendleft(int(args[0]))
    elif op == "pop":
        d.pop()
    elif op == "popleft":
        d.popleft()

print(" ".join(str(x) for x in d))
