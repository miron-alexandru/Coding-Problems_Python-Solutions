# problem link: https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/


# Description
"""
You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
Example 2:

Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= k <= 105
"""


# Solution:
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Find the maximum element in the array
        max_val = max(nums)

        left = 0            # Left pointer
        count = 0           # Count of max_val in the current window
        result = 0

        # Iterate through the array using right pointer
        for right in range(len(nums)):
            # If current element is equal to the max value increment the count
            if nums[right] == max_val:
                count += 1

            # When we have at least k occurrences of max_val in window
            while count >= k:
                # For each valid window, all subarrays starting from left to right
                # and ending at any index ≥ right are valid.
                # Since right is fixed all subarrays from left to len(nums) - 1 are valid.
                result += len(nums) - right

                # Shrink the window from the left to look for other valid windows
                if nums[left] == max_val:
                    count -= 1
                left += 1

        return result