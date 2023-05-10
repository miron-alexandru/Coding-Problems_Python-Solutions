# problem link: https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal


# my solution:
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = []

        if s1 == s2:
            return True

        # compare chars at each index in s1 and s2
        for i, (char1, char2) in enumerate(zip(s1, s2)):
            # if the characters are different, append the index to the diff list
            if char1 != char2:
                diff.append(i)
                # if more than two chars are different, it s not possible, return False
                if len(diff) > 2:
                    return False

        if len(diff) != 2:
            return False

        # get indices where chars are different
        j, k = diff[0], diff[1]

        # check if swapping the chars results in the strings being equal
        if s1[j] == s2[k] and s1[k] == s2[j]:
            return True

        return False
