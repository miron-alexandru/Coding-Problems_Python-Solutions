# problem link: https://leetcode.com/problems/buy-two-chocolates



# my solutions:

#with sorting:

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices = sorted(prices)
        cheapest_chocos = prices[0] + prices[1]

        if money >= cheapest_chocos:
            return money - cheapest_chocos
        return money



# without sorting
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = min(prices)
        prices.remove(min1)
        min2 = min(prices)

        cheapest_chocos = min1 + min2

        if money >= cheapest_chocos:
            return money - cheapest_chocos
        return money