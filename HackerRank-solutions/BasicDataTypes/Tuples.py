# Given an integer, n, and n space-separated integers as input
# create a tuple, t, of those n integer. Then compute and
# print the result of hash(t)


# Input format
# The first line contains an integer, n, denoting
# the number of elements in the tuple.
# The second line contains n space-separated integers
# describing the elements in the tuple t.


# Output format
# Print the result of hash(t)


# Sample input
# 2
# 1 2


# Sample Output
# 3713081631934410656


# My Solution: (Might not work with Python 3 (gives negative output), but works with Pypy3)
n = int(input())
t = tuple(map(int, input().split()))
print(hash(t))
