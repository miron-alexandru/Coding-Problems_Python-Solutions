# problem link: https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points



# my solution:
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])

        # Initialize maximum width
        max_width = 0

        # find the maximum width
        for i in range(1, len(points)):
            max_width = max(max_width, points[i][0] - points[i - 1][0])

        return max_width