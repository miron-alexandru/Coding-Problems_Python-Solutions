# problem link: https://leetcode.com/problems/delete-characters-to-make-fancy-string/import requests


# my solution:

class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        # Track the number of consecutive occurrences of the current character
        count = 1
        
        # Start iterating from the second character
        for i in range(len(s)):
            # Check if the current character is the same as the previous one
            if i > 0 and s[i] == s[i - 1]:
                count += 1
            else:
                count = 1  # Reset count for a new character sequence
            
            # Add character if it does not create three consecutive identical characters
            if count < 3:
                result.append(s[i])

        return ''.join(result)