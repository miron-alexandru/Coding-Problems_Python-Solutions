# problem link: https://leetcode.com/problems/sort-colors/


# my solution:
# used DNF algorithm
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        r, w, b = 0, 0, len(nums) - 1

        while w <= b:
            if nums[w] < 1:  # element is red
                nums[r], nums[w] = nums[w], nums[r]
                r += 1
                w += 1
            elif nums[w] > 1:  # element is blue
                nums[b], nums[w] = nums[w], nums[b]
                b -= 1
            else:  # element is white
                w += 1
