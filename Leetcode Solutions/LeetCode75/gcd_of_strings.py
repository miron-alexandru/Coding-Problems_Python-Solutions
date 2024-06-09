# problem link: https://leetcode.com/problems/greatest-common-divisor-of-strings


# my solution:
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        gcd_length = self.get_gcd_length(len(str1), len(str2))
        return str1[:gcd_length]

    def get_gcd_length(self, a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return a