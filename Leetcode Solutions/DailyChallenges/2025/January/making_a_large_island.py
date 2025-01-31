# problem link: https://leetcode.com/problems/making-a-large-island/


# solution:
from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Assign labels to islands and calculate their sizes
        label = 2  # Start labeling from 2 (since 0 and 1 are already used)
        island_sizes = {}
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    size = self.dfs(grid, i, j, label)
                    island_sizes[label] = size
                    label += 1
        
        # Check each 0 and calculate the potential island size
        max_size = max(island_sizes.values()) if island_sizes else 0
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbors = set()
                    for dx, dy in directions:
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < n and grid[x][y] > 1:
                            neighbors.add(grid[x][y])
                    
                    # Sum the sizes of neighboring islands and add 1 for the current cell
                    current_size = 1 + sum(island_sizes[label] for label in neighbors)
                    max_size = max(max_size, current_size)
        
        return max_size
    
    def dfs(self, grid: List[List[int]], i: int, j: int, label: int) -> int:
        n = len(grid)
        if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
            return 0
        
        grid[i][j] = label
        size = 1
        size += self.dfs(grid, i + 1, j, label)
        size += self.dfs(grid, i - 1, j, label)
        size += self.dfs(grid, i, j + 1, label)
        size += self.dfs(grid, i, j - 1, label)
        
        return size