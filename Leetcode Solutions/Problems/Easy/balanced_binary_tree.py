# problem link: https://leetcode.com/problems/balanced-binary-tree/


# my solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance(node):
            if node is None:
                return 0

            left_height = check_balance(node.left)
            right_height = check_balance(node.right)

            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1

            return max(left_height, right_height) + 1

        return check_balance(root) != -1


        left_height = height(root.left)
        right_height = height(root.right)

        if abs(left_height - right_height) > 1:
            return False

        balanced_l = self.isBalanced(root.left)
        balanced_r = self.isBalanced(root.right)

        return balanced_l and balanced_r
