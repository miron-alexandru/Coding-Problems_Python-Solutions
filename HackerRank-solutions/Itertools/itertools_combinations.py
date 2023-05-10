"""
You are given a string S.
Your task is to print all possible combinations, up to size k, of the
string in lexicograaphic sorted order.

Input format
A single line containing the string S and the integer value k, separated by a space


Output format
Print the different combinations of string S on a separate line

Sample Input
HACK 2


Sample output
A
C
H
K
AC
AH
AK
CH
CK
HK
"""

# My Solution:


def combinations(s, k):
    from itertools import combinations

    s = sorted(s)
    for i in range(1, k + 1):
        for comb in combinations(s, i):
            print("".join(comb))


s, k = input().split()
combinations(s, int(k))
