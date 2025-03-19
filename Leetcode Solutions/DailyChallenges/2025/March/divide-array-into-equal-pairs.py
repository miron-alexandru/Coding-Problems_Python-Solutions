# problem link: https://leetcode.com/problems/divide-array-into-equal-pairs/


# solution:


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)
        return all(v % 2 == 0 for v in count.values())