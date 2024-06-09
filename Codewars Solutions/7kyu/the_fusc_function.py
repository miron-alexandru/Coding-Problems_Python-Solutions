# problem link: https://www.codewars.com/kata/570409d3d80ec699af001bf9/train/python


# my solution:
def fusc(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2 == 0:
        return fusc(n // 2)
    else:
        return fusc(n // 2) + fusc(n // 2 + 1)
