# problem link: https://leetcode.com/problems/find-if-array-can-be-sorted


# solution (not mine):

from math import inf

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # Initialize previous maximum to negative infinity.
        previous_max = -inf
        # Initialize index and get the length of the list.
        i, n = 0, len(nums)
      
        # Iterate through the list of numbers.
        while i < n:
            # Initialize the next index and get the bit count of the current number.
            j = i + 1
            bit_count = bin(nums[i]).count('1')
            # Keep track of the minimum and maximum for the current bit count.
            current_min = current_max = nums[i]
          
            # Slide through the array to find consecutive numbers with the same bit count.
            while j < n and bin(nums[j]).count('1') == bit_count:
                current_min = min(current_min, nums[j])
                current_max = max(current_max, nums[j])
                j += 1
          
            # If the previous maximum number is greater than the current minimum,
            # the array cannot be sorted based on the conditions, hence return False.
            if previous_max > current_min:
                return False
            # Update previous maximum for the next iteration.
            previous_max = current_max
            # Move to the next segment with a different bit count.
            i = j
      
        # If we've reached this point, the array can be sorted, therefore return True.
        return True