# problem link: https://leetcode.com/problems/smallest-number-with-all-set-bits/



# Description:
"""
You are given a positive number n.

Return the smallest number x greater than or equal to n, such that the binary representation of x contains only set bits

 

Example 1:

Input: n = 5

Output: 7

Explanation:

The binary representation of 7 is "111".

Example 2:

Input: n = 10

Output: 15

Explanation:

The binary representation of 15 is "1111".

Example 3:

Input: n = 3

Output: 3

Explanation:

The binary representation of 3 is "11".
"""

# Solution:
class Solution:
    def smallestNumber(self, n: int) -> int:
        # check if n already has all bits set
        if (n & (n + 1)) == 0:
            return n
        # shifts 1 left by that count giving the next power of two.
        next_power = 1 << n.bit_length()
        # subtract 1 to get all bits set below that power
        return next_power - 1
