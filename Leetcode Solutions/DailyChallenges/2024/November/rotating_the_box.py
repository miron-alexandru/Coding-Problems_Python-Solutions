# problem link: https://leetcode.com/problems/rotating-the-box


# solution (not mine):
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # First, get the dimensions of the box
        rows, cols = len(box), len(box[0])
      
        # Initialize the answer matrix with None, rotated 90 degrees
        rotated_box = [[None] * rows for _ in range(cols)]
      
        # Rotate the box 90 degrees clockwise to the right
        for row in range(rows):
            for col in range(cols):
                rotated_box[col][rows - row - 1] = box[row][col]
      
        # For each column of the rotated box (which were rows in the original box)
        for col in range(rows):
            queue = deque()  # Initialize a queue to store the positions of empty '.' slots
            # Start from bottom and go upwards
            for row in reversed(range(cols)):
                # When we see an obstacle '*', we clear the queue as it can't be passed
                if rotated_box[row][col] == '*':
                    queue.clear()
                # If it's empty '.', add this position to the queue
                elif rotated_box[row][col] == '.':
                    queue.append(row)
                # When we find a stone '#', and there is an available position below it (recorded in the queue)
                elif queue:
                    new_pos = queue.popleft()  # Take the lowest available position
                    rotated_box[new_pos][col] = '#'  # Move the stone to the new position
                    rotated_box[row][col] = '.'  # Update the old position to empty '.'
                    queue.append(row)  # The old position is now a new empty position
        return rotated_box