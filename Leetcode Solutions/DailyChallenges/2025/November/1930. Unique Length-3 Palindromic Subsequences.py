# problem link: https://leetcode.com/problems/unique-length-3-palindromic-subsequences/


# Description:
"""
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")
Example 2:

Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".
Example 3:

Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")
"""


# Solution:
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
