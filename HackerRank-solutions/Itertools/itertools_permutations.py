"""
You are given a string S.
Your task is to print all possible permutations of size k of the string
in lexicographic sorted order.


Input format
A single line containing space separated string S  and the int value
k.


Output format
Print the permutations of the string S on separate lines.

Sample input
HACK 2

Sample output
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
"""

# Solution:


def permutations(s, k):
    from itertools import permutations

    s = sorted(s)
    for comb in permutations(s, k):
        print("".join(comb))


s, k = input().split()
permutations(s, int(k))
