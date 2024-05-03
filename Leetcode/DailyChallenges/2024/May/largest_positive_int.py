# problem link: https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/


# my solution:
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        max_k = -1
        for n in nums:
            if -n in nums and n > max_k:
                max_k = n
        return max_k
