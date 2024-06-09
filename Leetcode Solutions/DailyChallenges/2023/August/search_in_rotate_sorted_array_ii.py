# problem link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii


# my solution:
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
    
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return True
            
            # If left segment is sorted
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # If right segment is sorted
            elif nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            # Duplicates so we move left pointer
            else:
                left += 1
                
        return False