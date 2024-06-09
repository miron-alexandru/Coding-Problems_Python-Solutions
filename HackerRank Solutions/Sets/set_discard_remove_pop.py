"""
You have a non-empty set s, and you have to execute N commands
given in N lines.
The commands will be pop, remove and discard.


Input format
The first line contains integer n, the number of elements in the set s.
The second line contains n space separated elements of set s.
All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer N, the number of commands.
The next N lines contains either pop, remove and/or discard commands
followed by their associated value.


Output format
The sum of the elements of set s on a single line.


Sample input
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5


Sample Output
4
"""

# My solution
n = int(input().strip())
s = set(map(int, input().split()))
m = int(input().strip())

for i in range(m):
    cmd = input().strip().split()
    if cmd[0] == "pop":
        s.pop()
    elif cmd[0] == "remove":
        s.discard(int(cmd[1]))
    else:
        s.discard(int(cmd[1]))

print(sum(s))
