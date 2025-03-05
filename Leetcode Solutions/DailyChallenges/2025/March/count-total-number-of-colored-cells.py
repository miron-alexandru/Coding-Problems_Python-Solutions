# problem link: https://leetcode.com/problems/count-total-number-of-colored-cells/


# my solution:
class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 2 * (n - 1) * n