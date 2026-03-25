# problem link: https://leetcode.com/problems/equal-sum-grid-partition-i/


# Description:
"""
You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:

Each of the two resulting sections formed by the cut is non-empty.
The sum of the elements in both sections is equal.
Return true if such a partition exists; otherwise return false.

 

Example 1:

Input: grid = [[1,4],[2,3]]

Output: true

Explanation:



A horizontal cut between row 0 and row 1 results in two non-empty sections, each with a sum of 5. Thus, the answer is true.

Example 2:

Input: grid = [[1,3],[2,4]]

Output: false

Explanation:

No horizontal or vertical cut results in two non-empty sections with equal sums. Thus, the answer is false.
"""

# sOLUTION:
from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        total = sum(sum(row) for row in grid)
        
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        # Check horizontal cuts
        curr = 0
        for i in range(m - 1):  # ensure bottom part is non-empty
            curr += sum(grid[i])
            if curr == target:
                return True
        
        # Compute column sums
        col_sums = [0] * n
        for i in range(m):
            for j in range(n):
                col_sums[j] += grid[i][j]
        
        # Check vertical cuts
        curr = 0
        for j in range(n - 1):  # ensure right part is non-empty
            curr += col_sums[j]
            if curr == target:
                return True
        
        return False