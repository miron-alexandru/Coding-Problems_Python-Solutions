# problem link: https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/


# Description:
"""
You are given an integer array nums of size n.

Consider a non-empty subarray from nums that has the maximum possible bitwise AND.

In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
Return the length of the longest such subarray.

The bitwise AND of an array is the bitwise AND of all the numbers in it.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,3,3,2,2]
Output: 2
Explanation:
The maximum possible bitwise AND of a subarray is 3.
The longest subarray with that value is [3,3], so we return 2.
Example 2:

Input: nums = [1,2,3,4]
Output: 1
Explanation:
The maximum possible bitwise AND of a subarray is 4.
The longest subarray with that value is [4], so we return 1.
"""

# Solution:
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
