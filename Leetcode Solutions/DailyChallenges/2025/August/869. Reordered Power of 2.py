# problem link: https://leetcode.com/problems/reordered-power-of-2/



# Description:
"""
You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.

 

Example 1:

Input: n = 1
Output: true
Example 2:

Input: n = 10
Output: false
"""

# Solution:
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # Precompute all powers of two digit signatures
        powers = {"".join(sorted(str(1 << i))) for i in range(31)}
        return "".join(sorted(str(n))) in powers
