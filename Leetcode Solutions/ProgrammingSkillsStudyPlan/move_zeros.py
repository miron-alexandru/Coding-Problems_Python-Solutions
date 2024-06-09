# problem link: https://leetcode.com/problems/move-zeroes


# my solution:
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        nums[j:] = [0] * (n - j)