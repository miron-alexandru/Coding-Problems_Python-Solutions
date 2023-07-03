# problem link: https://leetcode.com/problems/buddy-strings/


# my solution:
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # Check if lengths are different or if the sets of characters are different
        if len(s) != len(goal) or set(s) != set(goal):
            return False

        # Check if the strings are already equal
        if s == goal:
            # Check if there are at least two repeated characters
            return len(s) - len(set(s)) >= 1

        # Find the differing characters between s and goal
        diffs = [(a, b) for a, b in zip(s, goal) if a != b]

        # Check if more than two characters differ
        if len(diffs) != 2:
            return False

        # Check if the characters at the differing indices can be swapped
        return diffs[0] == diffs[1][::-1]