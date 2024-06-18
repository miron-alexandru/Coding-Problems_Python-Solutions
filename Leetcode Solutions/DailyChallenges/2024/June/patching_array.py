# problem link: https://leetcode.com/problems/patching-array


# my solution:
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # Initialize the number of patches needed to 0
        patches = 0
        # Initialize the smallest number that cannot be formed to 1
        miss = 1
        # Initialize the index to iterate over the nums array
        i = 0
        
        # Continue until we can form all numbers up to n
        while miss <= n:
            # If the current number in nums is less than or equal to miss,
            # it means we can use it to extend the range of numbers we can form
            if i < len(nums) and nums[i] <= miss:
                # Add nums[i] to the range, so miss is updated to miss + nums[i]
                miss += nums[i]
                # Move to the next element in nums
                i += 1
            else:
                # If the current number in nums is greater than miss,
                # we need to patch the array by adding miss itself
                miss += miss
                # Increment the number of patches needed
                patches += 1

        return patches
