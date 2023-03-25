# Problem link: https://www.hackerrank.com/challenges/polar-coordinates/problem


# My Solution:
import cmath


z = complex((input()))
values = cmath.polar(z)
for v in values:
    print(v)