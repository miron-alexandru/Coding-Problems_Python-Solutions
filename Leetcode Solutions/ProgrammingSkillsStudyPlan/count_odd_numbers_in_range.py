# problem link: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range


# my solution:
"""If low is odd, the count of odd numbers between low and high is the same as
the count of odd numbers between low + 1 and high.
If high is odd, the count of odd numbers between low and high is the same as
the count of odd numbers between low and high -1."""
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = (high - low) // 2
        if low % 2 == 1 or high % 2 == 1:
            count += 1

        return count