# Problem Link: https://www.hackerrank.com/challenges/input/problem


# My solution
def evaluate_polynomial(x, k, p):
    return eval(p) == k


x, k = map(int, input().strip().split())
p = input().strip()

print(evaluate_polynomial(x, k, p))
