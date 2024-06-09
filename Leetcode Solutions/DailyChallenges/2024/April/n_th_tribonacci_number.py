# problem link: https://leetcode.com/problems/n-th-tribonacci-number


# my solution:
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            tn_minus_3, tn_minus_2, tn_minus_1 = 0, 1, 1
            for _ in range(3, n + 1):
                tn = tn_minus_3 + tn_minus_2 + tn_minus_1
                tn_minus_3, tn_minus_2, tn_minus_1 = tn_minus_2, tn_minus_1, tn
            return tn
