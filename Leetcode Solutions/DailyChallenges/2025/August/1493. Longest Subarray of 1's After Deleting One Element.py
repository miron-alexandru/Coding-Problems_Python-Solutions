# problem link: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/


# Desscription:
"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
"""


# Solution:
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_length = 0
        left = 0
        right = 0
        count_zeros = 0

        while right < len(nums):
            if nums[right] == 0:
                count_zeros += 1
            
            if count_zeros > 1:
                if nums[left] == 0:
                    count_zeros -= 1
                left += 1
            
            max_length = max(max_length, right - left)
            right += 1
        
        return max_length