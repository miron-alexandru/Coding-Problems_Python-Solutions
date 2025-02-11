# problem link: https://leetcode.com/problems/remove-all-occurrences-of-a-substring



# my solution:
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # Keep removing the leftmost occurrence of part from s
        while part in s:
            s = s.replace(part, '', 1)  # Replace the first occurrence of part with an empty string
        return s
