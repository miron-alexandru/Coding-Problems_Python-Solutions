# problem link: https://leetcode.com/problems/maximum-ascending-subarray-sum/


# my solution:
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                max_sum = max(max_sum, current_sum)
                current_sum = nums[i]

        return max(max_sum, current_sum)
