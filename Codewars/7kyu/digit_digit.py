# Problem Link: https://www.codewars.com/kata/546e2562b03326a88e000020


# My Solution:
def square_digits(num):
    return int("".join(str(int(i) ** 2) for i in str(num)))
