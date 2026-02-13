# problem link: https://leetcode.com/problems/longest-balanced-substring-ii/



# Description:
"""
You are given a string s consisting only of the characters 'a', 'b', and 'c'.

A substring of s is called balanced if all distinct characters in the substring appear the same number of times.

Return the length of the longest balanced substring of s.

 

Example 1:

Input: s = "abbac"

Output: 4

Explanation:

The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.

Example 2:

Input: s = "aabcc"

Output: 3

Explanation:

The longest balanced substring is "abc" because all distinct characters 'a', 'b' and 'c' each appear exactly 1 time.

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
        res = 0

        #Case 1
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            res = max(res, j - i)
            i = j

        # Helper for two characters
        def two_char(c1, c2):
            diff_index = {0: -1}
            diff = 0
            best = 0
            
            for i in range(n):
                if s[i] == c1:
                    diff += 1
                elif s[i] == c2:
                    diff -= 1
                else:
                    diff = 0
                    diff_index = {0: i}
                    continue

                if diff in diff_index:
                    best = max(best, i - diff_index[diff])
                else:
                    diff_index[diff] = i

            return best

        #Case 2
        res = max(res, two_char('a', 'b'))
        res = max(res, two_char('a', 'c'))
        res = max(res, two_char('b', 'c'))

        #Case 3
        prefix_map = {(0, 0): -1}
        count_a = count_b = count_c = 0
        
        for i in range(n):
            if s[i] == 'a':
                count_a += 1
            elif s[i] == 'b':
                count_b += 1
            else:
                count_c += 1

            key = (count_b - count_a, count_c - count_a)

            if key in prefix_map:
                res = max(res, i - prefix_map[key])
            else:
                prefix_map[key] = i

        return res
