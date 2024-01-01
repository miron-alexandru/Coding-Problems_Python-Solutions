# problem link: https://leetcode.com/problems/peak-index-in-a-mountain-array


# My solution:
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # Initialize left and right pointers
        left, right = 0, len(arr) - 1

        while left < right:
            # Calculate the middle index
            mid = left + (right - left) // 2

            if arr[mid] < arr[mid + 1]:
                # Search on the right side
                left = mid + 1
            else:
                # Search on the left size
                right = mid

        return left