# problem link: https://leetcode.com/problems/jump-game-vii/


# Description:
"""
You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.

 

Example 1:

Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation:
In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.
Example 2:

Input: s = "01101110", minJump = 2, maxJump = 3
Output: false
"""

# Solution:

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False] * n
        dp[0] = True

        # prefix[i] = number of reachable (True) indices in dp[0..i]
        prefix = [0] * n
        prefix[0] = 1

        for i in range(1, n):
            if s[i] == '0':
                # Any reachable index in [i - maxJump, i - minJump] can reach i
                lo = max(0, i - maxJump)
                hi = i - minJump

                if hi >= 0:
                    # Count of reachable indices in window [lo, hi]
                    window_reachable = prefix[hi] - (prefix[lo - 1] if lo > 0 else 0)
                    dp[i] = window_reachable > 0

            prefix[i] = prefix[i - 1] + (1 if dp[i] else 0)

        return dp[n - 1]
