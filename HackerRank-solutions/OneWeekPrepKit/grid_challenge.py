# Problem https://www.hackerrank.com/challenges/one-week-preparation-kit-grid-challenge/problem


# My Solution:
def gridChallenge(grid):
    # sort rows
    for i in range(len(grid)):
        grid[i] = sorted(grid[i])

    # check each row for ascending alphabetical order
    for j in range(len(grid[0])):
        for i in range(1, len(grid)):
            if grid[i][j] < grid[i - 1][j]:
                return "NO"

    return "YES"
