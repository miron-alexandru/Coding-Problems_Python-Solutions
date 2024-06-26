# problem link: https://leetcode.com/problems/set-mismatch



# my solution:
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for num in nums:
            if nums[abs(num) - 1] < 0:
                duplicate = abs(num)
            else:
                nums[abs(num) - 1] *= -1

        for i, num in enumerate(nums):
            if num > 0:
                return [duplicate, i + 1]