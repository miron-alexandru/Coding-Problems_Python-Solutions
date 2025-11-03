# problem link: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/


# Description:
"""
Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.
"""

# Solution:
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0
        prev = 0  # index of the previous balloon kept
        
        for i in range(1, len(colors)):
            if colors[i] == colors[prev]:
                # Remove the one with smaller neededTime
                total_time += min(neededTime[i], neededTime[prev])
                # Keep the one with larger neededTime
                if neededTime[i] > neededTime[prev]:
                    prev = i
            else:
                prev = i
        
        return total_time
