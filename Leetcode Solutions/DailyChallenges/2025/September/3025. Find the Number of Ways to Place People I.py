# problem link: https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/


# Description:
"""
You are given a 2D array points of size n x 2 representing integer coordinates of some points on a 2D plane, where points[i] = [xi, yi].

Count the number of pairs of points (A, B), where

A is on the upper left side of B, and
there are no other points in the rectangle (or line) they make (including the border).
Return the count.

 

Example 1:

Input: points = [[1,1],[2,2],[3,3]]

Output: 0

Explanation:



There is no way to choose A and B so A is on the upper left side of B.

Example 2:

Input: points = [[6,2],[4,4],[2,6]]

Output: 2

Explanation:



The left one is the pair (points[1], points[0]), where points[1] is on the upper left side of points[0] and the rectangle is empty.
The middle one is the pair (points[2], points[1]), same as the left one it is a valid pair.
The right one is the pair (points[2], points[0]), where points[2] is on the upper left side of points[0], but points[1] is inside the rectangle so it's not a valid pair.
Example 3:

Input: points = [[3,1],[1,3],[1,1]]

Output: 2

Explanation:



The left one is the pair (points[2], points[0]), where points[2] is on the upper left side of points[0] and there are no other points on the line they form. Note that it is a valid state when the two points form a line.
The middle one is the pair (points[1], points[2]), it is a valid pair same as the left one.
The right one is the pair (points[1], points[0]), it is not a valid pair as points[2] is on the border of the rectangle.
."""

# Solution:
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # sort by x ascending and for equal x by y descending
        # this ensures when we scan left points come before right ones
        points.sort(key=lambda x: (x[0], -x[1]))
        
        ans = 0
        # iterate each point as the upper-left candidate
        for i, (_, y1) in enumerate(points):
            max_y = -inf  # track the highest y seen so far on the right side
            
            # look at all points to the right of current point
            for _, y2 in points[i + 1:]:
                # valid lower-right corner must satisfy:
                #  y2 is not higher than y1, and y2 is strictly larger than all previous y2 checked
                if max_y < y2 <= y1:
                    max_y = y2   # update best candidate height
                    ans += 1     # count this pair as valid
        
        return ans