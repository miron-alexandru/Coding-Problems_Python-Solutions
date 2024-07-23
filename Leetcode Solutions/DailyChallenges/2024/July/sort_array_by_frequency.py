# problem link: https://leetcode.com/problems/sort-array-by-increasing-frequency/


# my solution:
from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = Counter(nums)
        sorted_elements = sorted(frequency.items(), key=lambda x: (x[1], -x[0]))

        result = []
        for value, freq in sorted_elements:
            result.extend([value] * freq)
        
        return result