# problem link: https://leetcode.com/problems/word-break


# my solution:
# using dynamic programming

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
	    n = len(s)

	    # Initialize a boolean array dp of length (n + 1) to track segmentation
	    dp = [False] * (n + 1)

	    # Empty string can always be segmented into zero words
	    dp[0] = True

	    for i in range(1, n + 1):
	        for j in range(i):
	            # Check if the substring s[j:i] is in the wordDict
	            # and if the previous substring s[0:j] can be segmented
	            if dp[j] and s[j:i] in wordDict:
	                # Set dp[i] to True as the substring s[0:i] can be segmented into words
	                dp[i] = True
	                # Exit the inner loop as we have found a segmentation for s[0:i]
	                break
	    return dp[n]

