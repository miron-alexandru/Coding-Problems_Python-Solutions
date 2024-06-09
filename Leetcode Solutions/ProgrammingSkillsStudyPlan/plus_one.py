# problem link: https://leetcode.com/problems/plus-one


# my solution:
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1
        for i in range(n-1, -1, -1):
            digits[i] += carry
            if digits[i] == 10:
                digits[i] = 0
                carry = 1
            else:
                carry = 0
        if carry == 1:
            digits = [1] + digits
        return digits
