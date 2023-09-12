# problem link: https://leetcode.com/problems/path-sum


# my solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return 0

        s = 0
        subSum = targetSum - root.val

        if (subSum == 0 and root.left == None and root.right == None):
            return True
        
        if root.left is not None:
            s = s or self.hasPathSum(root.left, subSum)
        if root.right is not None:
            s = s or self.hasPathSum(root.right, subSum)

        return s
        