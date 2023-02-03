'''
The students of District College have subscriptions to English
and Frech newspapers. Some students have subscribed only to 
English, some have subscribed to only French and some have subscribed to
both newspapers. You are given two sets of student roll numbers.
One set has subscribed to the English newspaper. and the other set
is subscribed to the French newspaper. The same student could be in both sets
Your task is to find the total number of students who have subscribed
to at least one newspaper.


Input format
The first line contains an integer, n, the number of students who have
subscribed to the English newspaper.
The second line contains n space separated roll numbers of those students.
The third line contains b, the number of students who have subscribed to the French newspaper.
The fourth line contains b space separated roll numbers of those students.


Output format
Output the total number of students who have subscriptions to both 
English and French newspapers.

Sample input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8


Sample output
5
'''

# My Solution

n = int(input().strip())
s_set = set(map(int, input().split()))
b = int(input().strip())
b_set = set(map(int, input().split()))

print(len(s_set & b_set))