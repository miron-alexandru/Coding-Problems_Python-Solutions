# Problem Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/


# My Solution:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        chars = set()
        longest = 0
        left = right = 0

        while right < n:
            char = s[right]
            if char in chars:
                chars.remove(s[left])
                left += 1
            else:
                chars.add(char)
                longest = max(longest, right - left + 1)
                right += 1

        return longest
