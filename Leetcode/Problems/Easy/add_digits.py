# problem link : https://leetcode.com/problems/add-digits/


# my solution:
class Solution:
    def addDigits(self, num: int) -> int:
        total = num
        while total >= 10:
            # Convert the integer to a str
            digits = [int(d) for d in str(total)]
            total = sum(digits)

        return total