# problem link: https://leetcode.com/problems/balanced-binary-tree/

# Description:
"""
Given a binary tree, determine if it is height-balanced.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
"""


# Solution:
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0

            left_h = height(node.left)
            if left_h == -1:
                return -1

            right_h = height(node.right)
            if right_h == -1:
                return -1

            if abs(left_h - right_h) > 1:
                return -1

            return max(left_h, right_h) + 1

        return height(root) != -1