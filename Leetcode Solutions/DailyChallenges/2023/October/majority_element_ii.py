# problem link: https://leetcode.com/problems/majority-element-ii


# my solution:
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        count = {}
        result = []

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        n = len(nums)
        threshold = n // 3

        for num, freq in count.items():
            if freq > threshold:
                result.append(num)

        return result