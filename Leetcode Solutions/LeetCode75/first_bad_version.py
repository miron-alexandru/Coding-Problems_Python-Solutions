# problem link: https://leetcode.com/problems/first-bad-version


# my solution:
class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Initialize left and right to first and last ver
        left = 1
        right = n

        while left < right:
            # Calculate middle ver number
            mid = (left + right) // 2
            # If middle is bad search for the left half
            if isBadVersion(mid):
                right = mid
            # If middle is good search for the right half
            else:
                left = mid + 1

        return left
