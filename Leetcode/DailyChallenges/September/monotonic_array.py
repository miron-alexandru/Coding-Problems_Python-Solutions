# problem link: https://leetcode.com/problems/monotonic-array


# my solution:

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isIncreasing = True
        isDecreasing = True
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                isDecreasing = False
            elif nums[i] < nums[i-1]:
                isIncreasing = False
                
            if not isIncreasing and not isDecreasing:
                return False
        
        return True
