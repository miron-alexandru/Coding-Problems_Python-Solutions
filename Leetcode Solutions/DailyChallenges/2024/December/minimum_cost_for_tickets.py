# problem link: https://leetcode.com/problems/minimum-cost-for-tickets/



# solution:
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day_set = set(days)
        # Maximum day we need to consider
        last_day = days[-1]
        # DP array to store the minimum cost up to each day
        dp = [0] * (last_day + 1)

        for i in range(1, last_day + 1):
            if i not in day_set:
                dp[i] = dp[i - 1]  # No travel on this day, cost remains the same
            else:
                # Calculate the cost for each ticket type
                cost1 = dp[i - 1] + costs[0]  # 1-day pass
                cost7 = dp[max(0, i - 7)] + costs[1]  # 7-day pass
                cost30 = dp[max(0, i - 30)] + costs[2]  # 30-day pass
                # Take the minimum of the three options
                dp[i] = min(cost1, cost7, cost30)

        return dp[last_day]
