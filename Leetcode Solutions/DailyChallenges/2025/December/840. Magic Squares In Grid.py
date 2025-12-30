# problem link: https://leetcode.com/problems/magic-squares-in-grid/



# Description:
"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

 

Example 1:


Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:

while this one is not:

In total, there is only one magic square inside the given grid.
Example 2:

Input: grid = [[8]]
Output: 0
"""

# Solution:
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        for i in range(rows - 2):
            for j in range(cols - 2):
                if self.is_magic(grid, i, j):
                    res += 1

        return res

    def is_magic(self, g, r, c):
        if g[r + 1][c + 1] != 5:
            return False

        seen = set()
        for i in range(r, r + 3):
            for j in range(c, c + 3):
                v = g[i][j]
                if v < 1 or v > 9 or v in seen:
                    return False
                seen.add(v)

        for i in range(3):
            if sum(g[r + i][c:c + 3]) != 15:
                return False
            if g[r][c + i] + g[r + 1][c + i] + g[r + 2][c + i] != 15:
                return False

        if g[r][c] + g[r + 1][c + 1] + g[r + 2][c + 2] != 15:
            return False
        if g[r][c + 2] + g[r + 1][c + 1] + g[r + 2][c] != 15:
            return False

        return True