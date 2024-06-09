# Problem Link: https://www.codewars.com/kata/51c8e37cee245da6b40000bd


# My Solution:


def strip_comments(s, markers):
    for marker in markers:
        s = "\n".join([line.split(marker)[0].rstrip() for line in s.split("\n")])
    return s
