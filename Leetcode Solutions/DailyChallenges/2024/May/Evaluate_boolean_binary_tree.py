# problem link: https://leetcode.com/problems/evaluate-boolean-binary-tree



# solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # Base case
        if root.left is None and root.right is None:
            return bool(root.val)
        
        # evaluate left and right children
        left_val = self.evaluateTree(root.left)
        right_val = self.evaluateTree(root.right)
        
        # Apply the boolean operations
        if root.val == 2:
            return left_val or right_val
        elif root.val == 3:
            return left_val and right_val
        else:
            return False
