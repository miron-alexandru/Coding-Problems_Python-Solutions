# Problem Link: https://www.hackerrank.com/challenges/find-angle/problem


# My solution:
import math

AB = float(input())
BC = float(input())

AC = math.sqrt(AB**2 + BC**2)
MC = AC / 2

angle = round(math.degrees(math.atan2(AB, BC)))

print("{}{}".format(angle, chr(176)))
