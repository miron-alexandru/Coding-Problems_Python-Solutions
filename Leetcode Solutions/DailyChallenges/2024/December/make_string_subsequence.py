# problem link: https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/

# my solution:
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        # Pointers for both strings
        i, j = 0, 0
        
        while i < len(str1) and j < len(str2):
            # Check if characters are the same or incrementing cyclically
            if str1[i] == str2[j] or chr((ord(str1[i]) - ord('a') + 1) % 26 + ord('a')) == str2[j]:
                # Move to the next character in str2 if a match is found
                j += 1
            # Always move to the next character in str1
            i += 1

        return j == len(str2)
