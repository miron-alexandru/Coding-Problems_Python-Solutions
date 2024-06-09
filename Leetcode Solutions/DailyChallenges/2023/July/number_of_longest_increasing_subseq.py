# problem link: https://leetcode.com/problems/number-of-longest-increasing-subsequence


# my solution:

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        lengths = [1] * n
        counts = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[i] == lengths[j] + 1:
                        counts[i] += counts[j]
                    elif lengths[i] < lengths[j] + 1:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]

        max_length = max(lengths)
        result = 0
        for i in range(n):
            if lengths[i] == max_length:
                result += counts[i]

        return result