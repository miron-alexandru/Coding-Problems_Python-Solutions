"""
The included code stub will read an integer, n, from STDIN.
Without using any string methods, try to print the following:
123...n
Note that "..." represents the consecutive values in between.

Example

n = 5

Print the string 12345

Input format
The first line contains an integer n.


Output format
Print the list of integers from 1 trough n as a string without spaces.

Sample input
3

Sample output
123
"""

# My Solution
n = int(input())
for i in range(1, n + 1):
    print(i, end="")
