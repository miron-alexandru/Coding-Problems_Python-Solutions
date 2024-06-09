# problem link: https://leetcode.com/problems/length-of-last-word/


# my solution:
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        words = s.split()
        
        if len(words) == 0:
            return 0
        
        return len(words[-1])