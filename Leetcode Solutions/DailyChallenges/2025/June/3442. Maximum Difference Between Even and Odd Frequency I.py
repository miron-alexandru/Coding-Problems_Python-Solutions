# problem link: https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/


# description:
"""
You are given a string s consisting of lowercase English letters.

Your task is to find the maximum difference diff = freq(a1) - freq(a2) between the frequency of characters a1 and a2 in the string such that:

a1 has an odd frequency in the string.
a2 has an even frequency in the string.
Return this maximum difference.

 

Example 1:

Input: s = "aaaaabbc"

Output: 3

Explanation:

The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
The maximum difference is 5 - 2 = 3.
Example 2:

Input: s = "abcabcab"

Output: 1

Explanation:

The character 'a' has an odd frequency of 3, and 'c' has an even frequency of 2.
The maximum difference is 3 - 2 = 1.
"""

# Solutions:
# 1.
class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s).values()
        odd_freq = [f for f in freq if f % 2 == 1]
        even_freq = [f for f in freq if f % 2 == 0]

        if not odd_freq or not even_freq:
            return -1

        return max(o - e for o in odd_freq for e in even_freq)



# 2.
class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        odd_freq = []
        even_freq = []
        result = float('-inf')

        for key, value in freq.items():
            if value % 2 == 0:
                even_freq.append(value)
            else:
                odd_freq.append(value)

        for i in odd_freq:
            for j in even_freq:
                diff = i - j
                if diff > result:
                    result = diff

        return result if result != float('-inf') else -1
