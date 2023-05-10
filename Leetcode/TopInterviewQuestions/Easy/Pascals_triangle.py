# Problem Link: https://leetcode.com/problems/pascals-triangle/


# My Solution:
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        t = [[1]]
        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(t[i - 1][j - 1] + t[i - 1][j])
            row.append(1)
            t.append(row)

        return t
