# Problem Link: https://www.hackerrank.com/challenges/one-week-preparation-kit-balanced-brackets/problem


# My Solution:
def isBalanced(s):
    brackets = []

    for char in s:
        if char in ["(", "{", "["]:
            brackets.append(char)
        elif char in [")", "}", "]"]:
            if not brackets:
                return "NO"
            elif char == ")" and brackets[-1] == "(":
                brackets.pop()
            elif char == "}" and brackets[-1] == "{":
                brackets.pop()
            elif char == "]" and brackets[-1] == "[":
                brackets.pop()
            else:
                return "NO"
    if not brackets:
        return "YES"
    else:
        return "NO"
