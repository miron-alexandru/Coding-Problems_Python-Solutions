# problem link: https://www.hackerrank.com/challenges/sherlock-and-squares/problem


# my solution:
import math

def squares(a, b):
    count = 0
    lower = math.ceil(math.sqrt(a))
    upper = math.floor(math.sqrt(b))

    for i in range(lower, upper + 1):
        if i ** 2 >= a and i ** 2 <= b:
            count += 1

    return count