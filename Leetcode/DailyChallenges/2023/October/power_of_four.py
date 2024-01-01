# problem link: https://leetcode.com/problems/power-of-four/


# my solution:
import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        i = math.log(n) / math.log(4)

        return i == math.floor(i)