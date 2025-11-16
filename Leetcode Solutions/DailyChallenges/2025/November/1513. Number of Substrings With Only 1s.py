# problem link: https://leetcode.com/problems/number-of-substrings-with-only-1s/


# Description:
"""
Given a binary string s, return the number of substrings with all characters 1's. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: s = "0110111"
Output: 9
Explanation: There are 9 substring in total with only 1's characters.
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.
Example 2:

Input: s = "101"
Output: 2
Explanation: Substring "1" is shown 2 times in s.
Example 3:

Input: s = "111111"
Output: 21
Explanation: Each substring contains only 1's characters.
"""

# Solution:
class Solution:
    def numSub(self, s: str) -> int:
        mod = 10**9 + 7
        run = 0       # current streak of consecutive 1s
        total = 0     # result accumulator

        for c in s:
            if c == '1':
                # extend the current streak
                run += 1
            else:
                # end of a streak, add its contribution
                total += run * (run + 1) // 2
                run = 0

        # add the last streak if the string ends with 1s
        total += run * (run + 1) // 2

        return total % mod
