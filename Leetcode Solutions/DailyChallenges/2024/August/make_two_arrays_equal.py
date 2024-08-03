# problem link: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/


# my solution:

from collections import Counter

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)