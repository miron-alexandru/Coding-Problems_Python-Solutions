




# my solutions:

#solution 1:
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []

        for char in s:
            if char != '#':
                s_stack.append(char)
            elif s_stack:
                s_stack.pop()
        
        for char in t:
            if char != '#':
                t_stack.append(char)
            elif t_stack:
                t_stack.pop()
    
        if len(s_stack) != len(t_stack):
            return False

        while s_stack and t_stack:
            if s_stack.pop() != t_stack.pop():
                return False

        return True

        

#solution two:

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(string):
            stack = []
            for char in string:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            return stack
        
        return process_string(s) == process_string(t)
