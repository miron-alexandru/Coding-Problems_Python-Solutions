# problem link: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element


# my solution:

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_length = 0
        left = 0
        count_zeros = 0

        for right, num in enumerate(nums):
            if num == 0:
                count_zeros += 1

            while count_zeros > 1:
                if nums[left] == 0:
                    count_zeros -= 1
                left += 1

            max_length = max(max_length, right - left)

        return max_length