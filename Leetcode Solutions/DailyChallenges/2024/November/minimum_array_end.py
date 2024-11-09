# problem link: https://leetcode.com/problems/minimum-array-end/


# solution (not mine):
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1  # Adjust n to account for zero-based indexing
        ans = x  # Start with x as the base

        for i in range(31):  # Iterate through the first 31 bits
            if (x >> i & 1) ^ 1:  # Check if the i-th bit of x is 0
                ans |= (n & 1) << i  # Set the i-th bit of ans if n's bit is 1
                n >>= 1  # Shift n to process the next bit

        ans |= n << 31  # Append any remaining bits of n shifted to the left
        return ans
