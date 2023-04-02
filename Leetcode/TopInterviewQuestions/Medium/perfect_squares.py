# problem link: https://leetcode.com/problems/perfect-squares/


# my solution:
class Solution:
    def numSquares(self, n: int) -> int:
    	# Initialize the dp array with infinity except for dp[0]
        dp = [float('inf')] * (n+1)
	    dp[0] = 0
	    
	    # Iterate over all numbers from 1 to n
	    for i in range(1, n+1):
	        # Iterate over all perfect squares less <= i
	        for j in range(1, int(i**0.5)+1):
	            # Update dp[i]
	            dp[i] = min(dp[i], dp[i-j*j]+1)

	    return dp[n]