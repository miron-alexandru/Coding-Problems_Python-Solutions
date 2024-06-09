# problem link: https://leetcode.com/problems/path-crossing

# my solution

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = {(0, 0)}
        directions = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}

        for move in path:
            # Update current position
            dx, dy = directions[move]
            x, y = x + dx, y + dy

            # Check if current position has been visited
            if (x, y) in visited:
                return True

            visited.add((x, y))

        return False
