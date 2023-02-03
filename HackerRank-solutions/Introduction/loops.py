'''
The provided code stub reads and integer, n, from STDIN.
For all non-negative integers i < n, print i ** 2.

Example
n = 3

The list of non-negative integers that are less than n =3 is [0,1,2].
Print the square of each number on a separate line.
0
1
4


Input format
The first and only line contains the integer, n.


Output format
Print n lines, one coresponding to each i.


Sample input
5


Sample output
0
1
4
9
16
'''

# My Solution

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i ** 2)