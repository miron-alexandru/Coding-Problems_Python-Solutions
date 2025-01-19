# problem link: https://leetcode.com/problems/trapping-rain-water-ii


# solution
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
