"""
There is an array of n integers. There are also 2 disjoint sets, A and B
each containing m integers. You like all the integers in set A and dislike
all the integers in set B. Your initial happiness is 0. For each i integer 
in the array, if i is in A, you add 1 to your happiness. If i is in B,
you add -1 to your happinness. Otherwise, your happiness does not change. 
Output your final happiness at the end.


Input format
The first line contains integers n and m separated by a space
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.


Output format
Output a single integer, your total happiness


Sample input
3 2
1 5 3
3 1
5 7


Sample output
1
"""

# My solution
n, m = (int(i) for i in input().split())
arr = map(int, input().strip().split())
set_a = set(map(int, input().strip().split()))
set_b = set(map(int, input().strip().split()))

happiness = 0
for i in arr:
    if i in set_a:
        happiness += 1
    if i in set_b:
        happiness -= 1

print(happiness)
