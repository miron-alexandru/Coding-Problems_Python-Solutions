# problem link: https://leetcode.com/problems/two-sum


# solution:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_num = {}
        # calculate the difference between target and the current element
        for i, num in enumerate(nums):
            diff = target - num
            # if diff exists in the dict we found the pair that add up to the targed
            if diff in dict_num:
                return [dict_num[diff], i]
            dict_num[num] = i

        return []
