# problem link: https://leetcode.com/problems/find-pivot-index


# my solution:
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for i, n in enumerate(nums):
            # calculate the right sum as the diff between the total sum and the left and current n
            right_sum = total_sum - left_sum - n
            if left_sum == right_sum:
                return i
            else:
                left_sum += n
        return -1