# problem link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/


# my solutions:

# brute force:
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]:
                    count += 1
            result.append(count)
        return result

# list comprehension:
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [sum(num > x for x in nums) for num in nums]