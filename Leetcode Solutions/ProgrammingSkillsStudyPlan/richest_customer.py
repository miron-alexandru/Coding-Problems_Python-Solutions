# problem link: https://leetcode.com/problems/richest-customer-wealth


# my solutions:
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for account in accounts:
            account_sum = sum(account)
            max_wealth = max(max_wealth, account_sum)
        return max_wealth


# second solution:
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = max(sum(account) for account in accounts)
        return max_wealth