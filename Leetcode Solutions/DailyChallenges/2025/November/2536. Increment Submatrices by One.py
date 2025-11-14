# problem link: https://leetcode.com/problems/increment-submatrices-by-one/



# Description:
"""
You are given a positive integer n, indicating that we initially have an n x n 0-indexed integer matrix mat filled with zeroes.

You are also given a 2D integer array query. For each query[i] = [row1i, col1i, row2i, col2i], you should do the following operation:

Add 1 to every element in the submatrix with the top left corner (row1i, col1i) and the bottom right corner (row2i, col2i). That is, add 1 to mat[x][y] for all row1i <= x <= row2i and col1i <= y <= col2i.
Return the matrix mat after performing every query.

 

Example 1:


Input: n = 3, queries = [[1,1,2,2],[0,0,1,1]]
Output: [[1,1,0],[1,2,1],[0,1,1]]
Explanation: The diagram above shows the initial matrix, the matrix after the first query, and the matrix after the second query.
- In the first query, we add 1 to every element in the submatrix with the top left corner (1, 1) and bottom right corner (2, 2).
- In the second query, we add 1 to every element in the submatrix with the top left corner (0, 0) and bottom right corner (1, 1).
Example 2:


Input: n = 2, queries = [[0,0,1,1]]
Output: [[1,1],[1,1]]
Explanation: The diagram above shows the initial matrix and the matrix after the first query.
- In the first query we add 1 to every element in the matrix.
"""

# Solution:
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # difference array (n x (n+1)) 
        diff = [[0] * (n + 1) for _ in range(n)]
        
        # apply range updates row by row
        for r1, c1, r2, c2 in queries:
            for r in range(r1, r2 + 1):
                diff[r][c1] += 1
                diff[r][c2 + 1] -= 1
        
        # build the result using prefix sums
        res = [[0] * n for _ in range(n)]
        for r in range(n):
            running = 0
            for c in range(n):
                running += diff[r][c]
                res[r][c] = running
        
        return res
