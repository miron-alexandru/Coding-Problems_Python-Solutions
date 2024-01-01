# problem link: https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs


# solution (not mine):
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        nums.sort()
        left, right = 0, nums[n - 1] - nums[0]
        
        while left < right:
            mid = (left + right) // 2
            if self.countValidPairs(nums, mid, p) >= p:
                right = mid
            else:
                left = mid + 1
        return left
    
    def countValidPairs(self, nums: List[int], max_diff: int, p: int) -> int:
        i, valid_pairs = 1, 0
        
        while i < len(nums):
            if nums[i] - nums[i - 1] <= max_diff:
                i += 1
                valid_pairs += 1
            i += 1
        return valid_pairs