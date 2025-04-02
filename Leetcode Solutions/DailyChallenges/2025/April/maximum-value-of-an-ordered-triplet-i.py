# problem link: https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/



# my solution:
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_value = 0
        max_so_far = 0
        max_difference = 0
        
        for num in nums:
            max_value = max(max_value, max_difference * num)  # Compute the triplet value
            max_difference = max(max_difference, max_so_far - num)  # Update max difference
            max_so_far = max(max_so_far, num)  # Update max seen so far
        
        return max_value