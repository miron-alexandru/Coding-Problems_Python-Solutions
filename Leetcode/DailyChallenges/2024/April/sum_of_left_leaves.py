# problem link: https://leetcode.com/problems/sum-of-left-leaves/


# my solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_leaves_sum = 0

        if root.left and root.left.left is None and root.left.right is None:
            left_leaves_sum += root.left.val

        left_leaves_sum += self.sumOfLeftLeaves(root.left)
        left_leaves_sum += self.sumOfLeftLeaves(root.right)

        return left_leaves_sum


# USING DFS:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, is_left):
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val if is_left else 0
            return dfs(node.left, True) + dfs(node.right, False)

        return dfs(root, False)
