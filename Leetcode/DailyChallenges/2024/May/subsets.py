# problem link: https://leetcode.com/problems/subsets/


# my solution:

import itertools

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        for i in range(len(nums) + 1):
            for subset in itertools.combinations(nums, i):
                subsets.append(list(subset))
        return subsets
