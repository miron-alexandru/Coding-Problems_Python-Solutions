# problem link: https://leetcode.com/problems/is-subsequence


# my solution:
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        for char in t:
            if j < len(s) and char == s[j]:
                j += 1
        return j == len(s)
