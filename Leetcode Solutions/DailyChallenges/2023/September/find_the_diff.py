# problem link: https://leetcode.com/problems/find-the-difference


# my solution:
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Initialize a counter
        counter = [0] * 26
        
        # Count characters in t
        for c in t:
            counter[ord(c) - ord('a')] += 1
        
        # Decrement the count for characters in s
        for c in s:
            counter[ord(c) - ord('a')] -= 1
        
        # Find the character with a count of 1 in t
        for i, count in enumerate(counter):
            if count == 1:
                return chr(i + ord('a'))
        
        return ''