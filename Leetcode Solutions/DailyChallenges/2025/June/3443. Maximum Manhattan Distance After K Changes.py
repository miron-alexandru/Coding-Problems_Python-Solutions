# problem link: https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/


# Description
"""
You are given a string s consisting of the characters 'N', 'S', 'E', and 'W', where s[i] indicates movements in an infinite grid:

'N' : Move north by 1 unit.
'S' : Move south by 1 unit.
'E' : Move east by 1 unit.
'W' : Move west by 1 unit.
Initially, you are at the origin (0, 0). You can change at most k characters to any of the four directions.

Find the maximum Manhattan distance from the origin that can be achieved at any time while performing the movements in order.

The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.
"""

# Solution:
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        def calc(primary: str, secondary: str) -> int:
            max_length = current_length = other_count = 0
            for direction in s:
                if direction == primary or direction == secondary:
                    current_length += 1
                elif other_count < k:
                    other_count += 1
                    current_length += 1
                else:
                    current_length -= 1
                max_length = max(max_length, current_length)
            return max_length

        option1 = calc("S", "E")
        option2 = calc("S", "W")
        option3 = calc("N", "E")
        option4 = calc("N", "W")
        return max(option1, option2, option3, option4)