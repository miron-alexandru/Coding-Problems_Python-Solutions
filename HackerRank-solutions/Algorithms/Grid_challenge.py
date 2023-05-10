# Problem Link: https://www.hackerrank.com/challenges/grid-challenge/problem


# My Solution:
def gridChallenge(grid):
    # Sort each row
    for i in range(len(grid)):
        grid[i] = sorted(grid[i])

    # Check each row for ascending alphabetical order
    for j in range(len(grid[0])):
        for i in range(1, len(grid)):
            if grid[i][j] < grid[i - 1][j]:
                return "NO"
    return "YES"
