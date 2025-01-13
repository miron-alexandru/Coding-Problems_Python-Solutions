# problem link: https://leetcode.com/problems/minimum-length-of-string-after-operations/



# my solution:
from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        counter = Counter(s)
        return sum(1 if x & 1 else 2 for x in counter.values())