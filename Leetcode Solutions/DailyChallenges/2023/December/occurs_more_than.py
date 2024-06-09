# problem link: https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array


# my solution:
from collections import Counter

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counts = Counter(arr)
        more_than = len(arr) * 0.25
        
        result = [num for num, count in counts.items() if count > more_than]

        if len(result) == 1:
            return result[0]
        else:
            return None