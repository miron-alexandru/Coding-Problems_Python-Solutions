"""
You are given a two lists A and B. Your task is to comute their cartesian
product AxB

Input format
The first line contains the space separated elements of list A.
The second line contains the space separated elements of list B.
Both lists have no duplicate integer elements.


Output format
Output the space separated tuples of the cartesian product.


Sample Input
1 2
3 4

Sample Output
(1, 3) (1, 4) (2, 3) (2, 4)
"""

# My solution
from itertools import product

a = map(int, input().strip().split())
b = map(int, input().strip().split())

for x, y in product(a, b):
    print("({}, {})".format(x, y), end=" ")
