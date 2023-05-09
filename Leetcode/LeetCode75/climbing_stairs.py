# problem link: https://leetcode.com/problems/climbing-stairs/

# my solution:
class Solution:
    def climbStairs(self, n: int) -> int:
    	# If n is 0 or 1, there is only one way to climb the stairs
        if n <= 1:
            return 1
        first, second = 1, 1
        # Calculate the number of ways to climb
        for i in range(2, n + 1):
        	# the number of ways to climb n stairs is the sum of the number of ways to climb n-1 stairs and n-2 stairs
            third = first + second
            # update the number of ways to climb n-2 stairs to the number of ways to climb n-1 stairs
            first = second
            # update the number of ways to climb n-1 stairs to the number of ways to climb n stairs
            second = third
        return second   # return the number of ways to climb n stairs
