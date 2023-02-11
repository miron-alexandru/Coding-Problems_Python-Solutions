# Problem link: https://www.hackerrank.com/challenges/30-recursion/problem


# My soluion:

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return (n * factorial(n- 1))
