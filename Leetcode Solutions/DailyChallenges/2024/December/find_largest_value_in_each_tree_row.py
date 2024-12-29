# problem link: https://leetcode.com/problems/find-largest-value-in-each-tree-row/


# my solution:
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # Initialize the queue for BFS
        queue = deque([root])
        largest_values = []
        
        while queue:
            level_size = len(queue)
            max_value = float('-inf')
            
            for _ in range(level_size):
                node = queue.popleft()
                max_value = max(max_value, node.val)
                
                # Add child nodes to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Append the largest value in the current level to the result list
            largest_values.append(max_value)
        
        return largest_values
