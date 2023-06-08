# problem link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix


# my solutions:
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            for element in row:
                if element < 0:
                    count += 1
        return count


# using binary search:
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        num_rows = len(grid)
        num_cols = len(grid[0]) if num_rows > 0 else 0

        for row in grid:
            left = 0
            right = num_cols - 1

            while left <= right:
                mid = left + (right - left) // 2
                if row[mid] < 0:
                    count += (right - mid + 1)
                    right = mid - 1
                else:
                    left = mid + 1
        return count