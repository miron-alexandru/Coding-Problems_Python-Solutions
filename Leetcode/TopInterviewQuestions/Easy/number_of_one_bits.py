# Problem Link: https://leetcode.com/problems/number-of-1-bits/


# My Solution:
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            count += 1
            n &= n - 1
        return count
