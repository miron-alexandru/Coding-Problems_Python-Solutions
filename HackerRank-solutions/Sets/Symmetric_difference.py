'''
Given 2 sets of integers, M and N, print their symmetric difference
in ascending order. The termin symmetric difference indicates
those value that existt in either M or N but do not exist in both.


Input format
The first line of input contains and integer, M.
The second line contains M space-separated integers.
The third lien contains an integer, N.
The fourth lien contains N space-separated integers.


Output format
Output the symmetric difference integers in ascendign order, one
per line.


Sample input
4
2 4 5 9
4
2 4 11 12


Sample output 
5
9
11
12
'''

# My solution
def symmetric_difference(set_a, set_b):
	return sorted(list(set(set_a) ^ set(set_b)))

m = int(input().strip())
m_elements = set(map(int, input().strip().split()))
n = int(input().strip())
n_elements = set(map(int, input().strip().split()))

result = symmetric_difference(m_elements, n_elements)

for num in result:
	print(num)


# Second solution:
m, m_set = int(input()), set(map(int, input().split()))
n, n_set = int(input()), set(map(int, input().split()))

for num in sorted(list(m_set ^ n_set)):
    print(num)

