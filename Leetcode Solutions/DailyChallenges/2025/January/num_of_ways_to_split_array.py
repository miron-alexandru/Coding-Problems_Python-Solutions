# problem link: https://leetcode.com/problems/number-of-ways-to-split-array/


# my solution:
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # Calculate the total sum of the array
        total_sum = sum(nums)
        left_sum = 0
        valid_splits = 0
        
        # Iterate through the array up to the second-to-last element
        for i in range(len(nums) - 1):
            left_sum += nums[i]  # Update the sum of the left part
            right_sum = total_sum - left_sum  # Calculate the sum of the right part
            
            # Check the condition for a valid split
            if left_sum >= right_sum:
                valid_splits += 1
        
        return valid_splits