# Problem Link: https://leetcode.com/problems/valid-palindrome/


# My Solution:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # remove non alphanum chars
        s = "".join(c for c in s if c.isalnum())
        return s == s[::-1]
