# Problem Link: https://leetcode.com/problems/reverse-string/


# My Solution:
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = "".join(reversed(s))
