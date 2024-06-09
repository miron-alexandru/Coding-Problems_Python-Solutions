"""
Read in two integers, a and b, and print three lines.
The first line is the integer division a // b
The second line in the result of the modulo operator: a % b.
The third line prints the divmod of a and b.


Input format
The first line contains the first integer, a. and the second line
contains the second integer, b.


Output format
Print the result as described above.


Sample input
177
10


Sample output
17
7
(17, 7)
"""


# My solution:
a = int(input())
b = int(input())

print(a // b)
print(a % b)
print(divmod(a, b))
