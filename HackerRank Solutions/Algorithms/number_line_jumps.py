# Problem link: https://www.hackerrank.com/challenges/kangaroo/problem


# My Solution:
def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v1 <= v2:
        return "NO"
    if x2 < x1 and v2 <= v1:
        return "NO"
    d = abs(x1 - x2)
    r = abs(v1 - v2)
    if r == 0:
        return "YES" if x1 == x2 else "NO"
    j = d / r
    return "YES" if j.is_integer() and j >= 0 else "NO"
