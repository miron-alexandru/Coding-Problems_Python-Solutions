"""
You are given a string S.
Your task is to print all possible size k replacement comb of the string
in lexicographic sorted order.


Input format
A single line containing space separated string S  and the int value
k.


Output format
Print the combinations of ftheir replacements of string S on separate
lines.

Sample input
HACK 2

Sample output
AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
"""

# Solution:


def comb_replacement(s, k):
    from itertools import combinations_with_replacement

    s = sorted(s)
    for comb in combinations_with_replacement(s, k):
        print("".join(comb))


s, k = input().split()
comb_replacement(s, int(k))
