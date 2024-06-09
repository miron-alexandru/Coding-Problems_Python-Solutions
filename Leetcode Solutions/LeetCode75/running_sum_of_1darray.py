# problem link: https://leetcode.com/problems/running-sum-of-1d-array


# my solution:
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        #  Init an array of the same length as nums
        running_sum = [0] * len(nums)
        so_far = 0
        # Loop through each element n in nums, add n to so_far and store the result in the array created
        for i, n in enumerate(nums):
            so_far += n
            running_sum[i] = so_far
        return running_sum
