# problem link: https://leetcode.com/problems/rotate-string/


# my solution:
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in (s + s)