# Problem Link: https://www.codewars.com/kata/55f2b110f61eb01779000053


# My Solution:
def get_sum(a,b):
    return sum(list(range(a, b+1))) if a < b else sum(list(range(b, a+1)))