# problem link: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated


# my solution:
class Solution:
    def check(self, nums: List[int]) -> bool:
        count_breaks = 0
        n = len(nums)

        if n <= 1:
            return True

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count_breaks += 1

        return count_breaks <= 1
