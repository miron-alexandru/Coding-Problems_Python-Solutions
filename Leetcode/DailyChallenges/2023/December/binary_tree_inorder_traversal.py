# problem link: https://leetcode.com/problems/binary-tree-inorder-traversal


# my solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            result.append(root.val)
            root = root.right

        return result

