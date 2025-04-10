# problem link: https://leetcode.com/problems/largest-divisible-subset/


# my solution:
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        # Initialize DP and prev arrays
        dp = [1] * n  # dp[i] is the size of the largest subset ending with nums[i]
        prev = [-1] * n  # To reconstruct the subset

        max_size = 1
        max_index = 0

        # Fill the DP table
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > max_size:
                max_size = dp[i]
                max_index = i

        # Reconstruct the subset
        result = []
        i = max_index
        while i != -1:
            result.append(nums[i])
            i = prev[i]

        result.reverse()
        return result