# problem link: https://leetcode.com/problems/binary-search


# my solution:
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize left and right boundary of the search range
        low = 0
        high = len(nums) - 1
        while low <= high:
            # Calculate the middle index
            mid = (low + high) // 2
            # If the middle element is less than the target
            # update the left boundary to be 1 more than the middle index
            if nums[mid] < target:
                low = mid + 1
            # If the middle element is greater than the target
            # update the right boundary to be 1 less than the middle index
            elif nums[mid] > target:
                high = mid - 1
            else:
                # If middle element is the target, return middle index
                return mid
        # Target not found
        return -1
