# problem link: https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/



# my solution:
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Find the maximum element in the array
        max_num = max(nums)
        
        #Initialize variables to track the longest subarray with all elements equal to max_num
        longest = 0
        current_length = 0
        
        #Iterate through the array to find the longest contiguous subarray of max_num
        for num in nums:
            if num == max_num:
                current_length += 1
                longest = max(longest, current_length)
            else:
                current_length = 0  # Reset the current length when a non-max element is found
        
        #Return the longest length found
        return longest
