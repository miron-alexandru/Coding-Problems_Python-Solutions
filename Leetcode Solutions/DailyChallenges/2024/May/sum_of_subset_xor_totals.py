# problem link: https://leetcode.com/problems/sum-of-all-subset-xor-totals


# my solution:
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result, n = 0, len(nums)

        for i in range(1 << n):
            s = 0
            for j in range(n):
                if i >> j & 1:
                    s ^= nums[j]
            result += s

        return result