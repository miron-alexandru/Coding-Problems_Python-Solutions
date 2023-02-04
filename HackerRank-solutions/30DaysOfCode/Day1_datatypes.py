'''
Complete the code in the editor below. The variables i, d and s are
already declared and initialized for you. You must:
1. Declare 3 variables. one of type int, one of type double, one of type string.
2. Read 3 lines of input from stdin (according to the sequence given in
the Input format section below) and initialize your 3 variables.
3. Use the + operator to perform the following operations:
    1. Print the sum of i plus your int variable on a new linee.
    2. Print the sum of d plus your double variable to a scale of
    one decimal place ona new line.
    3. Concatenate s with the string you read as input and print the result
    on a new line.


Input format
The first line contains an integer that you must sum with i.
The second line contains a double that you must sum with d.
The third line contains a string that you must concatenate with s.


Output format
Print the sum of both integers on the first line the sum of both doubles
(scaled to 1 decimal place) on the second line, and then the two 
concatenated strings on the third line.


Sample input
12
4.0
is the best place to learn and practice coding!


Sample output
16
8.0
HackerRank is the besst place to learn and practice coding!
'''

# My solution:
i = 4
d = 4.0
s = 'HackerRank '
second_i = int(input())
second_d = float(input())
second_s = str(input())

print(i + second_i)
print(d + second_d).
print(s + second_s)
