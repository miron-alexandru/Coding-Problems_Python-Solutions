# problem link: https://leetcode.com/problems/sign-of-the-product-of-an-array


# my solution:
# first solution, not so efficient because it iterates through the entire list to compute the product of all values
# which makes it slower for larger lists
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for num in nums:
            product *= num
        if product == 0:
            return 0
        else:
            return 1 if product > 0 else -1


# second solution, this has early stopping if a zero or negative value is encountered early in the list,
# the function can return immediately without needing to iterate through the rest of the list.
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                sign *= -1
        return sign
