# problem link: https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/


# Description:
"""
No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

Given an integer n, return a list of two integers [a, b] where:

a and b are No-Zero integers.
a + b = n
The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

 

Example 1:

Input: n = 2
Output: [1,1]
Explanation: Let a = 1 and b = 1.
Both a and b are no-zero integers, and a + b = 2 = n.
Example 2:

Input: n = 11
Output: [2,9]
Explanation: Let a = 2 and b = 9.
Both a and b are no-zero integers, and a + b = 11 = n.
Note that there are other valid answers as [8, 3] that can be accepted.
"""

# Solution:
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(1, n):
            b = n - a
            if '0' not in str(a) and '0' not in str(b):
                return [a, b]


# Second solution:
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def no_zero(x: int) -> bool:
            return '0' not in str(x)

        return next([a, n - a] for a in range(1, n) if no_zero(a) and no_zero(n - a))