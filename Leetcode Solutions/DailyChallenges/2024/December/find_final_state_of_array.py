# problem link: https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/

# my solution:
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            min_value = min(nums)
            index = nums.index(min_value)
            nums[index] = min_value * multiplier

        return nums