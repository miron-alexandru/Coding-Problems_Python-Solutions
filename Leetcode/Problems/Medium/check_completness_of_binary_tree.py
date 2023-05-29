# problem link: https://leetcode.com/problems/check-completeness-of-a-binary-tree


# my solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = [root]
        end_reached = False
        
        while queue:
            node = queue.pop(0)
            
            # If end has been reached and current node is not a leaf, it's not a complete binary tree
            if end_reached and (node.left or node.right):
                return False
            
            # If left child is None but right child is not None, it's not a complete binary tree
            if not node.left and node.right:
                return False
            
            # Add children to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
            # Mark that the end has been reached
            if not node.right:
                end_reached = True
        
        return True