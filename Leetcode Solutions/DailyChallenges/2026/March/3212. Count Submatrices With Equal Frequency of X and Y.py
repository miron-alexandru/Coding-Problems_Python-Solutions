# problem link: https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y


# Description:
"""
Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of submatrices that contain:

grid[0][0]
an equal frequency of 'X' and 'Y'.
at least one 'X'.
 

Example 1:

Input: grid = [["X","Y","."],["Y",".","."]]

Output: 3

Explanation:



Example 2:

Input: grid = [["X","X"],["X","Y"]]

Output: 0

Explanation:

No submatrix has an equal frequency of 'X' and 'Y'.

Example 3:

Input: grid = [[".","."],[".","."]]

Output: 0

Explanation:

No submatrix has at least one 'X'.
"""

# Solution:
from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # prefix sum for values
        ps = [[0]*(n+1) for _ in range(m+1)]
        # prefix sum for X count
        px = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                val = 0
                if grid[i][j] == 'X':
                    val = 1
                elif grid[i][j] == 'Y':
                    val = -1
                
                ps[i+1][j+1] = val + ps[i][j+1] + ps[i+1][j] - ps[i][j]
                px[i+1][j+1] = (1 if grid[i][j] == 'X' else 0) + px[i][j+1] + px[i+1][j] - px[i][j]
        
        ans = 0
        
        for i in range(m):
            for j in range(n):
                total = ps[i+1][j+1]
                count_x = px[i+1][j+1]
                
                if total == 0 and count_x > 0:
                    ans += 1
        
        return ans