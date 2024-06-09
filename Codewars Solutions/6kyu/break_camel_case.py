# Problem Link: https://www.codewars.com/kata/5208f99aee097e6552000148


# My Solution:
def solution(s):
    return "".join([" " + c if c.isupper() else c for c in s])
