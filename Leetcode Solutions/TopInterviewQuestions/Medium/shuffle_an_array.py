# problem link: https://leetcode.com/problems/shuffle-an-array/


# my solution:
# solved using Fisher Yates shuffle algorithm
import random


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = list(nums)

    def reset(self) -> List[int]:
        self.nums = list(self.original)
        self.original = list(self.original)
        return self.nums

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums) - 1, 0, -1):
            j = random.randint(0, i)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums
