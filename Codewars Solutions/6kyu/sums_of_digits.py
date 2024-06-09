# Problem Link: https://www.codewars.com/kata/541c8630095125aba6000c00


# My Solution:
def digital_root(n):
    if n < 10:
        return n
    else:
        return digital_root(sum(int(digit) for digit in str(n)))
