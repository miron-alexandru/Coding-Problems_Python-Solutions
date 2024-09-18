# problem link: https://leetcode.com/problems/largest-number/


# my solution;
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x: str, y: str) -> int:
            # Custom comparator to decide the order of two numbers
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        # Convert integers to strings for comparison
        nums_str = list(map(str, nums))
        
        # Sort the numbers based on the custom comparator
        nums_str.sort(key=cmp_to_key(compare))
        
        # Join the numbers to form the largest number
        largest_num = ''.join(nums_str)
        
        # Handle the case where all numbers are zero
        if largest_num[0] == '0':
            return '0'
        
        return largest_num
