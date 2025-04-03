# problem link: https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/



# my solution:
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_value = max_num = max_diff = 0
        for num in nums:
            max_value = max(max_value, max_diff * num)
            max_diff = max(max_diff, max_num - num)
            max_num = max(max_num, num)
        return max_value
            