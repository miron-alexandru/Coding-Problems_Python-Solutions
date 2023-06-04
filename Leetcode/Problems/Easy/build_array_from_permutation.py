# problem link: https://leetcode.com/problems/build-array-from-permutation


# my solution:
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[num] for num in nums]