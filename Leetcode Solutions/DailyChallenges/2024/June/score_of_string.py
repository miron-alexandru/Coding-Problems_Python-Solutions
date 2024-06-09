# problem link: https://leetcode.com/problems/score-of-a-string/


# my solution:

class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0

        for i in range(len(s) - 1):
            summ = abs(ord(s[i]) - ord(s[i + 1]))
            score += summ

        return score