# problem link: https://leetcode.com/problems/generate-parentheses/


# Description:
"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""


# Solution:

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(current, opened, closed):
            if len(current) == 2 * n:
                result.append(current)
                return

            if opened < n:
                backtrack(current + "(", opened + 1, closed)

            if closed < opened:
                backtrack(current + ")", opened, closed + 1)

        backtrack("", 0, 0)

        return result