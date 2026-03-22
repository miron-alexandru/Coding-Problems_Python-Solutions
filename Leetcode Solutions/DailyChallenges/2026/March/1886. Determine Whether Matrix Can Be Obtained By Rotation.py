# problem link:https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/


# Description:
"""Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.

 

Example 1:


Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.
Example 2:


Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.
Example 3:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.

"""

# Solution:
from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(matrix):
            n = len(matrix)
            # transpose
            for i in range(n):
                for j in range(i + 1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            # reverse each row
            for row in matrix:
                row.reverse()

        for _ in range(4):
            if mat == target:
                return True
            rotate(mat)
        
        return False