# problem link: https://leetcode.com/problems/walking-robot-simulation/



# my solution:
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Directions correspond to [North, East, South, West]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Initial position and direction (facing North)
        x, y = 0, 0
        direction_index = 0  # Initially facing North
        max_distance = 0

        # Convert the list of obstacles to a set for quick lookup
        obstacle_set = set(map(tuple, obstacles))

        for command in commands:
            if command == -2:  # Turn left 90 degrees
                direction_index = (direction_index + 3) % 4
            elif command == -1:  # Turn right 90 degrees
                direction_index = (direction_index + 1) % 4
            else:
                # Move forward k units
                for _ in range(command):
                    next_x = x + directions[direction_index][0]
                    next_y = y + directions[direction_index][1]
                    if (next_x, next_y) not in obstacle_set:
                        x, y = next_x, next_y
                        max_distance = max(max_distance, x**2 + y**2)
                    else:
                        # Hit an obstacle, stop moving in this direction
                        break

        return max_distance