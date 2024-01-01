# problem link: https://leetcode.com/problems/repeated-substring-pattern/


# my solution:
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]