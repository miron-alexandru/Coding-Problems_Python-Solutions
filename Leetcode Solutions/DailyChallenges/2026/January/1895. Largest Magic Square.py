# problem link: https://leetcode.com/problems/largest-magic-square/


# Description:
"""
A k x k magic square is a k x k grid filled with integers such that every row sum, every column sum, and both diagonal sums are all equal. The integers in the magic square do not have to be distinct. Every 1 x 1 grid is trivially a magic square.

Given an m x n integer grid, return the size (i.e., the side length k) of the largest magic square that can be found within this grid.

 

Example 1:


Input: grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
Output: 3
Explanation: The largest magic square has a size of 3.
Every row sum, column sum, and diagonal sum of this magic square is equal to 12.
- Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12
- Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12
- Diagonal sums: 5+4+3 = 6+4+2 = 12
Example 2:


Input: grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
Output: 2
"""

# Solution:
class Solution:
    def largestMagicSquare(self, grid):
        m = len(grid)
        n = len(grid[0])

        row = [[0] * (n + 1) for _ in range(m)]
        col = [[0] * n for _ in range(m + 1)]
        diag = [[0] * (n + 1) for _ in range(m + 1)]
        anti = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                row[i][j + 1] = row[i][j] + grid[i][j]
                col[i + 1][j] = col[i][j] + grid[i][j]
                diag[i + 1][j + 1] = diag[i][j] + grid[i][j]
                anti[i + 1][j] = anti[i][j + 1] + grid[i][j]

        for k in range(min(m, n), 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    target = row[i][j + k] - row[i][j]
                    valid = True

                    for r in range(i, i + k):
                        if row[r][j + k] - row[r][j] != target:
                            valid = False
                            break
                    if not valid:
                        continue

                    for c in range(j, j + k):
                        if col[i + k][c] - col[i][c] != target:
                            valid = False
                            break
                    if not valid:
                        continue

                    d1 = diag[i + k][j + k] - diag[i][j]
                    d2 = anti[i + k][j] - anti[i][j + k]

                    if d1 == target and d2 == target:
                        return k

        return 1
