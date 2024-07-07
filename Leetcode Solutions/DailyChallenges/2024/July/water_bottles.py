# problem link: https://leetcode.com/problems/water-bottles/


# my solution:
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_bottles = numBottles
        empty_bottles = numBottles

        while empty_bottles >= numExchange:
            new_bottles = empty_bottles // numExchange
            total_bottles += new_bottles
            empty_bottles = empty_bottles - (new_bottles * numExchange) + new_bottles

        return total_bottles