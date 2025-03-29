# problem link: https://leetcode.com/problems/longest-nice-subarray/




# my solution:

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        max_length = 0
        bit_mask = 0
        left = 0
        
        for right, num in enumerate(nums):
            while bit_mask & num:
                bit_mask ^= nums[left]
                left += 1
            bit_mask |= num
            max_length = max(max_length, right - left + 1)
        
        return max_length
