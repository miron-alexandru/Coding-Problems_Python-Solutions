# problem link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

# my solution:
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)