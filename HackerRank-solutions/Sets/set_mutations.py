'''
You are given a set A and N number of other sets. These N number of
sets have to perform some specific mutation operations on set A.
Your task is to execute those operations and print the sum of elements 
from set A.


Input format
The first line contains the number of elements in set A.
The second line contains the space separated list of elements in set A.
The third lien contains integer N, the number of other sets.
The next 2 * N lines are divided into N parts containing two lines each
The first lien of each part contains the space separated entries of
the operation name and the length of the other set.
The second line of each part c ontains space separated list of elements
in the other set.


Output format
Output the sum of elements in set A.


Sample input
16
1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
4
intersection_update 10
2 3 5 6 8 9 1 4 7 11
update 2
55 66
symmetric_difference_update 5
22 7 35 62 58
difference_update 7
11 22 35 55 58 62 66


Sample output
38
'''

# My Solution:

n = int(input().strip())
a = set(map(int, input().strip().split()))
ops = int(input().strip())

for i in range(ops):
	op, len_set = map(str, input().strip().split())
	b = set(map(int, input().strip().split()))
	if op == 'intersection_update':
		a.intersection_update(b)
	elif op == 'update':
		a.update(b)
	elif op = 'symmetric_difference_update':
		a.symmetric_difference_update(b)
	else: 
		a.difference_update(b)

print(sum(a))

# Solution 2
n = int(input().strip())
a = set(map(int, input().strip().split()))
m = int(input().strip())

ops = {'intersection_update': a.intersection_update,
       'update': a.update,
       'symmetric_difference_update': a.symmetric_difference_update,
       'difference_update': a.difference_update}

for i in range(m):
    op, _ = input().split()
    b = set(map(int, input().split()))
    ops[op](b)

print(sum(a))
