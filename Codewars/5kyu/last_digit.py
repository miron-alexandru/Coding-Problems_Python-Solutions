# Problem Link: https://www.codewars.com/kata/5511b2f550906349a70004e1


# My Solution:
def last_digit(n1, n2):
    if n2 == 0:
        return 1
    if n1 == 0:
        return 0
    return pow(n1, n2, 10)
