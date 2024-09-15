# problem link: https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/


# my solution:
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Map vowels to specific bits
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        
        # Initialize bitmask and the dictionary to store first occurrence of each bitmask
        bitmask = 0
        first_occurrence = {0: -1}
        max_length = 0
        
        # Iterate through the string
        for i, char in enumerate(s):
            if char in vowels:
                # Flip the corresponding bit for the vowel
                bitmask ^= (1 << vowels[char])
            
            # Check if this bitmask has been seen before
            if bitmask in first_occurrence:
                # Calculate the length of the substring
                max_length = max(max_length, i - first_occurrence[bitmask])
            else:
                # Store the first occurrence of this bitmask
                first_occurrence[bitmask] = i
        
        return max_length
