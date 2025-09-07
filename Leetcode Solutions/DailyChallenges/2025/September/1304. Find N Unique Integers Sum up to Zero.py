# problem link: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/



# Description:
"""
Given an integer n, return any array containing n unique integers such that they add up to 0.

 

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]."""


# SOlution:
class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        # Add symmetric pairs i, -i so they cancel out
        for i in range(1, n // 2 + 1):
            res.append(i)
            res.append(-i)
        # If n is odd include 0 to balance the sum
        if n % 2 == 1:
            res.append(0)
        return res
