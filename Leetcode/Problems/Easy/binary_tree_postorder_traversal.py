# problem link: https://leetcode.com/problems/binary-tree-postorder-traversal/


# my solutions:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive:

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: 
            return []
        return(self.postorderTraversal(root.left) + 
            self.postorderTraversal(root.right) +
            [root.val])


# iterative:

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()

            if visited:
                # If the node has been visited, add its value to the result
                result.append(node.val)
            else:
                # If the node hasn't been visited, push it back to the stack with visited flag as True
                stack.append((node, True))

                # Push the right child with visited flag as False
                if node.right:
                    stack.append((node.right, False))

                # Push the left child with visited flag as False
                if node.left:
                    stack.append((node.left, False))

        return result