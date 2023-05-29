# problem link: https://leetcode.com/problems/diameter-of-binary-tree


# my solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxDepthAndDiameter(node):
            nonlocal max_diameter

            if node is None:
                return 0

            left_depth = maxDepthAndDiameter(node.left)
            right_depth = maxDepthAndDiameter(node.right)

            current_diameter = left_depth + right_depth
            max_diameter = max(max_diameter, current_diameter)

            return max(left_depth, right_depth) + 1

        max_diameter = 0
        maxDepthAndDiameter(root)
        return max_diameter
