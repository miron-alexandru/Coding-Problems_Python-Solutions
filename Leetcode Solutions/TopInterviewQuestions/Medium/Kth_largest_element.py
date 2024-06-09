# Problem Link: https://leetcode.com/problems/kth-largest-element-in-an-array/


# My Solution:
# use quickselect algorithm
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]

        pivot = random.choice(nums)
        lows = [x for x in nums if x < pivot]
        highs = [x for x in nums if x > pivot]
        pivots = [x for x in nums if x == pivot]

        if k <= len(highs):
            return self.findKthLargest(highs, k)
        elif k <= len(highs) + len(pivots):
            return pivots[0]
        else:
            return self.findKthLargest(lows, k - len(highs) - len(pivots))
