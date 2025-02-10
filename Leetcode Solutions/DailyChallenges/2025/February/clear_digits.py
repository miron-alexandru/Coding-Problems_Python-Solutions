# problem link: https://leetcode.com/problems/clear-digits/



# my solutions
#1
class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if not s[i].isnumeric():
                stack.append(s[i])
            else:
                stack.pop()

        return "".join(stack)



#2 
class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for char in s:
            if char.isdigit() and stack:
                stack.pop()
            elif not char.isdigit():
                stack.append(char)

        return "".join(stack)



#3
class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for char in s:
            stack.pop() if char.isdigit() and stack else stack.append(char)
        return "".join(stack)
