# problem link: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/


# solution:
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_seen = [-1, -1, -1]  # To store last index of 'a', 'b', and 'c'
        count = 0
        
        for i, char in enumerate(s):
            last_seen[ord(char) - ord('a')] = i  # Update last index of 'a', 'b', or 'c'
            count += min(last_seen) + 1  # Valid substrings end at i
        
        return count
