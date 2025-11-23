# problem link: https://leetcode.com/problems/greatest-sum-divisible-by-three/


# Description:
"""
Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.

 

Example 1:

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
Example 2:

Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.
Example 3:

Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
"""


# Solution:
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-float('inf')] * 3 for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            x = nums[i - 1]
            for r in range(3):
                dp[i][r] = dp[i - 1][r]
                pr = (r - x) % 3
                dp[i][r] = max(dp[i][r], dp[i - 1][pr] + x)

        return dp[n][0]
