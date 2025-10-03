# problem link: https://leetcode.com/problems/trapping-rain-water-ii/


# Description:
"""
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

 

Example 1:


Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.
Example 2:


Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10
"""

# Solution:
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        rows, cols = len(heightMap), len(heightMap[0])
        visited = [[False] * cols for _ in range(rows)]
        priority_queue = []
        
        for row in range(rows):
            for col in range(cols):
                if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                    heappush(priority_queue, (heightMap[row][col], row, col))
                    visited[row][col] = True
        
        total_water = 0
        directions = (-1, 0, 1, 0, -1)
        
        while priority_queue:
            height, row, col = heappop(priority_queue)
            for delta_row, delta_col in pairwise(directions):
                new_row, new_col = row + delta_row, col + delta_col
                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and not visited[new_row][new_col]
                ):
                    total_water += max(0, height - heightMap[new_row][new_col])
                    visited[new_row][new_col] = True
                    heappush(priority_queue, (max(height, heightMap[new_row][new_col]), new_row, new_col))
        
        return total_water
