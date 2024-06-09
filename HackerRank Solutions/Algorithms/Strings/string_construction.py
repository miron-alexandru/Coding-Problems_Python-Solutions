# problem link: https://www.hackerrank.com/challenges/string-construction/problem


# my solution:
def stringConstruction(s):
    cost = 0
    unique = set()
    for char in s:
        if char not in unique:
            unique.add(char)
            cost += 1
    return cost