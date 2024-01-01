# problem link: https://leetcode.com/problems/coin-change-ii/


# my solution:
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Store the number of combinations for each amount in a list
        dp = [0] * (amount + 1)
        # There's only one way to make amount 0 (no coins)
        dp[0] = 1

        # Loop through each coin denomination
        for coin in coins:
            # For each coin denomination update the dp array for amounts from coin to the target amount
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]