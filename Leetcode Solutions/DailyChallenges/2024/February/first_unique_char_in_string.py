# problem link: https://leetcode.com/problems/first-unique-character-in-a-string


# my solution:
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        # keep count of each char
        for char in s:
            count[char] = count.get(char, 0) + 1
        # get the first char with count 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1