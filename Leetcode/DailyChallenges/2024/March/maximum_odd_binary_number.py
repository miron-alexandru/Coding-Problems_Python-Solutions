# problem link: https://leetcode.com/problems/maximum-odd-binary-number/



# my solution:
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_ones = s.count('1')
    
        # Calculate the number of zeros in the string
        count_zeros = len(s) - count_ones
        
        # Calculate the number of ones required in the result
        count_ones_result = count_ones - 1
        
        # Construct the resulting string
        result = '1' * count_ones_result + '0' * count_zeros + '1'
        
        return result