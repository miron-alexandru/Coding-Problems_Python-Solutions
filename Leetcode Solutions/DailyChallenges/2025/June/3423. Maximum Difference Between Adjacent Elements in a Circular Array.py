# problem link: https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/


# description:
"""
Given a circular array nums, find the maximum absolute difference between adjacent elements.

Note: In a circular array, the first and last elements are adjacent.

 

Example 1:

Input: nums = [1,2,4]

Output: 3

Explanation:

Because nums is circular, nums[0] and nums[2] are adjacent. They have the maximum absolute difference of |4 - 1| = 3.

Example 2:

Input: nums = [-5,-10,-5]

Output: 5

Explanation:

The adjacent elements nums[0] and nums[1] have the maximum absolute difference of |-5 - (-10)| = 5.
"""

# Solutions:
#1 Straightforward

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        result = 0
        
        for i in range(1, len(nums)):
            diff = abs(nums[i] - nums[i-1])
            if diff > result:
                result = diff

        last_and_first = abs(nums[-1] - nums[0])
        if last_and_first > result:
            result = last_and_first

        return result


# One-liner (simplified):
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        return max(abs(a - b) for a, b in zip(nums, nums[1:] + nums[:1]))