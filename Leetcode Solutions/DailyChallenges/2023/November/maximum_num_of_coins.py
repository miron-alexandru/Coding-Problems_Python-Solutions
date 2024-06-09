# problem link: https://leetcode.com/problems/maximum-number-of-coins-you-can-get


# my solution:
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        your_total = 0
        rounds = n // 3

        for i in range(rounds, n, 2):
            your_total += piles[i]

        return your_total