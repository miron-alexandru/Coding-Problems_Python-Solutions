# problem link: https://leetcode.com/problems/find-the-highest-altitude


# my solutions:
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        current_alt = 0
        
        for g in gain:
            current_alt += g
            max_alt = max(max_alt, current_alt)
        
        return max_alt

# using itertools
import itertools

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = list(itertools.accumulate(gain, initial=0))
        return max(altitudes)
