# problem link: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer

# my solution:
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        summ = 0
        for i in str(n):
            dig = int(i)
            prod *= dig
            summ += dig
        return prod - summ