# problem link: https://leetcode.com/problems/minimum-increment-to-make-array-unique



# my solution:
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        num_moves = 0

        for i in range(1, len(nums)):
            # Check if the current element is not greater than the previous element
            if nums[i] <= nums[i-1]:
                # Calculate the increment needed to make nums[i] unique
                increment = nums[i-1] + 1 - nums[i]
                # Update nums[i] to the new unique value and add the increment to the total number of moves
                nums[i] = nums[i-1] + 1
                num_moves += increment

        return num_moves
