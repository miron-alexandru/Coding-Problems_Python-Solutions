# problem link: https://leetcode.com/problems/count-of-matches-in-tournament


# my solution:
class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches_played = 0

        while n > 1:
            # number of teams is even
            if n % 2 == 0:
                matches_played += n // 2
                n //= 2
            # number of teams is odd
            else:
                matches_played += (n - 1) // 2
                n = (n - 1) // 2 + 1

        return matches_played