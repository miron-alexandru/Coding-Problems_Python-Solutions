# problem link: https://leetcode.com/problems/permutations/


# My Solution:
import itertools


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(iterools.permutations(nums))
