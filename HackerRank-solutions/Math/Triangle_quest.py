'''
You are given a positive integer N. Print a numerical triangle
of height N - 1 like the one below:
1
22
333
4444
55555
......


Input format
A single line containing integer, N.


Output format
Print N - 1 liens as explained above.

Sample input
5

Sample output
1
22
333
4444
'''


# Solution:
for i in range(1,int(input())):
    print(i*(10**i-1)//9)