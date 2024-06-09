# problem link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array


# my solution:
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            first_occurrence = -1

            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    first_occurrence = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return first_occurrence

        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            last_occurrence = -1

            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    last_occurrence = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return last_occurrence

        first = findFirst(nums, target)
        last = findLast(nums, target)

        return [first, last]