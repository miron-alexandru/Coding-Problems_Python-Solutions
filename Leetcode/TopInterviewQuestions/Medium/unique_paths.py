# problem link: https://leetcode.com/problems/unique-paths/


# my solution:
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Init 2d array up of size m x n
        up = [[0] * n for i in range(m)]

        # only one way to reach the starting point
        up[0][0] = 1

        # is only one way to reach any point in the first column
        # going down
        for i in range(1, m):
            up[i][0] = 1

        # only one way to reach any point in the first row
        # going right
        for j in range(1, n):
            up[0][j] = 1

        # calculate the number of unique paths as the sum of
        # the number of paths to reach the cell above and the cell to the left
        for i in range(1, m):
            for j in range(1, n):
                up[i][j] = up[i - 1][j] + up[i][j - 1]

        return up[m - 1][n - 1]
