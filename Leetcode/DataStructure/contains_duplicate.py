# problem link: https://leetcode.com/problems/contains-duplicate


# my solution:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()  # sort the input array in-place
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
