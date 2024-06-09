# Problem Link: https://www.hackerrank.com/challenges/map-and-lambda-expression/problem


# My solution:

cube = lambda x: x**3


def fibonacci(n):
    result = []
    a, b = 0, 1
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result
