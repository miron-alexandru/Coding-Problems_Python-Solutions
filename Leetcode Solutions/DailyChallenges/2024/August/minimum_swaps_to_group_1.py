# problem link: https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/


# my solution:

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k = nums.count(1)
        max_count = count = sum(nums[:k])
        n = len(nums)

        for i in range(k, n + k):
            count += nums[i % n]
            count -= nums[(i - k + n) % n]
            max_count = max(max_count, count)

        return k - max_count