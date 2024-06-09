# problem link: https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/


# my solution:
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()

        for x in range(len(nums) + 1):
            count = sum(num >= x for num in nums)
            if count == x:
                return x
        return - 1