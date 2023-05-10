# Problem Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/


# My Solution:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 0 depth node
        if root == None:
            return 0

        left_subtree_depth = self.maxDepth(root.left)
        right_subtree_depth = self.maxDepth(root.right)
        if left_subtree_depth > right_subtree_depth:
            return left_subtree_depth + 1
        else:
            return right_subtree_depth + 1
