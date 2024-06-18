# problem link: https://leetcode.com/problems/sum-of-square-numbers/



# my solution:
import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # Iterate over all possible values of a from 0 to the square root of c
        for a in range(int(math.isqrt(c)) + 1):
            # Calculate b_squared as the difference between c and the square of a
            b_squared = c - a * a
            # Calculate b as the integer square root of b_squared
            b = int(math.isqrt(b_squared))
            # Check if b_squared is a perfect square
            if b * b == b_squared:
                return True

        return False