# problem link: https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

# my solution:

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # XOR the two numbers to find the differing bits
        xor_result = start ^ goal
        # Count and return the number of 1s in the XOR result
        return bin(xor_result).count('1')
