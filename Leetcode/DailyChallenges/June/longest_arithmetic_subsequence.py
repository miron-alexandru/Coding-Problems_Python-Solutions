# problem link: https://leetcode.com/problems/longest-arithmetic-subsequence/


# my solution:
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        max_length = 0

        for i, num in enumerate(nums):
            for j in range(i):
                diff = num - nums[j]
                if diff in dp:
                    dp[diff][i] = dp[diff].get(j, 1) + 1
                else:
                    dp[diff] = {i: 2}

                max_length = max(max_length, dp[diff][i])

        return max_length