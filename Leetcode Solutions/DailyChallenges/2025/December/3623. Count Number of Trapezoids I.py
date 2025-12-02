# problem link: https://leetcode.com/problems/count-number-of-trapezoids-i/

# Description:
You are given a 2D integer array points, where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.

A horizontal trapezoid is a convex quadrilateral with at least one pair of horizontal sides (i.e. parallel to the x-axis). Two lines are parallel if and only if they have the same slope.

Return the number of unique horizontal trapezoids that can be formed by choosing any four distinct points from points.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: points = [[1,0],[2,0],[3,0],[2,2],[3,2]]

Output: 3

Explanation:



There are three distinct ways to pick four points that form a horizontal trapezoid:

Using points [1,0], [2,0], [3,2], and [2,2].
Using points [2,0], [3,0], [3,2], and [2,2].
Using points [1,0], [3,0], [3,2], and [2,2].
Example 2:

Input: points = [[0,0],[1,0],[0,1],[2,1]]

Output: 1

Explanation:



There is only one horizontal trapezoid that can be formed.
"""

# Solution:
class Solution:
    def countTrapezoids(self, points):
        mod = 10**9 + 7
        
        by_y = {}
        for x, y in points:
            by_y.setdefault(y, 0)
            by_y[y] += 1
        
        pair_count = []
        for y in by_y:
            c = by_y[y]
            if c >= 2:
                pair_count.append(c * (c - 1) // 2)
        
        m = len(pair_count)
        if m < 2:
            return 0
        
        s = 0
        prefix = 0
        for pc in sorted(pair_count):
            s = (s + prefix * pc) % mod
            prefix = (prefix + pc) % mod
        
        return s % mod
