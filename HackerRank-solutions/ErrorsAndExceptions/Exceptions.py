'''
You are given two values a and b.
Perform integer division and print a/b.


Input format
The first line contains T, the number of test cases.
The next t lines each contain the space separated values of a and b.


Output format
Print the value of a/b
In case of ZeroDivisionError or ValueError, print the error code.


Sample input
3
1 0
2 $
3 1

Sample Output
Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
'''

# Solution:
t = int(input().strip())

for i in range(t):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except Exception as e:
        print('Error Code:', e)
