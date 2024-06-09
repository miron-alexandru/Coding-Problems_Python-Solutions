# problem link: https://leetcode.com/problems/maximum-length-of-pair-chain


# my solution:
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Sort the pairs based on ending values
        pairs.sort(key=lambda x: x[1])
        
        n = len(pairs)
        
        # Initialize DP array
        dp = [1] * n
        
        # DP recurrence
        for i in range(1, n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # Find the maximum length
        return max(dp)