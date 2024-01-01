# problem link: https://leetcode.com/problems/find-the-highest-altitude/


# my solution:
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_alt, max_alt = 0, 0
        for i in gain:
            current_alt += i
            if current_alt > max_alt:
                max_alt = current_alt
        return max_alt