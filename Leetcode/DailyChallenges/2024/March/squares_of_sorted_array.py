# problem link: https://leetcode.com/problems/squares-of-a-sorted-array/

# my solution:
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([n ** 2 for n in nums])
