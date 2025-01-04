# problem link: https://leetcode.com/problems/unique-length-3-palindromic-subsequences/


# my solution:
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Track the first and last occurrence of each character
        first_occurrence = {}
        last_occurrence = {}
        
        for i, char in enumerate(s):
            if char not in first_occurrence:
                first_occurrence[char] = i
            last_occurrence[char] = i
        
        # Count unique palindromes of length 3
        unique_palindromes = 0
        for char in first_occurrence:
            if last_occurrence[char] > first_occurrence[char]:
                # Get the substring between first and last occurrence
                start = first_occurrence[char] + 1
                end = last_occurrence[char]
                # Count unique characters in this range
                unique_middle_chars = set(s[start:end])
                unique_palindromes += len(unique_middle_chars)
        
        return unique_palindromes
