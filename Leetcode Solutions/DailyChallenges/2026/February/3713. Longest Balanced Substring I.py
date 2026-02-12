# problem link: https://leetcode.com/problems/longest-balanced-substring-i/


# Description:
"""
You are given a string s consisting of lowercase English letters.

A substring of s is called balanced if all distinct characters in the substring appear the same number of times.

Return the length of the longest balanced substring of s.

 

Example 1:

Input: s = "abbac"

Output: 4

Explanation:

The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.

Example 2:

Input: s = "zzabccy"

Output: 4

Explanation:

The longest balanced substring is "zabc" because the distinct characters 'z', 'a', 'b', and 'c' each appear exactly 1 time.

Example 3:

Input: s = "aba"

Output: 2

Explanation:
One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".
"""

# Solution:
class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            freq = [0] * 26
            distinct = 0
            maxFreq = 0

            for j in range(i, n):
                idx = ord(s[j]) - ord('a')

                if freq[idx] == 0:
                    distinct += 1

                freq[idx] += 1
                maxFreq = max(maxFreq, freq[idx])

                length = j - i + 1

                if length == distinct * maxFreq:
                    ans = max(ans, length)

        return ans