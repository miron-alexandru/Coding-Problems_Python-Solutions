# problem link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/


# Description:
"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
"""

# Solution:
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        row = 0
        col = n - 1
        count = 0

        while row < m and col >= 0:
            if grid[row][col] < 0:
                count += m - row
                col -= 1
            else:
                row += 1

        return count
