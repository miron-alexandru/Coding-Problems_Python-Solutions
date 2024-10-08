# problem link: https://leetcode.com/problems/minimum-string-length-after-removing-substrings/


# my solution:
class Solution:
    def minLength(self, s: str) -> int:
        # Initialize an empty stack
        stack = []
        
        # Traverse each character in the string
        for char in s:
            # If the current character and the last character in the stack form "AB" or "CD", remove them
            if stack and ((stack[-1] == 'A' and char == 'B') or (stack[-1] == 'C' and char == 'D')):
                stack.pop()  # Remove the last character from the stack
            else:
                stack.append(char)  # Otherwise, push the current character to the stack
        
        # The remaining characters in the stack form the final string
        return len(stack)
