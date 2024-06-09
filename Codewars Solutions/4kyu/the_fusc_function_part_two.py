# problem link: https://www.codewars.com/kata/57040e445a726387a1001cf7/train/python


# my solution:
def fusc(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    while n > 1:
        if n % 2 == 0:
            b = a + b
        else:
            a = a + b
        n //= 2

    return a + b
