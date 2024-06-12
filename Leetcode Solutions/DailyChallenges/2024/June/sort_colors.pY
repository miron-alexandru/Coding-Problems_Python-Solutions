# problem link: https://leetcode.com/problems/sort-colors/


# my solution:
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
        