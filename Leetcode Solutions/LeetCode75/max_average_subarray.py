# problem link: https://leetcode.com/problems/maximum-average-subarray-i


# my solution:
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_window = sum(nums[:k])
        max_sum = sum_window

        for i in range(k, len(nums)):
            sum_window += nums[i] - nums[i - k]
            max_sum = max(max_sum, sum_window)

        return max_sum / k