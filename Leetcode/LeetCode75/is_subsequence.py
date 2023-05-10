# problem link: https://leetcode.com/problems/is-subsequence


# my solution:
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        k = 0
        while j < len(s) and k < len(t):
            # If curr chars in s and t match go to the next character in s
            if s[j] == t[k]:
                j += 1
            # move to the next char in t
            k += 1
        return j == len(s)
