# problem link: https://leetcode.com/problems/shifting-letters-ii/


# my solution:
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)
        
        # Apply the shifts to the difference array
        for start, end, direction in shifts:
            if direction == 1:  # Forward shift
                diff[start] += 1
                diff[end + 1] -= 1
            else:  # Backward shift
                diff[start] -= 1
                diff[end + 1] += 1
        
        # Calculate the cumulative shifts
        cumulative_shift = 0
        net_shifts = [0] * n
        for i in range(n):
            cumulative_shift += diff[i]
            net_shifts[i] = cumulative_shift
        
        # Apply the shifts to the string
        result = []
        for i in range(n):
            # Calculate the new character
            new_char = chr((ord(s[i]) - ord('a') + net_shifts[i]) % 26 + ord('a'))
            result.append(new_char)
        
        return ''.join(result)
