# problem link: https://leetcode.com/problems/reverse-bits/


# my solution:
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        # Loop through all 32 bits of the input integer
        for i in range(32):
            # Shift the result integer to the left by 1 bit to make space for the next bit
            res <<= 1
            # Use the bitwise OR operator to set the current bit of the result to the current bit of the input integer
            res |= n & 1

            # Shift the input integer to the right by 1 bit to move to the next bit
            n >>= 1

        return res
