# problem link: https://leetcode.com/problems/permutations


# my solution:
import itertools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))