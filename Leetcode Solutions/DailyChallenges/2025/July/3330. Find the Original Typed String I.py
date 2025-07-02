# problem link: https://leetcode.com/problems/find-the-original-typed-string-i/


# Description
"""
Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.

Although Alice tried to focus on her typing, she is aware that she may still have done this at most once.

You are given a string word, which represents the final output displayed on Alice's screen.

Return the total number of possible original strings that Alice might have intended to type.

 

Example 1:

Input: word = "abbcccc"

Output: 5

Explanation:

The possible strings are: "abbcccc", "abbccc", "abbcc", "abbc", and "abcccc".

Example 2:

Input: word = "abcd"

Output: 1

Explanation:

The only possible string is "abcd".

Example 3:

Input: word = "aaaa"

Output: 4
."""

# Solution:
class Solution:
    def possibleStringCount(self, word: str) -> int:
        if not word:
            return 1

        groups = []
        prev_char = word[0]
        count = 1

        # Group consecutive characters
        for i in range(1, len(word)):
            if word[i] == prev_char:
                count += 1
            else:
                groups.append((prev_char, count))
                prev_char = word[i]
                count = 1
        groups.append((prev_char, count))

        # Calculate the total number of possible original strings
        total = 1

        for char, count in groups:
            if count > 1:
                total += (count - 1)

        return total

# Second:
class Solution:
    def possibleStringCount(self, word: str) -> int:
        groups = [(char, sum(1 for _ in group)) for char, group in groupby(word)]
    
        # The total is the original string + all reductions from each group
        total = 1 + sum(count - 1 for _, count in groups if count > 1)
        
        return total