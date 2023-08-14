# problem link: https://leetcode.com/problems/kth-largest-element-in-an-array


# my solution:
# use quickselect algorithm
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # If input list has only one element return that element (base case)
        if len(nums) == 1:
            return nums[0]

        # Choose a pivot element randomly
        pivot = random.choice(nums)

        # Partition the input list into three sublists based on the pivot element
        lows = [x for x in nums if x < pivot]
        highs = [x for x in nums if x > pivot]
        pivots = [x for x in nums if x == pivot]

        # Compare k with the number of elements in the highs sublist
        if k <= len(highs):
            # If k is less than or equal to the count of elements greater than pivot,
            # recursively find the kth largest element in highs
            return self.findKthLargest(highs, k)
        elif k <= len(highs) + len(pivots):
            # If k is within the range of elements equal to the pivot,
            # return the pivot element as it's the kth largest
            return pivots[0]
        else:
            # If k is greater than the sum of elements greater and equal to the pivot,
            # recursively find the kth largest element in lows
            # Adjust k by subtracting the count of elements greater and equal to the pivot
            return self.findKthLargest(lows, k - len(highs) - len(pivots))