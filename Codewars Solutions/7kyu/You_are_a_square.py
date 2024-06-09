# Problem link: https://www.codewars.com/kata/54c27a33fb7da0db0100040e


# My Solution:
import math


def is_square(n):
    if n < 0:
        return False
    square = int(math.sqrt(n))
    return square * square == n
