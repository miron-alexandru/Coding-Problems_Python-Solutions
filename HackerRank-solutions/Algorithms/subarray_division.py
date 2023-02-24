# Problem Link: https://www.hackerrank.com/challenges/the-birthday-bar/problem


# My solution:

def birthday(s, d, m):
    count = 0
    for i in range(len(s) - m + 1):
        if sum(s[i:i+m]) == d:
            count += 1
    return count