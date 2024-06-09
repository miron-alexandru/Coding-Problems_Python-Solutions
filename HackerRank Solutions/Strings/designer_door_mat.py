"""
Mr. Vincent works in a door mat manufacturing company.
One day, he designed a new door mat with the following specifications:

Mat size must be N x M. (N is an odd natural number, and M is 3 times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.


Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------


Input format
A single line containing the space separated values of N and M.


Output format
Output the design pattern.


Sample input
9 27


Sample output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""

# My Solution
n, m = map(int, input().split())
for i in range(int(n / 2)):
    print((".|." * (2 * i + 1)).center(m, "-"))
print("WELCOME".center(m, "-"))
for i in range(int(n / 2), 0, -1):
    print((".|." * (2 * i - 1)).center(m, "-"))
