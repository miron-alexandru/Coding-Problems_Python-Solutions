# problem link: https://leetcode.com/problems/count-the-number-of-consistent-strings/


# my solution:

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)  

        count = 0

        for word in words:
            if all(char in allowed_set for char in word):
                count += 1

        return count
