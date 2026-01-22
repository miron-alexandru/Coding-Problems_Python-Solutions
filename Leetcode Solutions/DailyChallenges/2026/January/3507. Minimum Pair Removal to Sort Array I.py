# problem link: https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/


# Description:
"""
Given an array nums, you can perform the following operation any number of times:

Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
Replace the pair with their sum.
Return the minimum number of operations needed to make the array non-decreasing.

An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).

 

Example 1:

Input: nums = [5,2,3,1]

Output: 2

Explanation:

The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
The array nums became non-decreasing in two operations.

Example 2:

Input: nums = [1,2,2]

Output: 0

Explanation:

The array nums is already sorted.
"""

# Solution:
class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        ops = 0
        
        while True:
            is_sorted = True
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    is_sorted = False
                    break
            
            if is_sorted:
                return ops
            
            min_sum = -1
            min_idx = -1
            
            for i in range(len(nums) - 1):
                current_sum = nums[i] + nums[i + 1]
                if min_idx == -1 or current_sum < min_sum:
                    min_sum = current_sum
                    min_idx = i
            
            nums[min_idx] = min_sum
            del nums[min_idx + 1]
            ops += 1
