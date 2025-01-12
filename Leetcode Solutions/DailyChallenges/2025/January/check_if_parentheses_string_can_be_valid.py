# problem link: https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/


# my solution:
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # if length is odd; impossible to balance
        if len(s) % 2 != 0:
            return False
        
        n = len(s)
        
        # Left-to-Right pass
        balance = 0
        free = 0
        for i in range(n):
            if locked[i] == '1':
                balance += 1 if s[i] == '(' else -1
            else:
                free += 1
            # If locked ')' exceeds possible `(` from locked + free, invalid
            if balance + free < 0:
                return False
        
        # Right-to-Left pass
        balance = 0
        free = 0
        for i in range(n - 1, -1, -1):
            if locked[i] == '1':
                balance += 1 if s[i] == ')' else -1
            else:
                free += 1
            # If locked '(' exceeds possible `)` from locked + free, invalid
            if balance + free < 0:
                return False
        
        return True
