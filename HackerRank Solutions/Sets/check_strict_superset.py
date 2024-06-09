"""
You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of the N
sets.
Print true if A is a strict superset of each of the N. Otherwise, print
False


Input format
The first line contains the space separated elements if set A.
The second lien contains integer n, the number of other sets.
The next n liens contains the space separated elements of other sets.


Output format
Print true if set A is a strict superset of all other N sets.
Otherwise print False.


Sample input
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

Sample output
False
"""

# My Solution
a = set(map(int, input().strip().split()))
n = int(input().strip())

sets = [set(map(int, input().split())) for s in range(n)]

result = True
for sets in sets:
    if not set(sets).issubset(a) or len(sets) >= len(a):
        result = False
        break

print(result)
