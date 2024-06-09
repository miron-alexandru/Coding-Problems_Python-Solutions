# problem link: https://leetcode.com/problems/check-if-it-is-a-straight-line


# my solution:
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # get first two points
        (x0, y0), (x1, y1) = coordinates[0], coordinates[1]
        
        # Check the slope of the line connecting them
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            # Check if the slope between each point and the first point is equal to the original slope
            if (x0 - x1) * (y1 - y) != (x1 - x) * (y0 - y1):
                return False
        
        # If all slopes are equal, return True
        return True