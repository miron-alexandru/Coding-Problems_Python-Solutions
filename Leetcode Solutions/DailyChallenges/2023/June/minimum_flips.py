# problem link: https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c


# my solution:
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0  # keep track of the needed flips
    
        while a or b or c:
            # Extract the least significant bit of a, b and c
            bit_a = a & 1 
            bit_b = b & 1
            bit_c = c & 1
            # Check if a flip is needed
            if (bit_a | bit_b) != bit_c:
                # If c's bit is 1, flip one of the bits
                if bit_c == 1:
                    flips += 1
                else:  # If c's bit is 0 flip both bits
                    flips += (bit_a + bit_b)
            # Shift a, b and c to the right by 1 bit discarding the least significant bit
            a >>= 1
            b >>= 1
            c >>= 1

        return flips