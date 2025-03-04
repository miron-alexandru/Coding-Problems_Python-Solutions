# problem link: https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/



# my solution:
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            else:
                n //= 3
            
        return True
