# Problem Link: https://www.hackerrank.com/challenges/30-bitwise-and/problem


# My Solution:
def bitwiseAnd(N, K):
    max_and = 0
    for a in range(N, 0, -1):
        for b in range(a - 1, 0, -1):
            if (a & b) < K and (a & b) > max_and:
                max_and = a & b
            if max_and == K - 1:
                return max_and
    return max_and
