# Problem Link: https://www.codewars.com/kata/52774a314c2333f0a7000688


# My Solution:
def valid_parentheses(string):
    stack = []
    for c in string:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack or stack[-1] != "(":
                return False
            stack.pop()
    return not stack
