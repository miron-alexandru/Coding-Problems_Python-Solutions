# problem link: https://leetcode.com/problems/maximum-number-of-fish-in-a-grid


# my solution:
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Helper function for DFS traversal
        def dfs(r: int, c: int) -> int:
            # Check if the current cell is out of bounds or a land cell
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0

            # Catch the fish at the current cell
            fish_count = grid[r][c]

            # Mark the cell as visited by setting it to 0 (land)
            grid[r][c] = 0

            # Explore all four adjacent cells
            fish_count += dfs(r + 1, c)
            fish_count += dfs(r - 1, c)
            fish_count += dfs(r, c + 1)
            fish_count += dfs(r, c - 1)

            return fish_count

        max_fish = 0

        # Iterate over every cell in the grid
        for r in range(m):
            for c in range(n):
                # Start DFS from any water cell
                if grid[r][c] > 0:
                    max_fish = max(max_fish, dfs(r, c))

        return max_fish
