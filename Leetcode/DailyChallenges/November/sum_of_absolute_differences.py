# problem link: https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/


# my solution:
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        left_sum = 0
        for i in range(1, n):
            left_sum += i * (nums[i] - nums[i - 1])
            result[i] += left_sum

        right_sum = 0
        for i in range(n - 2, -1, -1):
            right_sum += (n - 1 - i) * (nums[i + 1] - nums[i])
            result[i] += right_sum

        return result