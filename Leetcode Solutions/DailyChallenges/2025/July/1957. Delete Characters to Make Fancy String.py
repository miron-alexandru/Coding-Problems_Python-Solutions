# problem link: https://leetcode.com/problems/delete-characters-to-make-fancy-string/


# Description:
"""
A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.

 

Example 1:

Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".
Example 2:

Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".
Example 3:

Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".
."""

# Solution:
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