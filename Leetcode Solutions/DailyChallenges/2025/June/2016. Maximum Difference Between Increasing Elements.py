# problem link: https://leetcode.com/problems/maximum-difference-between-increasing-elements/


# Description
"""
Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.

"""



# Solution:
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_so_far = nums[0]
        max_diff = -1

        # Start from index 1 because min_so_far is already nums[0]
        for j in range(1, len(nums)):
            # If current number is greater than the min so far
            # we have a valid pair (i, j) such that i < j and nums[i] < nums[j]
            if nums[j] > min_so_far:
                # Update the max_diff if this difference is greater
                max_diff = max(max_diff, nums[j] - min_so_far)
            else:
                # If current number is smaller than or equal to min_so_far,
                # update min_so_far to the current number
                min_so_far = nums[j]
        
        return max_diff