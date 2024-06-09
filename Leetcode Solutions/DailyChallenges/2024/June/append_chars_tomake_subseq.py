# problem link: https://leetcode.com/problems/append-characters-to-string-to-make-subsequence


# my solution:
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_ptr, t_ptr = 0, 0
    
        while s_ptr < len(s) and t_ptr < len(t):
            if s[s_ptr] == t[t_ptr]:
                t_ptr += 1
            s_ptr += 1

        if t_ptr == len(t):
            return 0

        return len(t) - t_ptr
