# Problem Link: https://www.codewars.com/kata/5254ca2719453dcc0b00027d


# My Solution:
import itertools

def permutations(s):
    perms = set(''.join(p) for p in itertools.permutations(s))
    return list(perms)