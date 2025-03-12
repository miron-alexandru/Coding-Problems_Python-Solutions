# problem link: https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/


# my solution:
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negatives = 0
        positives = 0
        
        for n in nums:
            if n < 0:
                negatives += 1
            elif n > 0:
                positives += 1
    
        return max(negatives, positives)


# using binary search:

from bisect import bisect_left

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Find the index of the first non-negative number using binary search
        index_of_first_non_negative = bisect_left(nums, 0)
        
        # Count of negative numbers is simply the index of the first non-negative number
        negatives = index_of_first_non_negative
        
        # Count of positive numbers is the remaining numbers after index_of_first_non_negative
        positives = len(nums) - negatives - nums.count(0)  # Subtract zeros from the total
        
        # Return the maximum count of negatives or positives
        return max(negatives, positives)
