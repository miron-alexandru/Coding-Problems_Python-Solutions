# Problem Link: https://leetcode.com/problems/generate-parentheses/


# My Solution:
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = [(0, 0, "")]

        while stack:
            open_para, close_para, cur_str = stack.pop()
            if open_para == n and close_para == n:
                result.append(cur_str)
            if open_para < n:
                stack.append((open_para + 1, close_para, cur_str + "("))
            if close_para < open_para:
                stack.append((open_para, close_para + 1, cur_str + ")"))
        return result
