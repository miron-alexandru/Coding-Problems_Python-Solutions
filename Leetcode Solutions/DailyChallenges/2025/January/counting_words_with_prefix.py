# problem link: https://leetcode.com/problems/counting-words-with-a-given-prefix/


# my solution:
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if word.startswith(pref):
                count += 1

        return count