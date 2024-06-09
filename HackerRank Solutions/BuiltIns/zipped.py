# Problem Link: https://www.hackerrank.com/challenges/zipped/problem


# My solution:

x = list(map(int, input().split()))
n = [map(float, input().split()) for i in range(x[1])]
for i in zip(*n):
    print(sum(i) / x[1])
