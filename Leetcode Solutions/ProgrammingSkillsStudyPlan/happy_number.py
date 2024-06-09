# problem link: https://leetcode.com/problems/happy-number


# my solution:
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        # Repeat until result is a happy number or not happy
        while n != 1:
            # get digits of number
            digits = [int(d) for d in str(n)]
            # square each of them and add them up
            n = sum([d**2 for d in digits])
            # if result is the same, the number is not happy
            if n in seen:
                return False
            seen.add(n)

        # if n = 1, the number is happy
        return True
