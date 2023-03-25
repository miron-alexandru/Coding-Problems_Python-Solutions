'''
Read four numbers, a, b, c, and d and print the result of a ** b + c ** d.

Input format
Integers a, b, c, and d are given four separate lines, respectively.


Output format
Print the result of a ** b + a ** c on one line

Sample input
9
29
7
27


Sample output
4710194409608608369201743232
'''


# My solution
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print((a ** b) + (c ** d))