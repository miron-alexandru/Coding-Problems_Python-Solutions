# Problem Link: https://www.hackerrank.com/challenges/game-of-stones-1/problem


# My Solution:

def gameOfStones(n):
    if n % 7 in [0, 1]:
        return "Second"
    else:
        return "First"