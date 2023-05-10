# Problem Link: https://www.hackerrank.com/challenges/two-strings/problem


# My Solution:
def twoStrings(s1, s2):
    for c in s1:
        if c in s2:
            return "YES"
    return "NO"
