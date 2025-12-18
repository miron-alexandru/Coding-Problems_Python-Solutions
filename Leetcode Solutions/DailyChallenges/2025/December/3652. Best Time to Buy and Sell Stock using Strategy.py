# problem link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/


# Description:
"""
You are given two integer arrays prices and strategy, where:

prices[i] is the price of a given stock on the ith day.
strategy[i] represents a trading action on the ith day, where:
-1 indicates buying one unit of the stock.
0 indicates holding the stock.
1 indicates selling one unit of the stock.
You are also given an even integer k, and may perform at most one modification to strategy. A modification consists of:

Selecting exactly k consecutive elements in strategy.
Set the first k / 2 elements to 0 (hold).
Set the last k / 2 elements to 1 (sell).
The profit is defined as the sum of strategy[i] * prices[i] across all days.

Return the maximum possible profit you can achieve.

Note: There are no constraints on budget or stock ownership, so all buy and sell operations are feasible regardless of past actions.
"""

# Solution:
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        base = 0
        for i in range(n):
            base += strategy[i] * prices[i]

        pref_price = [0] * (n + 1)
        pref_profit = [0] * (n + 1)

        for i in range(n):
            pref_price[i + 1] = pref_price[i] + prices[i]
            pref_profit[i + 1] = pref_profit[i] + strategy[i] * prices[i]

        best = base
        half = k // 2

        for l in range(n - k + 1):
            m = l + half
            r = l + k

            old = pref_profit[r] - pref_profit[l]
            new = pref_price[r] - pref_price[m]

            total = base - old + new
            if total > best:
                best = total

        return best