# problem link: https://leetcode.com/problems/count-number-of-homogenous-substrings


# my solution:
class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        count = 1
        result = 0

        for i in range(1, len(s)):
            # Check if the current character is the same as the previous
            if s[i] == s[i - 1]:
                count += 1
            else:
                # Calculate the number of homogenous substrings for the previous character and add it to the result
                result = (result + count * (count + 1) // 2) % MOD
                # Reset count for the new character
                count = 1

        # Calculate for the last character
        result = (result + count * (count + 1) // 2) % MOD

        return result
