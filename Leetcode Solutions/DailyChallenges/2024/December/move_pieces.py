# problem link: https://leetcode.com/problems/move-pieces-to-obtain-a-string/



# my solution:
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Remove all underscores and compare character sequence
        if start.replace('_', '') != target.replace('_', ''):
            return False
        
        # Check positional constraints for 'L' and 'R'
        i = j = 0
        n = len(start)
        
        while i < n and j < n:
            # Move i and j to the next 'L' or 'R'
            while i < n and start[i] == '_':
                i += 1
            while j < n and target[j] == '_':
                j += 1
            
            # If both reached the end they are matching
            if i == n and j == n:
                return True
            
            # If one reached the end but the other did not
            if i == n or j == n:
                return False
            
            # Check if characters match
            if start[i] != target[j]:
                return False
            
            # Verify 'L' and 'R' positions
            if start[i] == 'L' and i < j:
                return False  # 'L' cannot move right
            if start[i] == 'R' and i > j:
                return False  # 'R' cannot move left
            
            # Move to the next character
            i += 1
            j += 1
        
        return True
