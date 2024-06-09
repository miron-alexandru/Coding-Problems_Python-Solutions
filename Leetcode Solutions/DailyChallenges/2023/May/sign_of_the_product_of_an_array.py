# problem link: https://leetcode.com/problems/sign-of-the-product-of-an-array/


# my solution:
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                sign *= -1
        return sign
