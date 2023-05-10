# Problem Link: https://leetcode.com/problems/power-of-three/


# My Solution:
import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # use recurion
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 3 != 0:
            return False

        return self.isPowerOfThree(n // 3)
