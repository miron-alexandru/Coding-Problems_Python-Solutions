# problem link: https://leetcode.com/problems/sort-colors/


# description:
"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""

# Solution:
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize three pointers
        low, mid, high = 0, 0, len(nums) - 1
        
        # Traverse the array
        while mid <= high:
            if nums[mid] == 0:  # If the element is 0 (red)
                # Swap the elements at indices low and mid
                nums[low], nums[mid] = nums[mid], nums[low]
                # Increment both pointers
                low += 1
                mid += 1
            elif nums[mid] == 1:  # If the element is 1 (white)
                # move mid pointer
                mid += 1
            else:  # If the element is 2 (blue)
                # Swap the elements at indices mid and high
                nums[mid], nums[high] = nums[high], nums[mid]
                # Decrement the high pointer
                high -= 1
        