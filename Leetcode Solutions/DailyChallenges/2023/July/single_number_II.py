# problem link: https://leetcode.com/problems/single-number-ii


# my solutions:

# Solution one:
# Straightforward
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for n in nums:
            if nums.count(n) < 3:
                return n


# Solution two:
# Using XOR
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        
        for num in nums:
            # Update "ones" to keep track of elements appearing once
            ones = (ones ^ num) & (~twos)
            
            # Update "twos" to keep track of elements appearing twice
            twos = (twos ^ num) & (~ones)
        
        return ones

# Solution three:
# Using counter
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        
        for num, count in counter.items():
            if count == 1:
                return num