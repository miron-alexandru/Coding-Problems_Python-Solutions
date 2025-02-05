# problem link: https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/



# my solution:
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        # Find the indices where the characters are different
        differences = [(i, s1[i], s2[i]) for i in range(len(s1)) if s1[i] != s2[i]]

        # Check if the number of differences is exactly 2
        if len(differences) != 2:
            return False

        # Check if swapping makes the strings equal
        (i1, c1_s1, c1_s2), (i2, c2_s1, c2_s2) = differences
        return c1_s1 == c2_s2 and c2_s1 == c1_s2