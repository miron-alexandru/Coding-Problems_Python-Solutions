# problem link: https://leetcode.com/problems/maximize-the-confusion-of-an-exam/



# my solution:
# Using the sliding window algorithm
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0
        right = 0
        maxConsecutive = 0
        maxCount = 0
        counts = {'T': 0, 'F': 0}

        while right < len(answerKey):
            counts[answerKey[right]] += 1
            maxCount = max(maxCount, counts[answerKey[right]])

            if (right - left + 1) - maxCount > k:
                counts[answerKey[left]] -= 1
                left += 1

            maxConsecutive = max(maxConsecutive, right - left + 1)
            right += 1

        return maxConsecutive