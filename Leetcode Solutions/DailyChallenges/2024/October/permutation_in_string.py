# problem link: https://leetcode.com/problems/permutation-in-string/


# my solution:
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Helper function to get the frequency count of characters in a string
        def get_char_frequency(s):
            frequency = [0] * 26
            for char in s:
                frequency[ord(char) - ord('a')] += 1  # Convert char to its index in alphabet
            return frequency

        if len(s1) > len(s2):
            return False

        s1_freq = get_char_frequency(s1)
        
        # Frequency count of the first window in s2 (substring of length len(s1))
        window_freq = get_char_frequency(s2[:len(s1)])
        
        # Check if the first window matches the frequency of s1
        if s1_freq == window_freq:
            return True
        
        # Start sliding the window from left to right over the rest of s2
        for i in range(len(s1), len(s2)):
            # Remove the character that's sliding out of the window (left side of the window)
            left_char = s2[i - len(s1)]
            window_freq[ord(left_char) - ord('a')] -= 1  # Decrease its frequency
            
            # Add the character that's sliding into the window (right side of the window)
            right_char = s2[i]
            window_freq[ord(right_char) - ord('a')] += 1  # Increase its frequency
            
            # Check if the updated window matches the frequency of s1
            if window_freq == s1_freq:
                return True

        return False
