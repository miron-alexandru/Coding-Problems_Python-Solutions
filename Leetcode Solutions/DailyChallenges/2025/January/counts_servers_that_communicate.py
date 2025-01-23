# problem link: https://leetcode.com/problems/count-servers-that-communicate/


# solution:
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # Dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        
        # Arrays to store the number of servers in each row and column
        row_count = [0] * rows
        col_count = [0] * cols
        
        # Count the number of servers in each row and column
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        
        # Count the number of servers that are not isolated
        communicating_servers = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    communicating_servers += 1
        
        return communicating_servers
