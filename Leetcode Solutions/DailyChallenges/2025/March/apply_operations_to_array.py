# problem link: https://leetcode.com/problems/apply-operations-to-an-array/



# my solution:
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        def move_zeros(arr):
            return [num for num in arr if num != 0] + [0] * arr.count(0)

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        ans = move_zeros(nums)
        return ans