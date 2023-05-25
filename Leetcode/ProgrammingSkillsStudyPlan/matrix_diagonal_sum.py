# problem link: https://leetcode.com/problems/matrix-diagonal-sum


# my solution:
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0
        for i in range(n):
            for j in range(n):
                if i == j or i + j == n - 1:
                    total += mat[i][j]
        return total