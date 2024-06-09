# problem link: https://leetcode.com/problems/minimum-absolute-difference-in-bst


# my solution:
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float('inf')
        prev = None

        # Helper func for in-order traversal
        def inorder(node):
            nonlocal min_diff, prev

            if node is None:
                return

            # In-order traversal: left subtree, current node, right subtree
            inorder(node.left)

            # Calculate the absolute diff with the previous node
            if prev is not None:
                min_diff = min(min_diff, abs(node.val - prev.val))

            # Update the previous node
            prev = node

            inorder(node.right)

        # Start the in-order traversal
        inorder(root)

        return min_diff