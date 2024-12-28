# problem link: https://leetcode.com/problems/target-sum/


# my solution:
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}  # Initial state, we can make 0 with 1 way (using no numbers)
    
        for num in nums:
            next_dp = {}  # Temporary dictionary for the next state
            for sum_val in dp:
                # Add the number with a '+' or a '-'
                next_dp[sum_val + num] = next_dp.get(sum_val + num, 0) + dp[sum_val]
                next_dp[sum_val - num] = next_dp.get(sum_val - num, 0) + dp[sum_val]
            
            dp = next_dp  # Update dp to the new state
        
        return dp.get(target, 0)  # Return the count of ways to reach the target