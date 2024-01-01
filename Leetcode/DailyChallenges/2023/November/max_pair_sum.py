# problem link: https://leetcode.com/problems/minimize-maximum-pair-sum-in-array


# my solution:

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        max_pair_sum = 0

        for i in range(n // 2):
            pair_sum = (nums[i] + nums[n - i - 1])
            max_pair_sum = max(max_pair_sum, pair_sum)

        return max_pair_sum