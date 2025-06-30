# problem link: https://leetcode.com/problems/longest-harmonious-subsequence/


# Description:
"""
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:

Input: nums = [1,3,2,2,5,2,3,7]

Output: 5

Explanation:

The longest harmonious subsequence is [3,2,2,2,3].

Example 2:

Input: nums = [1,2,3,4]

Output: 2

Explanation:

The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.

Example 3:

Input: nums = [1,1,1,1]

Output: 0

Explanation:

No harmonic subsequence exists.
."""


# Solution:
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_len = 0

        for num in nums:
            if num + 1 in freq:
                max_len = max(max_len, freq[num] + freq[num + 1])

        return max_len
