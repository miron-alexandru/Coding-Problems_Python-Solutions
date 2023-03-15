# Problem Link: https://leetcode.com/problems/rotate-image/


# My Solution:

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        #reverse each row 
        for i in range(n):
            matrix[i].reverse()