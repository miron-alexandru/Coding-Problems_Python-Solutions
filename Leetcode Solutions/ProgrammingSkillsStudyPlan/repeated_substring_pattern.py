# problem link: https://leetcode.com/problems/repeated-substring-pattern


# my solution:
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Get the length of the input string
        n = len(s)
        # Iterate over all possible substring lengths
        for i in range(1, n//2 + 1):
            # Check if we can repeat it to form the original string
            if n % i == 0:
                # Extract the substring of length i
                substring = s[:i]
                # Check if the substring can be repeated to form the original string
                if substring * (n//i) == s:
                    return True
        return False