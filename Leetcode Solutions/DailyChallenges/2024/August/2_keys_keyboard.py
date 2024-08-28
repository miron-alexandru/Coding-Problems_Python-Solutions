# problem link: https://leetcode.com/problems/2-keys-keyboard/description/


# my solution:
class Solution:
    def minSteps(self, n: int) -> int:
        op = 0
        factor = 2

        while n > 1:
            while n % factor == 0:
                op += factor
                n //= factor
            factor += 1
        
        return op