# problem link: https://leetcode.com/problems/largest-perimeter-triangle


# my solution:
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        max_perimeter = 0

        for i in range(n - 2):
            side1 = nums[i]
            side2 = nums[i + 1]
            side3 = nums[i + 2]
            # Check the three sides
            if side1 < side2 + side3:
                # If the sides form a triangle, calculate peri and update max perimeter
                perimeter = side1 + side2 + side3
                max_perimeter = max(max_perimeter, perimeter)

        return max_perimeter
