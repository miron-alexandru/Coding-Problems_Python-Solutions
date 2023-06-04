# problem link: https://leetcode.com/problems/shuffle-the-array


# my solution:

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        mid = len(nums) // 2
        first_half = nums[:mid]
        second_half = nums[mid:]

        for i in range(len(first_half)):
            result.append(first_half[i])
            result.append(second_half[i])

        return result