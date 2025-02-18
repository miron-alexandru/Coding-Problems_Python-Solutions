# problem link: https://leetcode.com/problems/construct-smallest-number-from-di-string/



# my solution:
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        result = ""
        for i in range(len(pattern) + 1):
            stack.append(str(i + 1))  # Push the next available digit
            if i == len(pattern) or pattern[i] == 'I':
                while stack:
                    result += stack.pop()  # Pop elements in reverse order for 'D'
        return result
