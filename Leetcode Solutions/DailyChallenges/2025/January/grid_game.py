# problem link: https://leetcode.com/problems/grid-game/


# solution:

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        
        # Compute prefix sums for the rows
        prefix_top = [0] * n
        prefix_bottom = [0] * n
        
        # Prefix sum for the top row
        prefix_top[0] = grid[0][0]
        for i in range(1, n):
            prefix_top[i] = prefix_top[i - 1] + grid[0][i]
        
        # Prefix sum for the bottom row
        prefix_bottom[0] = grid[1][0]
        for i in range(1, n):
            prefix_bottom[i] = prefix_bottom[i - 1] + grid[1][i]
        
        # Initialize the result to a large value
        result = float('inf')
        
        # Iterate over all possible switching points
        for i in range(n):
            # Points left for the second robot to collect
            top_remaining = prefix_top[-1] - prefix_top[i]  # Points on the top row after i
            bottom_remaining = prefix_bottom[i - 1] if i > 0 else 0  # Points on the bottom row before i
            
            # The second robot will collect the maximum of the two remaining sections
            second_robot_points = max(top_remaining, bottom_remaining)
            
            # Minimize the maximum points the second robot can collect
            result = min(result, second_robot_points)
        
        return result
