# problem link: https://leetcode.com/problems/roman-to-integer/

# my solution:
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0
        
        for c in reversed(s):
            curr_value = roman[c]
            
            if curr_value >= prev_value:
                result += curr_value
            else:
                result -= curr_value
            
            prev_value = curr_value
        
        return result