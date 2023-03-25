'''
You are given three integers: a, b, and m. Print two lines.
One the first line, print the result of pow(a,b). On the second line 
print the result of pow(a, b,m)

Input format
The first line contains a, the second b, and the third m.


Sample input
3
4
5

Sample output
81
1
'''

# My solution
a = int(input())
b = int(input())
m = int(input())

print(pow(a, b))
print(pow(a, b, m))
