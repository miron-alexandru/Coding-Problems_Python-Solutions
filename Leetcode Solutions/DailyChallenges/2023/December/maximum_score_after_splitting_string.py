# problem link: https://leetcode.com/problems/maximum-score-after-splitting-a-string


# my solution:
class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        ones = s.count('1')
        zeros = 0

        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1

            current_score = zeros + ones
            max_score = max(max_score, current_score)

        return max_score