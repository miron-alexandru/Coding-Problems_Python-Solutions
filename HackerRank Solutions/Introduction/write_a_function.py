"""
Given a year, determine whether it is a leap year. If it is a leap year,
return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and 
passes arguments to the is_leap function.
It is only necessary to complete the is_leap function.


Read year, the year to test.


Output format
The function must return a Boolean value (True/False).
Output is handled by the provided code stub.


Sample input
1990


Sample output
False
"""

# My Solution


def is_leap(year):
    leap = False

    if (year % 4 == 0) and (year % 100 != 0):
        leap = True
    elif (year % 400 == 0) and (year % 100 == 0):
        leap = True

    return leap


year = int(input())
