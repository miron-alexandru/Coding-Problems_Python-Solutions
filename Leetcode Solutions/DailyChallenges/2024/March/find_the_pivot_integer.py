# problem link: https://leetcode.com/problems/find-the-pivot-integer/


# my solution:
class Solution:
    def pivotInteger(self, n: int) -> int:
        numbers_sum = n * (n + 1) // 2
        square_root = int(sqrt(numbers_sum))

        return square_root if square_root * square_root == numbers_sum else -1