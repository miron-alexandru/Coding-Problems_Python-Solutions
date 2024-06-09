# problem link: https://leetcode.com/problems/contains-duplicate-ii/


# my solution:
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexed_num = {}
        for i, num in enumerate(nums):
            if num in indexed_num and abs(i - indexed_num[num]) <= k:
                return True
            indexed_num[num] = i
        return False
