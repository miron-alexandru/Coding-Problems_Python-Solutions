# Problem Link: https://www.codewars.com/kata/513e08acc600c94f01000001


# My Solution:
def rgb(r, g, b):
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    return "{:02X}{:02X}{:02X}".format(r, g, b)
