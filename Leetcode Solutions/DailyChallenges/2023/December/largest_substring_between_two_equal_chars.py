# problem link: https://leetcode.com/problems/largest-substring-between-two-equal-characters


# my solution:
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_indices = {}
        max_length = -1

        for i, char in enumerate(s):
            if char in char_indices:
                max_length = max(max_length, i - char_indices[char] - 1)
            else:
                char_indices[char] = i

        return max_length
