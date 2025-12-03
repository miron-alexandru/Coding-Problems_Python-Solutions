# problem link: https://leetcode.com/problems/count-number-of-trapezoids-ii/


# Description
"""
You are given a 2D integer array points where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.

Return the number of unique trapezoids that can be formed by choosing any four distinct points from points.

A trapezoid is a convex quadrilateral with at least one pair of parallel sides. Two lines are parallel if and only if they have the same slope.

 

Example 1:

Input: points = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]

Output: 2

Explanation:



There are two distinct ways to pick four points that form a trapezoid:

The points [-3,2], [2,3], [3,2], [2,-3] form one trapezoid.
The points [2,3], [3,2], [3,0], [2,-3] form another trapezoid.
Example 2:

Input: points = [[0,0],[1,0],[0,1],[2,1]]

Output: 1

Explanation:



There is only one trapezoid which can be formed.
"""

# Solution:
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)

        # cnt1: k -> (b -> count)
        cnt1: dict[float, dict[float, int]] = defaultdict(lambda: defaultdict(int))
        # cnt2: p -> (k -> count)
        cnt2: dict[int, dict[float, int]] = defaultdict(lambda: defaultdict(int))

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i):
                x2, y2 = points[j]
                dx, dy = x2 - x1, y2 - y1

                if dx == 0:
                    k = 1e9
                    b = x1
                else:
                    k = dy / dx
                    b = (y1 * dx - x1 * dy) / dx

                cnt1[k][b] += 1

                p = (x1 + x2 + 2000) * 4000 + (y1 + y2 + 2000)
                cnt2[p][k] += 1

        ans = 0

        for e in cnt1.values():
            s = 0
            for t in e.values():
                ans += s * t
                s += t

        for e in cnt2.values():
            s = 0
            for t in e.values():
                ans -= s * t
                s += t

        return ans