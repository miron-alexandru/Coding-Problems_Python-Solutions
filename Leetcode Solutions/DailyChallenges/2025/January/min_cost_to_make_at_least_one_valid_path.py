# problem link: https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/



# solution:
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # Dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        
        # Direction offsets: index matches grid values (1 to 4)
        # dirs[0] is a placeholder for 1-based indexing
        directions = [[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0]]
        
        # Queue for BFS: stores tuples of (row, col, cost)
        queue = deque([(0, 0, 0)])
        
        # Set to track visited cells
        visited = set()
        
        while queue:
            row, col, cost = queue.popleft()
            
            # Skip if already visited
            if (row, col) in visited:
                continue
            
            # Mark the cell as visited
            visited.add((row, col))
            
            # If we reach the bottom-right corner, return the cost
            if row == rows - 1 and col == cols - 1:
                return cost
            
            # Explore all possible directions
            for direction in range(1, 5):
                new_row = row + directions[direction][0]
                new_col = col + directions[direction][1]
                
                # Check if the new position is within bounds
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    # If the current cell's direction matches, no additional cost
                    if grid[row][col] == direction:
                        queue.appendleft((new_row, new_col, cost))
                    # Otherwise, add 1 to the cost
                    else:
                        queue.append((new_row, new_col, cost + 1))
        
        # If no path is found (though this shouldn't occur in valid grids)
        return -1
