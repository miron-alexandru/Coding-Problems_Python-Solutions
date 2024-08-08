# problem link: https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii


# my solution:
from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count the frequency of each character in the string `word`
        char_count = Counter(word)
        
        # Initialize the total number of pushes needed
        minimum_pushes = 0
        
        # Sort the counts of characters in descending order
        sorted_counts = sorted(char_count.values(), reverse=True)
    
        # Iterate over the sorted counts
        for index, count in enumerate(sorted_counts):
            # Calculate the number of pushes needed for each character
            # (index // 8) gives the "page" number, and adding 1 represents the number of pushes for that page
            minimum_pushes += ((index // 8) + 1) * count
      
        return minimum_pushes
