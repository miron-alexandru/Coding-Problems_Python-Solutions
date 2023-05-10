# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e .
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.


# Initialize your list and read in the value of n followed by n lines of
# commands where each command will be of the 7 types listed above.
# Iterate through each command in order and perform the corresponding
# operation on your list.


# Input format
# The first lien contains an integer, n. denoting the number of commands.
# Each line i of the n subsequent lines contains one of the commands
# described above

# Constraints
# The elements added to the list must be integers.

# Output format
# For each command of type print, print the list on a a new line


# Sample input
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# remove 9
# append 1
# sort
# print
# pop
# reverse
# print


# Sample output
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]


# My Solution:

list = []
n = int(input().strip())

for i in range(n):
    line = input().strip().split()
    cmd = line[0]
    args = line[1:]

    if cmd == "insert":
        list.insert(int(args[0]), int(args[1]))
    elif cmd == "print":
        print(list)
    elif cmd == "remove":
        list.remove(int(args[0]))
    elif cmd == "append":
        list.append(int(args[0]))
    elif cmd == "sort":
        list.sort()
    elif cmd == "pop":
        list.pop()
    elif cmd == "reverse":
        list.reverse()
