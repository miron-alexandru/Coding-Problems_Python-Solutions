# problem link: https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate


# my solution:
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance = float("inf")
        min_index = -1

        for i, point in enumerate(points):
            ai, bi = point

            # Check if the point has the same x or y coord
            if ai == x or bi == y:
                # Calculate the Manhattan distance between the current location and the point
                distance = abs(x - ai) + abs(y - bi)

                # if necessary update min distance and min index
                if distance < min_distance:
                    min_distance = distance
                    min_index = i

        return min_index
