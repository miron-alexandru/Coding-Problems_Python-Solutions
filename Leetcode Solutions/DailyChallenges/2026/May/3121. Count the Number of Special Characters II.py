# problem link: https://leetcode.com/problems/count-the-number-of-special-characters-ii/

# Description:
"""
You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.

Return the number of special letters in word.

 

Example 1:

Input: word = "aaAbcBC"

Output: 3

Explanation:

The special characters are 'a', 'b', and 'c'.

Example 2:

Input: word = "abc"

Output: 0

Explanation:

There are no special characters in word.

Example 3:

Input: word = "AbBCab"

Output: 0

Explanation:

There are no special characters in word."""

# Solution:
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_last = {}
        upper_first = {}

        for i, ch in enumerate(word):
            if ch.islower():
                lower_last[ch] = i
            else:
                c = ch.lower()
                if c not in upper_first:
                    upper_first[c] = i

        count = 0

        for c in lower_last:
            if c in upper_first and lower_last[c] < upper_first[c]:
                count += 1

        return count