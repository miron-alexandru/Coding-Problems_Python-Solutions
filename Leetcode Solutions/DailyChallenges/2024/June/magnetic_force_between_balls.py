# problem link: https://leetcode.com/problems/magnetic-force-between-two-balls/



# my solution:
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # Sort the positions
        position.sort()
        
        n = len(position)
        # Initialize binary search bounds
        left = 1  # smallest possible force
        right = position[n-1] - position[0]  # largest possible force
        best_force = 0

        # Define the feasibility function to check if we can place m balls
        # such that the minimum distance between any two is at least F
        def canPlaceBalls(position, m, F):
            # Place the first ball in the first basket
            last_placed_position = position[0]
            balls_placed = 1  # One ball is already placed
            
            # Iterate through the remaining baskets to place the remaining balls
            for i in range(1, n):
                # Check if the current basket is at least F distance away from the last placed ball
                if position[i] - last_placed_position >= F:
                    # Place the ball in the current basket
                    balls_placed += 1
                    last_placed_position = position[i]  # Update the position of the last placed ball
                    
                    # If all m balls have been placed return True
                    if balls_placed == m:
                        return True
            
            # If not all balls have been placed return False
            return False

        # Perform binary search to find the maximum minimum force
        while left <= right:
            mid = (left + right) // 2
            if canPlaceBalls(position, m, mid):
                best_force = mid  # Update the best force found
                left = mid + 1  # Try for a larger force
            else:
                right = mid - 1  # Try for a smaller force

        return best_force