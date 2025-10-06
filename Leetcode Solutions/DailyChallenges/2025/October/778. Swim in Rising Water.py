# problem link: https://leetcode.com/problems/swim-in-rising-water/


# Description:
"""
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

It starts raining, and water gradually rises over time. At time t, the water level is t, meaning any cell with elevation less than equal to t is submerged or reachable.

You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the minimum time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

 

Example 1:


Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
Example 2:


Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
"""

# Solution:
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def find(node: int) -> int:
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        n = len(grid)
        parent = list(range(n * n))
        elevation_to_position = [0] * (n * n)
        for row_idx, row in enumerate(grid):
            for col_idx, elevation in enumerate(row):
                elevation_to_position[elevation] = row_idx * n + col_idx

        for time in range(n * n):
            current_cell_idx = elevation_to_position[time]
            current_row = current_cell_idx // n
            current_col = current_cell_idx % n
            directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
            for delta_row, delta_col in directions:
                neighbor_row = current_row + delta_row
                neighbor_col = current_col + delta_col
                if 0 <= neighbor_row < n and 0 <= neighbor_col < n and grid[neighbor_row][neighbor_col] <= time:
                    neighbor_idx = neighbor_row * n + neighbor_col
                    parent[find(neighbor_idx)] = find(current_cell_idx)
            start_idx = 0
            end_idx = n * n - 1
            if find(start_idx) == find(end_idx):
                return time

        return -1
