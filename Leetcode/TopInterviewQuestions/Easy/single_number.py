# Problem Link: https://leetcode.com/problems/single-number


# Solution:
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result